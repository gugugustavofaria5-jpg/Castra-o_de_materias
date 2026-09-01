import json

# Inicialização das listas globais que armazenarão os dados durante a execução
lista_materias = []
lista_tarefas = []

def cadastrar_materia():
    # Loop infinito para permitir cadastro múltiplo até o usuário decidir sair
    while True:
        # Recebe entrada do usuário, remove espaços extras e normaliza
        materia = input("Digite a materia que você quer. Digite 'sair' para encerrar: ").strip()

        # Verifica condição de parada (sentinela)
        if materia.lower() == 'sair':
            print("\nCadastro encerrado.")
            break

        # Valida se a entrada não está vazia antes de adicionar
        if materia:
            lista_materias.append(materia)
            print(f"Matéria '{materia}' adicionada com sucesso!")
        else:
            print("Você não digitou nada, Tente novamente.")

def listar_materias():
    # Exibe cabeçalho e verifica se há dados para listar
    print("\n--- Matérias Cadastradas ---")
    if not lista_materias:
        print("Nenhuma matéria cadastrada.")
    else:
        # Itera sobre a lista e imprime cada item formatado
        for item in lista_materias:
            print(f"- {item}")

def cadastrar_tarefa():
    # Validação de pré-requisito: verifica se existe pelo menos uma matéria cadastrada
    if not lista_materias:
        print("\nAviso: Você ainda não cadastrou nenhuma matéria!")
        return

    print("\n--- Cadastração de tarefas ---")
    # Coleta os dados da tarefa via input do usuário
    nome_tarefa = input("Digite o nome da tarefa: ").strip()
    materia_tarefa = input("Digite a materia que você quer: ").strip()
    if materia_tarefa not in lista_materias:
        print("Erro: Essa matéria não existe! Cadastre ela primeiro.")

    prioridade = input("Digite a prioridade que você quer: ").strip()

    # Validação de campo obrigatório (nome da tarefa)
    if not nome_tarefa:
        print("Erro: O nome da tarefa não pode ser vazio.")
        return
    
    # Criação do dicionário (objeto) que representa a tarefa com status padrão
    dicionario_tarefa = {
        "nome": nome_tarefa,
        "materia": materia_tarefa,
        "prioridade": prioridade,
        "status": "Pendente"
    }

    # Adiciona o dicionário à lista global de tarefas
    lista_tarefas.append(dicionario_tarefa)
    print(f"Tarefa '{nome_tarefa}' cadastrada com sucesso!")

def listar_tarefas():
    # Exibe cabeçalho e verifica se há tarefas
    print("\n---Listas de tarefas---")

    if not lista_tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        # Itera sobre a lista de dicionários e acessa cada chave para exibição
        for tarefa in lista_tarefas:
            print(f"Tarefa: {tarefa['nome']}")
            print(f"Matéria: {tarefa['materia']}")
            print(f"Prioridade: {tarefa['prioridade']}")
            print(f"Status: {tarefa['status']}")
            print(f"-=-" * 30)

def concluir_tarefa():
    # Exibe cabeçalho e verifica se há tarefas disponíveis
    print("\n---Conclusão de tarefas---")

    if not lista_tarefas:
        print("Não existe nenhuma tarefa disponível.")
        return

    # Enumera a lista começando do 1 para facilitar a visualização do usuário
    for numero, tarefa in enumerate(lista_tarefas, 1):
        print(f"{numero} - {tarefa['nome']} (Status: {tarefa['status']})")

    # Bloco try/except para tratar erro de conversão de tipo (entrada não numérica)
    try:
        numero_tarefa = int(input("Digite o número da tarefa que deseja concluir: "))

        # Validação de intervalo: garante que o número esteja dentro da lista existente
        if 1 <= numero_tarefa <= len(lista_tarefas):
            # Ajuste de índice: subtrai 1 pois listas em Python começam em 0
            tarefa_escolhida = lista_tarefas[numero_tarefa - 1]

            # Atualiza o valor da chave 'status' no dicionário selecionado
            tarefa_escolhida['status'] = "concluída"
            print(f"Tarefa '{tarefa_escolhida['nome']}' marcada como concluínda!")
        else:
            print("Erro: número inválido. Tente novamente.")

    except ValueError:
        # Captura especificamente o erro de digitação (letras em vez de números)
        print("Erro: Por favor, digite apenas números ínteiros.")

