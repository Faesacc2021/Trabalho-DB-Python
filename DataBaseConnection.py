import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                                database='beautysalon',
                                                user='root',
                                                password='BancoDados2022')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Conectado no Servidor MySQL versão ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Você está conectado ao Banco de Dados", record)

except Error as e:
    print("Erro ao conectar o Banco de Dados MySQL. Sistema será encerrado", e)
    print("Sistema será encerrado!!!")
    quit()