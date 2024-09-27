import json
from colorama import init, Fore, Style
from messages import clear_screen

def load_tips():
    with open('./data/tips.json', 'r', encoding='utf-8') as file:
        return json.load(file)

def display_tips():
    clear_screen()
    tips = load_tips()

    print(Fore.RED + "=" * 50)
    print(Fore.RED + "          Dicas para Doadores de Sangue")
    print(Fore.RED + "=" * 50)

    dicas_para_doadores = tips['dicas_para_doadores']
    for key, value in dicas_para_doadores.items():
        print(Style.BRIGHT + Fore.LIGHTGREEN_EX + f"{key.replace('_', ' ').capitalize()}: {value}")

    input("\nPressione Enter para voltar ao Menu Principal...")