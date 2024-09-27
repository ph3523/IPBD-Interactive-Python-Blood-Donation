import json
from colorama import init, Fore, Style
from messages import clear_screen

def load_quiz():
    with open('./data/quiz.json', 'r', encoding='utf-8') as file:
        return json.load(file)

def display_quiz():
    clear_screen()
    quiz_data = load_quiz()

    print(Fore.RED + "=" * 50)
    print(Fore.RED + "          Quiz sobre Doação de Sangue")
    print(Fore.RED + "=" * 50)

    score = 0
    perguntas = quiz_data['quiz']['perguntas']
    for pergunta in perguntas:
        while True:
            clear_screen()
            print(Fore.RED + "=" * 50)
            print(Fore.RED + "          Quiz sobre Doação de Sangue")
            print(Fore.RED + "=" * 50)
            print(Style.BRIGHT + f"\n{pergunta['pergunta']}")
            for index, opcao in enumerate(pergunta['opcoes']):
                print(Style.BRIGHT + f"{index + 1} - {opcao}")
            try:
                answer = int(input("\nDigite o número da resposta correta: "))
                if pergunta['opcoes'][answer - 1] == pergunta['resposta_correta']:
                    score += 1
                break
            except (ValueError, IndexError):
                print(Fore.RED + "Por favor, digite um número válido.")
                input("Pressione Enter para tentar novamente...")

    print(Fore.GREEN + f"\nVocê acertou {score} de {len(perguntas)} questões!")
    input("\nPressione Enter para voltar ao Menu Principal...")