def pesquisar_tarefa():
    # Exibe cabeçalho e verifica se há tarefas para buscar
    print("\n--- Pesquisar tarefa ---")

    if not lista_tarefas:
        print("Não existe nenhuma tarefa para se pesquisar.")
        return

    # Recebe termo de busca, normaliza para minúsculas para comparação case-insensitive
    termo = input("Digite qual tarefa ou matéria você quer buscar.").strip().lower()
    resultado = []

    # Busca linear: verifica se o termo está presente no nome ou na matéria
    for tarefa in lista_tarefas:
        if termo in tarefa['nome'].lower() or termo in tarefa['materia'].lower():
            resultado.append(tarefa)

    # Exibe resultados encontrados ou mensagem de ausência
    if not resultado:
        print("Nenhuma tarefa encontrada.")
    else:
        print(f"\n{len(resultado)} tarefa(s) encontrada(s):")
        for tarefa in resultado:
            print(f"Tarefa: {tarefa['nome']}")
            print(f"Matéria: {tarefa['materia']}")
            print(f"Prioridade: {tarefa['prioridade']}")
            print(f"Status: {tarefa['status']}")
            print("-=-" * 30)

def salvar_dados():
    # Agrupa as duas listas em um único dicionário para serialização
    dados = {
        "materias": lista_materias,
        "tarefas": lista_tarefas
    }

    # Abre arquivo em modo escrita ('w'), criando ou sobrescrevendo o arquivo JSON
    # encoding='utf-8' garante que acentos e caracteres especiais sejam salvos corretamente
    with open("dados.json", "w", encoding="utf-8") as arquivo:
        # json.dump converte o dicionário Python para texto JSON e grava no arquivo
        # ensure_ascii=False mantém os acentos legíveis no arquivo
        # indent=4 formata o JSON com recuos para facilitar a leitura humana
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)

def carregar_dados():
    # Declara uso das variáveis globais para que a função possa modificá-las
    global lista_materias, lista_tarefas
    try:
        # Abre arquivo em modo leitura ('r')
        with open("dados.json", "r", encoding="utf-8") as arquivo:
            # json.load lê o arquivo e converte o texto JSON de volta para dicionário Python
            dados = json.load(arquivo)
            
            # Atualiza as listas globais com os dados recuperados do arquivo
            lista_materias = dados["materias"]
            lista_tarefas = dados["tarefas"]
            print("Dados carregados com sucesso!")
            
    except FileNotFoundError:
        # Tratamento para quando o arquivo ainda não existe (primeira execução)
        print("Nenhum arquivo de dados encontrado. Iniciando listas vazias.")
        
    except json.JSONDecodeError:
        # Tratamento para quando o arquivo existe mas está corrompido ou inválido
        print("Erro ao ler o arquivo. Iniciando listas vazias.")

# Chama a função de carregamento antes de iniciar o menu para restaurar dados salvos
carregar_dados()

def mostrar_menu():
    # Loop principal do programa que mantém o menu ativo até a opção de sair
    while True:
        print("\n--- MEU ESTUDO PYTHON ---")
        print("1 - Cadastrar matéria")
        print("2 - Listar matérias")
        print("3 - Cadastrar tarefa")
        print("4 - Listar tarefa")
        print("5 - Concluir Tarefa")
        print("6 - Sair")

        opcao = input("Escolha quais das opçães: ").strip()

        # Estrutura condicional para despachar a execução para a função correta
        if opcao == "1":
            cadastrar_materia()
        elif opcao == "2":
            listar_materias()
        elif opcao == "3":
            cadastrar_tarefa()
        elif opcao == "4":
            listar_tarefas()
        elif opcao =="5":
            concluir_tarefa()
        elif opcao == "6":
            print("Programa encerrado. Bons estudos!")
            break # Interrompe o loop while e encerra o programa
        else:
            print("Erro: Opção inválida. Digite novamente.")

# Inicia a execução do menu principal
mostrar_menu()   
