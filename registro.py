def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    email = input("Digite o email do aluno: ")
    curso = input("Digite o curso do aluno: ")

    aluno = {
        'Nome': nome,
        'Email': email,
        'Curso': curso
    }

    with open('alunos.txt', 'a') as arquivo:
        arquivo.write(f"{aluno['Nome']}, {aluno['Email']}, {aluno['Curso']}\n")

    print("Aluno cadastrado com sucesso!")

def listar_alunos():
    try:
        with open('alunos.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            if not linhas:
                print("Nenhum aluno cadastrado ainda.")
            else:
                print("Lista de alunos cadastrados:")
                for linha in linhas:
                    nome, email, curso = linha.strip().split(', ')
                    print(f"Nome: {nome}, Email: {email}, Curso: {curso}")
    except FileNotFoundError:
        print("Nenhum aluno cadastrado ainda.")

def buscar_aluno():
    nome_busca = input("Digite o nome do aluno que deseja buscar: ")
    encontrado = False

    try:
        with open('alunos.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                nome, email, curso = linha.strip().split(', ')
                if nome == nome_busca:
                    print(f"Nome: {nome}, Email: {email}, Curso: {curso}")
                    encontrado = True
                    break

        if not encontrado:
            print(f"Aluno com o nome '{nome_busca}' não encontrado.")
    except FileNotFoundError:
        print("Nenhum aluno cadastrado ainda.")

while True:
    print("\nOpções:")
    print("1. Cadastrar um novo aluno")
    print("2. Listar os alunos cadastrados")
    print("3. Buscar um aluno pelo nome")
    print("4. Sair")
    
    opcao = input("Digite o número da opção desejada: ")
    
    if opcao == '1':
        cadastrar_aluno()
    elif opcao == '2':
        listar_alunos()
    elif opcao == '3':
        buscar_aluno()
    elif opcao == '4':
        break
    else:
        print("Opção inválida. Tente novamente.")
