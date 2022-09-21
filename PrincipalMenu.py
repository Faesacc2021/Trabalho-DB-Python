from util.Message import Message
message = Message.showMessage
   
def menuPrincipal():
    print('\nMENU PRINCIPAL')
    print('C = Cadastros')
    print('R = Relatórios')
    print('S = Sair\n')
    choice = input('Digite a sua opção = ')

    if choice == 'C':
        from RegisterMenu import dataMenu
        dataMenu()
    elif choice == 'R':
        # To do
        "implantar chada menu de relatorios"
    elif choice == 'S':
        quit()
    else:
        message('Opção inválida, Escolha novamente', '')
    menuPrincipal()            
menuPrincipal()