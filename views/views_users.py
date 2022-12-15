from flask import request
from datetime import datetime, timedelta, timezone
import bcrypt
import jwt
from config import get_config
from exceptions import BadRequestException, InputException
from sql import get_mariadb_connection
from validations.input import check_login

# RESPONSE CODE HTTP
# 2XX - OK
# 3XX - REDIRECTION
# 4XX - BAD REQUEST / FORBIDDEN / NOT FOUND
# 5XX - INTERNAL ERROR

# Fonction permettant d'enregistrer un nouvel utilisateur


def register_user():
    try:
        # Récupérations des inputs de la requête
        input_data = request.get_json()

        # La fonction check_login va vérifier qu'il n'y a pas de caractères non souhaités dans le login
        # Si le login ne convient pas, une exception de type InputException sera levée.
        check_login(input_data["login"])

        # On génère le hash du mot de pass
        password = input_data["password"].encode()
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password, salt)

        # On récupère l'instance de connexion à la BDD pour enregistrer le nouvel utilisateur
        conn = get_mariadb_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO users (login, password)
            VALUES (?,?)
            """, (input_data["login"], hashed))

        # On retourne la réponse du serveur, pour indiquer que l'enregistrement s'est bien passé
        return {"success": "created"}, 201

    # Si quelque chose s'est mal passé et qu'une exception est levée, alors on retourne les réponses ci-dessous
    # selon l'exception levée.
    except InputException as e:
        # On retourne le message de l'exception
        return {"error": str(e)}, 403
    except Exception as e:
        print(str(e))
        # Dans le cas d'une exception non maîtrisée (générique), on ne retourne pas le message de l'exception
        # qui pourrait donner des informations techniques à un éventuel hacker.
        return {"error": "Internal error"}, 500


# Fonction permettant d'authentifier un utilisateur avec son login et son mot de passe
def auth_user():
    try:
        input_data = request.get_json()

        if input_data is None or "login" not in input_data or "password" not in input_data:
            raise BadRequestException("Missing parameters")

        check_login(input_data["login"])

        conn = get_mariadb_connection()
        cursor = conn.cursor()
        # On récupère le MDP correspondant au login
        cursor.execute(
            """
                SELECT id, password
                FROM users
                WHERE login = ?
                """, (input_data["login"],))

        auth_row = cursor.fetchone()

        # S'il n'y a pas d'identifiant correspondant, on retourne une erreur
        if auth_row is None:
            # On ne donne pas d'indication sur le fait que l'identifiant n'existe pas, sinon il devient possible de trouver
            # des identifiants existants par bruteforce
            return {"error": "Invalid credentials"}, 403

        fetched_id = auth_row[0]
        fetched_password = auth_row[1]

        # Si le mdp correspond, on retourne un JWT, sinon une erreur
        if bcrypt.checkpw(input_data["password"].encode(), fetched_password.encode()):
            jwt_config = get_config()["jwt"]
            # On créé le token JWT. sub = subject (l'utilisateur), iat = issued at (date à laquelle le token a été délivré), exp = expiration (date d'expiration du token)
            issued_at = datetime.now(timezone.utc)
            encoded_jwt = jwt.encode(
                {
                    "sub": fetched_id,
                    "iat": datetime.timestamp(issued_at),
                    "exp": datetime.timestamp(issued_at + timedelta(hours=2))
                },
                jwt_config["secret"],
                jwt_config["algorithm"]
            )
            return {"token": encoded_jwt}, 200
        else:
            return {"error": "Invalid credentials"}, 403

    except BadRequestException as e:
        # Exception levée si il manque le login ou le password dans le corps de la requête (input_data)
        return {"error": str(e)}, 400
    except InputException as e:
        # Exception pouvant être levée par la fonction check_login
        return {"error": str(e)}, 403
    except Exception as e:
        print(str(e))
        # Exception générique pouvant être levée par n'importe quelle fonction en cas de dysfonctionnement
        # (par exemple le service mariadb arrêté)
        # Pas soucis de sécurité, on ne retourne pas le message de l'exception car on ne sait pas quel type de message peut être retourné
        return {"error": "Internal error"}, 500
