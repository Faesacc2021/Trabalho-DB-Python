import DataBaseConnection as db
import model.Employee

employee = model.Employee.Employee(0,"",0.0)

class CreateEmployee:
  def createData():

    if db.connection.is_connected():
      cursor = db.connection.cursor()

      returnInput = inputValues()
      
      if checkEmptyData(returnInput):
         return 
        
      sql = "INSERT INTO employee (cpf, name, salary) VALUES (%s, %s, %s)"
      data = (returnInput.cpf, returnInput.name, returnInput.salary)
      try:
        cursor.execute(sql, data)
        db.connection.commit()
        cursor.close()
        db.connection.close()
        print("Foi cadastrado o novo usuário")
      except db.Error as e:
        print("Erro ao tentar salvar o registro", e)
    else:
      print("Não conexão com o Banco de dados")

def inputValues():
    employee.cpf = input('Digite o CPF = ')
    employee.name = input('Digite o nome = ')
    employee.salary = input('Informe o salário = ')
    return employee
       
def checkEmptyData(returnInput):
    isEmpty = True
    if returnInput.cpf == 0 or returnInput.name == '' or returnInput.salary == 0.0:
      print("É obrigatório o preenchimento de todos os campos")      
    else:
      isEmpty = False
    return isEmpty       