from util.Message import Message
from RegisterMenu import dataMenu
message = Message.showMessage
   
def menuPrincipal():
    print('\nMENU PRINCIPAL')
    print('C = Cadastros')
    print('R = Relatórios')
    print('S = Sair\n')
    choice = input('Digite a sua opção = ')

    if choice == 'C':
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