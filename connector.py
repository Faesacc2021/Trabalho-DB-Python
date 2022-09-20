import DataBaseConnection as db

if db.connection.is_connected():
        
    cursor = db.connection.cursor()

    sql = "INSERT INTO fornecedores (cnpj, razaoSocial, contato) VALUES (%s, %s, %s)"
    data = (
    '01006785333199',
    'tem de tudo material de construcao',
    'franz blauth ximenes'
    )

    cursor.execute(sql, data)
    db.connection.commit()

    userid = cursor.lastrowid

    cursor.close()
    db.connection.close()

    print("Foi cadastrado o novo usuário de ID:", userid)

