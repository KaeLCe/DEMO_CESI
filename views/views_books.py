from flask import request
import jwt
from jwt.exceptions import InvalidSignatureError, ExpiredSignatureError
import json
from config import get_config
from sql import get_mariadb_connection


def get_books():
    result = []
    try:
        encoded_jwt = request.headers.get('Authorization').split(" ")[1]
        jwt_config = get_config()["jwt"]

        # La fonction jwt.decode va vérifier l'intégrité du token. En cas de problème, une exception sera levée
        decoded_jwt = jwt.decode(
            encoded_jwt, jwt_config["secret"], algorithms=jwt_config["algorithm"])

        # Si nous sommes ici dans le code, sans qu'une exception ait été levée, c'est que le token est valide.
        # On peut alors aller chercher des données que seuls les utilisateurs authentifiés peuvent voir
        # Pour l'exemple il s'agit simplement de titre de livres enregistrés en BDD
        conn = get_mariadb_connection()
        cursor = conn.cursor()
        cursor.execute(
                """
                SELECT id, title
                FROM books
                """)

        book_rows = cursor.fetchall()

        for book_row in book_rows:
            result.append({"id": book_row[0], "title": book_row[1]})

        return json.dumps(result), 200

    except ExpiredSignatureError as e:
        return {"error": "JWT expired"}, 401
    except InvalidSignatureError as e:
        return {"error": "Are you trying to compromise the JWT ?"}, 403
    except Exception as e:
        return {"error": "Internal error"}, 500
