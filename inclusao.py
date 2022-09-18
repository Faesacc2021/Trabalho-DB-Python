import mysql.connector
import datetime

connection = mysql.connector.connect(host='localhost',
                                         database='dbcompras',
                                         user='root',
                                         password='fb36271809')

cursor = connection.cursor()

sql = "INSERT INTO fornecedores (cnpj, razaoSocial, contato, email, telefone, dataInclusao) VALUES (%s, %s, %s, %s, %s, %s)"
data = (
  '01002345777199',
  'Tem de tudo materiais eletricos',  
  '123456',
  'primeirousuario@teste.com.br',
  '27999990909',
  datetime.datetime.today()
)

cursor.execute(sql, data)
connection.commit()

userid = cursor.lastrowid

cursor.close()
connection.close()

print("Foi cadastrado o novo usuário de ID:", userid)