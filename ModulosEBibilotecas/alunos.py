alunos = {}

def AdicionarAluno():
    """Solicita ao usuário que digite o nome e o número de matrícula de um aluno e adicione-o ao dicionário de alunos."""
    matricula = input("Digite o número de matrícula do aluno: ")
    nome = input("Digite o nome do aluno: ")
    if matricula in alunos:
        print("Aluno com esta matrícula já existe.")
    else:
        alunos[matricula] = nome
        print(f"Aluno {nome} com matrícula {matricula} foi adicionado.")

def RemoverAluno():
    """Solicita ao usuário que digite o número de matrícula de um aluno e remove-o do dicionário de alunos."""
    matricula = input("Digite o número de matrícula do aluno a ser removido: ")
    if matricula in alunos:
        del alunos[matricula]
        print(f"Aluno com matrícula {matricula} foi removido.")
    else:
        print("Não existe aluno com esta matrícula.")

def AtualizarAluno():
    """Solicita ao usuário que digite o número de matrícula de um aluno e atualize o nome desse aluno no dicionário."""
    matricula = input("Digite o número de matrícula do aluno a ser atualizado: ")
    if matricula in alunos:
        nome = input("Digite o novo nome do aluno: ")
        alunos[matricula] = nome
        print(f"Nome do aluno com matrícula {matricula} foi atualizado para {nome}.")
    else:
        print("Não existe aluno com esta matrícula.")

def VerAlunos():
    """Lista todos os alunos cadastrados, exibindo o número de matrícula e o nome de cada um."""
    if alunos:
        print("Lista de alunos cadastrados:")
        for matricula, nome in alunos.items():
            print(f"Matrícula: {matricula}, Nome: {nome}")
    else:
        print("Nenhum aluno cadastrado.")
