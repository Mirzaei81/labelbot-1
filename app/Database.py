import logging.config
import mysql.connector
import logging
logger = logging.getLogger(__name__)

try:
    connection = mysql.connector.connect(
            user="root",
            password="TGIydaGzqj8nkXiR40rkLRtH0HSlkGPL",
            host="a6aeb8a2-34b1-4713-b85c-7375e8c5aff2.hsvc.ir",
            database="mainDB",
            port=30248
    )
    print("Connected to MySQL successfully.")
    print(connection)
    executer=connection.cursor()
except mysql.connector.Error as err:
    logger.error(f"Failed to connect to MySQL: {err}")
    

def main():
    ...


def GetCredits(username):
    try:
        connection = mysql.connector.connect(
                user="root",
                password="TGIydaGzqj8nkXiR40rkLRtH0HSlkGPL",
                host="a6aeb8a2-34b1-4713-b85c-7375e8c5aff2.hsvc.ir",
                database="mainDB",
                port=30248
        )
        print("Connected to MySQL successfully.")
        print(connection)
        executer=connection.cursor()
    except mysql.connector.Error as err:
        logger.error(f"Failed to connect to MySQL: {err}")
    executer.execute('Select Credits FROM users WHERE UserName = "{}"'.format(username))
    result=executer.fetchone()
    result=result[0]
    print(result)
    return result

def LoseCredits(username):
    try:
        connection = mysql.connector.connect(
                user="root",
                password="TGIydaGzqj8nkXiR40rkLRtH0HSlkGPL",
                host="a6aeb8a2-34b1-4713-b85c-7375e8c5aff2.hsvc.ir",
                database="mainDB",
                port=30248
        )
        print("Connected to MySQL successfully.")
        print(connection)
        executer=connection.cursor()
        executer.execute('UPDATE users SET credits = credits-1 WHERE UserName = "{}"'.format(username))
    except mysql.connector.Error as err:
        logger.error(f"Failed to connect to MySQL: {err}")


        
if __name__=="__main__":
    main()