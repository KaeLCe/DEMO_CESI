import mariadb
import sys
from config import get_config


#Fonction à appeler pour récupérer l'instance de connexion à la BDD.
def get_mariadb_connection():
    #La fonction get_config() permet de charger en mémoire le fichier config.json.
    #En ajoutant derrière la clef "mariadb", je ne récupère que la partie du json qui se trouve derrière la clef "mariadb".
    maria_db_config = get_config()["mariadb"]
    #Try / Except permet de dire au programme : si ça se passe mal, exécute le code que je mets dans le bloc "except".
    #En l'occurence, la fonction sys.exit(1) indique au programme de se fermer complètement. Autrement dit, si il y a un problème
    #de communication avec la BDD (service mariadb arrêté par exemple), le serveur web s'arrêtera.
    try:
        conn = mariadb.connect(
            user=maria_db_config["user"],
            password=maria_db_config["password"],
            host=maria_db_config["host"],
            port=maria_db_config["port"],
            database=maria_db_config["database"]
        )
        #Par défaut, privilégier le mode autocommit = True. Pour les curieux, si on désactive l'autocommit (= False), c'est pour faire du transactionnel.
        #Le transactionnel c'est dire au programme ceci : je vais faire plusieurs requêtes SQL à la suite, si une seule de ces requêtes plante,
        #alors on rollback l'ensemble des requêtes SQL de la transaction.
        conn.autocommit = True
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    #A la fin, on retourne l'objet de connexion à la BDD (l'instance de connexion) à celui qui appelle la fonction get_mariadb_connection.
    return conn