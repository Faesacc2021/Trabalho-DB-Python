import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='dbcompras',
                                         user='root',
                                         password='fb36271809')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        
        cursor = connection.cursor()

        sql = "INSERT INTO fornecedores (cnpj, razaoSocial, contato) VALUES (%s, %s, %s)"
        data = (
        '01006785000199',
        'tem de tudo material de construcao',
        'franz blauth ximenes'
        )

        cursor.execute(sql, data)
        connection.commit()

        userid = cursor.lastrowid

        cursor.close()
        connection.close()

        print("Foi cadastrado o novo usuário de ID:", userid)

