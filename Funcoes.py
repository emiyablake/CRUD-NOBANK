#Função Cadastrar Dados
def cadastrar_dados():

    #Tentativa criar arquivo e salvar dados no mesmo
    try:

        #Abrir arquivo em modo apendice
        with open('Dados_Clientes', 'a') as arquivo:

            cpf = int(input("CPF(apenas números): "))
            nome_cliente = input("Nome: ")
            endereco = input("Endereço: ")
            bairro = input("Bairro: ")
            cidade = input("Cidade: ")

            #Formatar dados
            cliente = f"{cpf},{nome_cliente},{endereco},{bairro},{cidade},\n"

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
        with open ('Dados_Clientes','r') as arquivo:

            #Ler os dados do arquivo e armazenar em lista
            linhas = arquivo.readlines()

            #Verificar se há dados no arqiuvo
            if not linhas:
                print("Nenhum dado de cliente cadastrado")

            #Exibir um cabeçalho com os dados
            else:
                print("Dados cadastrados: ")
                
                #repetir sobre cada linha do arquivo
                for linha in linhas:
                    #Dividir linhas por vírgulas e remover os espaços em branco
                    dados = linha.strip().split(',')

                    #Extrair os valores de cada dado
                    cpf = dados[1]
                    nome_cliente = dados[2]
                    endereco = dados [3]
                    bairro = dados [4]
                    cidade = dados [5]

                    #Exibir os dados dos clientes na tela
                    print("CPF: ", cpf)
                    print("Nome: ", nome_cliente)
                    print("Endereço: ", endereco)
                    print("Bairro: ", bairro)
                    print("Cidade: ", cidade)
                    print("-"*30)
    except FileNotFoundError:
        print("Arquivo de dados não encontrado")
    except Exception as e:
        print("Ocorreu um erros ao listar os dados:", str(e))




#Função Backup
def backup_dados():

    #Tentativa de criar um backup dos dados
    try:

        #Abrir dados clientes 
        with open ('Dados_Clientes','r') as origem:
            dados = origem.read()

            #Criar uma copia dos dados clientes
            with open ('Dados_Clientes_Backup','w') as destino:
                destino.write(dados)

        #Alerta de sucesso
        print("Backup realizado com sucesso!")
    
    #Exceção de erro arquivo não encontrado
    except FileNotFoundError:
        print("Arquivo de origem não encontrado")
     #Exceção de erro backup não realizado
    except Exception as e: 
        print("Ocorreu um erro ao realizar o backup de dados: ", str(e))


"""
#Função Atualizar dados
def atualizar_dados():

    #Tentativa de atualizar dados
    try:

        #Abrir arquivo de dados
        with open ('Dados_Clientes','r') """