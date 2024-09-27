import json
from colorama import init, Fore, Style
from messages import clear_screen

def load_procedures():
    with open('./data/procedures.json', 'r', encoding='utf-8') as file:
        return json.load(file)

def display_procedures():
    clear_screen()
    procedures = load_procedures()

    print(Fore.RED + "=" * 50)
    print(Fore.RED + "          Procedimentos de Doação de Sangue")
    print(Fore.RED + "=" * 50)

    print(Style.BRIGHT+ "\nPreparação:")
    preparation = procedures['procedimentos_de_doacao']['preparacao']
    for key, value in preparation.items():
        if isinstance(value, dict):
            print(Style.BRIGHT + f"\t{key.replace('_',' ').capitalize()}:")
            for sub_key, sub_value in value.items():
                print(Style.BRIGHT + Fore.LIGHTGREEN_EX + f" \t\t{sub_key.replace('_',' ').capitalize()}: {sub_value}")
        else:
            print(Style.BRIGHT + Fore.LIGHTCYAN_EX + f"\t{key.replace('_',' ').capitalize()}: {value}")

    print(Style.BRIGHT + "\nColeta:")
    collection = procedures['procedimentos_de_doacao']['coleta']
    for key, value in collection.items():
        print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + f"\t{key.replace('_',' ').capitalize()}: {value}")

    print(Style.BRIGHT + "\nCuidados Pós-Doação:")
    post_donation = procedures['procedimentos_de_doacao']['cuidados_pos_doacao']
    for key, value in post_donation.items():
        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + f"\t{key.replace('_',' ').capitalize()}: {value}")

    input("\nPressione Enter para voltar ao Menu Principal...")