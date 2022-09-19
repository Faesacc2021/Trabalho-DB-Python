from RegisterMenu import dataMenu
# from update import Update
# from delete import Delete
    
def main():
    print('\nMENU PRINCIPAL')
    print('C = Cadastros')
    print('R = Relatórios')
    print('S = Sair\n')
    choice = input('Digite a sua opção = ')

    if choice == 'C':
        dataMenu()
    elif choice == 'R':
        readObj =  Read()
        readObj.func_ReadData()
    elif choice == 'S':
        quit()
    else:
        print('Opção inválida, Escolha novamente')
        main()

main()