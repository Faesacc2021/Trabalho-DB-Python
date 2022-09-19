import DataBaseConnection as db

name = str
cpf = int
salary = float

class CreateEmployee:
  def createData(self):

    if db.connection.is_connected():
      cursor = db.connection.cursor()
      cpf = input('Digite o CPF = ')
      name = input('Digite o nome = ')
      salary = input('Informe o salário = ')

      if cpf == 0 or name == '' or salary == 0.0:
        print("É obrigatório o preenchimento de todos os campos")      
        return 
        
      sql = "INSERT INTO employee (cpf, name, salary) VALUES (%s, %s, %f)"
      data = (cpf, name, salary)
    
      cursor.execute(sql, data)
      db.connection.commit()
      cursor.close()
      db.connection.close()
      print("Foi cadastrado o novo usuário")
    else:
      print("Não conexão com o Banco de dados")
      
  def checkEmptyData(isEmpty):
      isEmpty = True
      

      
      return True       