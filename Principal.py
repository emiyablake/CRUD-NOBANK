#CRUD NOBANK                Discente: Mara Júlia Ávila

from Funcoes import *

def exibir_menu():
    print("--------------- MENU ---------------")
    print("1. Cadastrar novo cliente")
    print("2. Listar dados dos clientes")
    print("3. Atualizar dados de um cliente")
    print("4. Deletar dados de um cliente")
    print("5. Realizar backup dos dados")
    print("0. Sair do sistema")
    print("-"*36)


def main():
    while True:
        exibir_menu()
        opcao = input("Digite o numero da opção desejada: ")
        print("-"*36)

        if opcao == "1":
            cadastrar_dados()
        elif opcao == "2":
            listar_dados()
        elif opcao == "3":
            atualizar_dados()
        elif opcao == "4":
            deletar_dado()
        elif opcao == "5":
            backup_dados()
        elif opcao == "0":
            print("Saindo do sistema...")
            break
                
        else: 
            print("Opção inválida.Por favor, escolha uma opção válida")
   

if __name__ == "__main__":
    main()