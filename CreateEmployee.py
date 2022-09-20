import DataBaseConnection as db
import model.Employee

employee = model.Employee.Employee(0,"",0.0)

class CreateEmployee:
  def createData(self):

    if db.connection.is_connected():
      cursor = db.connection.cursor()
      employee.cpf = input('Digite o CPF = ')
      employee.name = input('Digite o nome = ')
      employee.salary = input('Informe o salário = ')

      if checkEmptyData():
         return 
        
      sql = "INSERT INTO employee (cpf, name, salary) VALUES (%s, %s, %s)"
      data = (employee.cpf, employee.name, employee.salary)
      try:
        cursor.execute(sql, data)
        db.connection.commit()
        cursor.close()
        db.connection.close()
        print("Foi cadastrado o novo usuário")
      except db.Error as e:
        print("Erro ao tentar salvar o registro", e)
        return
    else:
      print("Não conexão com o Banco de dados")
      return
       
def checkEmptyData():
    isEmpty = True
    if employee.cpf == 0 or employee.name == '' or employee.salary == 0.0:
      print("É obrigatório o preenchimento de todos os campos")      
    else:
      isEmpty = False
    return isEmpty       