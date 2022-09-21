def dataMenu():
    print('\nEscolha uma Opção: C = Cadastros, R = Relatórios, S = Sair')
    choice = input('Digite a sua opção = ')
    if choice == 'C':
       from CreateEmployee import CreateEmployee
       CreateEmployee.createData()
    elif choice == 'R':
        ""
    elif choice == 'S':
        quit()
    else:
        print('Opção inválida, Escolha novamente')
        dataMenu()    
    dataMenu()
dataMenu()    
