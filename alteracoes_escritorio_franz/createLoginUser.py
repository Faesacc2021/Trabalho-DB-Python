import DataBaseConnection as db
from responseModel import ResponseModel
class CreateLoginUser:
  def createLogin(LoginUser):
    if db.connection.is_connected():
        cursor = db.connection.cursor()
        
        sql = "INSERT INTO loginuser (email, descriptionAccess) VALUES (%s, %s)"
        data = (LoginUser.email, LoginUser.descriptionAccess)
        try:
            cursor.execute(sql, data)
            db.connection.commit()
            cursor.close()
            db.connection.close()
            responseModel = ResponseModel(True, "Login criado com sucesso")
            return responseModel
        except db.Error as error:
            return ResponseModel(False, error)
    else:
        return ResponseModel(False, "Não foi possível criar uma conexão com o Banco de dados")
            