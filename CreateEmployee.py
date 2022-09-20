import DataBaseConnection as db
import model.Employee as Employee
from util.Message import Message as message 
 
cpf = str
name = str
salary = float

class CreateEmployee:
  def createData():

    if db.connection.is_connected():
      cursor = db.connection.cursor()
      
      inputDataEmplyee()
      
      if checkEmptyData():
         return 

      try:
        sql = "INSERT INTO employee (cpf, name, salary) VALUES (%s, %s, %s)"
        data = ("0123", "catatau", 1500)
        cursor.execute(sql, data)
        db.connection.commit()
        cursor.close()
        db.connection.close()
        message.showMessage("\nNovo funcionário cadastrado com sucesso!")
      except db.Error as e:
        message.showMessage("\nErro ao tentar salvar o registro", e)
    else:
      message.showMessage.showMessageint("Não há conexão com o Banco de dados")
    return

def inputDataEmplyee():
    cpf = input('Digite o CPF = ')
    name = input('Digite o nome = ')
    salary = input('Informe o salário = ')
       
def checkEmptyData():
    isEmpty = True
    if cpf == 0 or name == '' or salary == 0.0:
      message.showMessage("É obrigatório o preenchimento de todos os campos")      
    else:
      isEmpty = False
    return isEmpty       