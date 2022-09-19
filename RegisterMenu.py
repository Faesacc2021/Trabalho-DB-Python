from CreateEmployee import CreateEmployee
# from create import Create
# from update import Update
# from delete import Delete
    
def dataMenu():
    print('Opções Disponíveis: C = Cadastros, R = Relatórios, S = Sair')
    choice = input('Digite a sua opção = ')

    if choice == 'C':
        createObj = CreateEmployee()
        createObj.createData()
    elif choice == 'R':
        readObj =  Read()
        readObj.func_ReadData()
    elif choice == 'S':
        quit()
    else:
        print('Opção inválida, Escolha novamente')
        dataMenu()

dataMenu()