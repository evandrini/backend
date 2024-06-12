from alunos import AdicionarAluno, RemoverAluno, AtualizarAluno, VerAlunos

def menu():
    """Exibe o menu de opções para o usuário e executa as funções conforme a escolha."""
    while True:
        print("\nMenu de Opções:")
        print("1. Adicionar Aluno")
        print("2. Remover Aluno")
        print("3. Atualizar Aluno")
        print("4. Ver Alunos")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            AdicionarAluno()
        elif opcao == '2':
            RemoverAluno()
        elif opcao == '3':
            AtualizarAluno()
        elif opcao == '4':
            VerAlunos()
        elif opcao == '5':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")
