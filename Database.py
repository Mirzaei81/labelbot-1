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
except mysql.connector.Error as err:
    logger.error(f"Failed to connect to MySQL: {err}")
    

def main():
    ...

def CheckUser(username):
    print(username)
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
        executer.execute('Select UserName FROM users WHERE UserName ="{}"'.format(username))
        result=executer.fetchall()
        
    except mysql.connector.Error as err:
        logger.error(f"Failed to connect to MySQL: {err}")
    if result==[]:
        print("no such column")
        return False
    else:
        return True
def CreateUser(username):
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
        
        executer.execute('INSERT INTO mainDB.users (UserName,Credits) VALUES ("{0}",{1})'.format(username,10))
        connection.commit()
        print(executer.warnings)
        print("inserted!")
        return True
    
    except mysql.connector.Error as err:
        logger.error(f"Failed to connect to MySQL: {err}")    

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
        executer.execute('Select Credits FROM users WHERE UserName = "{}"'.format(username))
        result=executer.fetchone()
        
        print(result)
        result=result[0]
        print(result)
        return result
    except mysql.connector.Error as err:
        logger.error(f"Failed to connect to MySQL: {err}")


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
        executer.execute('UPDATE users SET Credits = Credits-1 WHERE UserName = "{}"'.format(username))
        connection.commit()
    except mysql.connector.Error as err:
        logger.error(f"Failed to connect to MySQL: {err}")

#info is a list of 3 elements as : name , address , phone number
def UpdateShopInfo(username,info):
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
        executer.execute('UPDATE users SET FullName = "{0}" , Address = "{1}", PhoneNumber = "{2}",Zip_Code = "{3}" WHERE UserName = "{4}"'.format(info[0],info[1],info[2],info[3],username))
        connection.commit()
        print("info updated!")
        return True
    except mysql.connector.Error as err:
        logger.error(f"Failed to connect to MySQL: {err}")
        return False
def GetInfo(username):
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
        executer.execute('Select FullName, Address, PhoneNumber,Zip_Code FROM users WHERE UserName = "{}"'.format(username))
        result=executer.fetchone()
        print(result)
        return result
        
    except mysql.connector.Error as err:
        logger.error(f"Failed to connect to MySQL: {err}")
if __name__=="__main__":
    main()