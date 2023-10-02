'''
Voltando ao cenário que trata de um sistema de registro de notas de alunos em uma pequenainstituição de ensino, propor situações em que strings fornecidas como entrada para o aplicativoprecisam de tratamento para que sejam corretamente armazenadas em arquivo. Realizartambém requisitos de tratamentos de exceções a serem implementadas. Os alunos devemincrementar o sistema desenvolvido na aula anterior para incluir esta funcionalidade, conformerequisitos fornecidos pelo docente.
Exemplos de requisitos são:
(A) Manipulações de Strings:
(i) tratar entradas vazias, 
(ii) tratar nomes de alunos que contém números e 
(iii) tratarnúmero de matrículas com caracteres.
(B) Tratamento de exceções:
(i) Tratar fechamento de arquivos que não foram abertos, (ii) tentar escrever em arquivoscom permissão para somente leitura,
(iii) tentar ler dados de arquivos inexistentes.
'''
def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    email = input("Digite o email do aluno: ")
    curso = input("Digite o curso do aluno: ")

    
    if not nome or not email or not curso:
        print("Erro: Nenhum campo pode estar vazio.")
        return

   
    if any(char.isdigit() for char in nome):
        print("Erro: O nome não pode conter números.")
        return

    
    try:
        with open("alunos.txt", "a") as arquivo:
            arquivo.write(f"Nome: {nome}\nEmail: {email}\nCurso: {curso}\n\n")
        print("Aluno cadastrado com sucesso.")
    except Exception as e:
        print(f"Erro ao escrever no arquivo: {str(e)}")

def listar_alunos():
    try:
        with open("alunos.txt", "r") as arquivo:
            conteudo = arquivo.read()
            if conteudo:
                print(conteudo)
            else:
                print("Nenhum aluno cadastrado.")
    except FileNotFoundError:
        print("Nenhum aluno cadastrado.")

def buscar_aluno_por_nome():
    nome = input("Digite o nome do aluno que deseja buscar: ")
    try:
        with open("alunos.txt", "r") as arquivo:
            conteudo = arquivo.read()
            if nome in conteudo:
                inicio = conteudo.index(nome)
                fim = conteudo.index("\n\n", inicio)
                aluno = conteudo[inicio:fim]
                print(aluno)
            else:
                print("Aluno não encontrado.")
    except FileNotFoundError:
        print("Nenhum aluno cadastrado.")

while True:
    print("\nMenu:")
    print("1. Cadastrar um novo aluno")
    print("2. Listar os alunos cadastrados")
    print("3. Buscar um aluno pelo nome")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_aluno()
    elif opcao == "2":
        listar_alunos()
    elif opcao == "3":
        buscar_aluno_por_nome()
    elif opcao == "4":
        break
    else:
        print("Opção inválida")
