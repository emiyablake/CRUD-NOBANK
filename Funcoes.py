#Função Cadastrar Dados
def cadastrar_dados():

    #Tentativa criar arquivo e salvar dados no mesmo
    try:

        #Abrir arquivo em modo apendice
        with open('dados_clientes.txt', 'a') as arquivo:

            #declarando variaveis
            nome_cliente = input("Nome: ")
            cpf = input("CPF: ")
            dataNasc = input("Data de Nascimento: ")
            endereco = input("Endereço: ")
            cep = input("CEP: ")
            cidade = input("Cidade: ")
            estado = input("estado: ")
            telefone = input("telefone: ")
            obs = input("Observações: ")
            print("-"*36)

            #Formatar dados
            cliente = f"{nome_cliente},{cpf},{dataNasc},{endereco}, {cep}, {cidade}, {estado}, {telefone}, {obs}, \n"

            #Escrever no arquivo
            arquivo.write(cliente)

            #Exibir mensagem de conclusão
            print("Dados do cliente cadastrados com sucesso!")

    except ValueError: 
        #Captura erros caso for inserido valores fora do formato esperado
        print("Valor inválido")
    
    except Exception as e:
        #Captura erros durante o cadastro dos dados
        print("Ocorreu um erro ao cadastrar os dados:", str(e))




#Função listar dados
def listar_dados ():

    #Tentativa ler e listar dados
    try:

        #Abrir Dados_Clientes
        with open ('dados_clientes.txt','r') as arquivo:
            linhas = arquivo.readlines()

            #Verificar se há dados no arqiuvo
            if not linhas:
                print("Nenhum dado de cliente cadastrado")

            #Exibir um cabeçalho com os dados
            else:
                print("-"*30)
                print("Dados cadastrados: ")
                
                #repetir sobre cada linha do arquivo
                for linha in linhas:
                    #Dividir linhas por vírgulas e remover os espaços em branco
                    dados = linha.strip().split(',')

                    #Extrair os valores de cada dado
                    nome_cliente = dados[0]
                    cpf = dados[1]
                    dataNasc = dados [2]
                    endereco = dados [3]
                    cep = dados [4]
                    cidade = dados [5]
                    estado = dados [6]
                    telefone = dados [7]
                    obs = dados [8]

                    #Exibir os dados dos clientes na tela
                    print("Nome: ", nome_cliente)
                    print("CPF: ", cpf)
                    print("Data de Nascimento: ", dataNasc)
                    print("Endereço: ", endereco)
                    print("CEP: ", cep)
                    print("Cidade: ", cidade)
                    print("Estado: ", estado)
                    print("Telefone: ", telefone)
                    print("obs: ", obs)
                    print("-"*30)

    except FileNotFoundError:
        print("Arquivo de dados não encontrado")
    except Exception as e:
        print("Ocorreu um erros ao listar os dados:", str(e))




#Função Atualizar dados
def atualizar_dados():

    cpf = input("Digite o CPF do cliente a ser atualizado: ")

    encontrado = False

    #Lista para armazenar os dados atualizados
    dados_atualizados = []

    #Tentativa de atualizar dados
    try:

        #Abrir arquivo de dados
        with open ('dados_clientes.txt','r') as arquivo:

            #ler as linhas do arquivo
            linhas =  arquivo.readlines()
            
            #Repetir sobre cada linha do arquivo
            for linha in linhas:
                dados = linha.strip().split(',')
                cpf_cliente = dados[1]

                #Verficiar CPF
                if cpf == cpf_cliente:
                    encontrado = True
                    # Mostra na tela os dados do cliente
                    print("-"*30)
                    print("Dados atuais do cliente:")
                    print("Nome:", dados[0])
                    print("CPF:", dados[1])
                    print("Data Nascimento:", dados[2])
                    print("Endereço:", dados[3])
                    print("CEP: ",dados [4])
                    print("Cidade:", dados[5])
                    print("Estado: ", dados [6])
                    print("Telefone: ", dados [7])
                    print("Observação: ", dados [8])
                    print()

                    #Obter novos dados
                    novos_dados = {}
                    novos_dados['nome_cliente'] = input("Digite o novo nome do cliente: ")
                    novos_dados['endereco'] = input ("Digite o novo endereço do cliente: ")
                    novos_dados['cep'] = input("Digite o novo CEP do cliente: ")
                    novos_dados['cidade'] = input("Digite a nova cidade do cliente: ")
                    novos_dados['estado'] = input("Digite o novo estado do cliente: ")
                    novos_dados['telefone'] = input("Digite o novo telefone do cliente: ")
                    novos_dados['obs'] = input("Digite uma nova observação sobre o cliente: ")
                    print()

                    # Atualizar os dados do cliente
                    dados[0] = novos_dados['nome_cliente']
                    dados[3] = novos_dados['endereco']
                    dados[4] = novos_dados['cep']
                    dados[5] = novos_dados['cidade']
                    dados[6] = novos_dados['estado']
                    dados[7] = novos_dados['telefone']
                    dados[8] = novos_dados['obs']
                    
                linha_atualizada = ','.join(dados) + '\n'
                dados_atualizados.append(linha_atualizada)

        if encontrado:
            with open('dados_clientes.txt', 'w') as arquivo:
                #Escrever dados atualizados de volta no arquivo
                arquivo.writelines(dados_atualizados)
                print("Dados atualizados com sucesso!")
        else:
            print("Clientes não encontrado")
    
    except FileNotFoundError:
        print("Arquivo de dados não encontrado")
    except Exception as e:
        print("Ocorreu um erro ao atualizar os dados: ", str(e))



#Função Deletar Dado
def deletar_dado():

    cpf = input("Digite o CPF do cliente a ser deletado: ")

    try:
        with open ('dados_clientes.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
        
        with open ('dados_clientes.txt', 'w') as arquivo:
            encontrado = False

            for linha in linhas:
                dados = linha.strip().split(',')
                cpf_cliente = dados [1]

                if cpf == cpf_cliente:
                    encontrado = True 
                
                else: 
                    arquivo.write(linha)
            
            if encontrado:
                print("Cliente excluido com sucesso!")
            
            else:
                print("Cliente não encontrado. Nenhum dado foi excluido.")

    
    except FileNotFoundError:
        print("Arquivo de dados não encontrado")
    
    except Exception as e:
        print("Ocorreu um erro ao excluir os dados: ", str(e))




#Função Backup
def backup_dados():

    #Tentativa de criar um backup dos dados
    try:

        #Abrir dados clientes 
        with open ('dados_clientes.txt','r') as origem:
            dados = origem.read()

            #Criar uma copia dos dados clientes
            with open ('dados_clientes_backup.txt','w') as destino:
                destino.write(dados)

        #Alerta de sucesso
        print("Backup realizado com sucesso!")
    
    #Exceção de erro arquivo não encontrado
    except FileNotFoundError:
        print("Arquivo de origem não encontrado")
     #Exceção de erro backup não realizado
    except Exception as e: 
        print("Ocorreu um erro ao realizar o backup de dados: ", str(e))



#Exibir MENU
def exibir_menu():
    print("--------------- MENU ---------------")
    print("1. Cadastrar novo cliente")
    print("2. Listar dados dos clientes")
    print("3. Atualizar dados de um cliente")
    print("4. Deletar dados de um cliente")
    print("5. Realizar backup dos dados")
    print("0. Sair do sistema")
    print("-"*36)


#Main para rodar o menu
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