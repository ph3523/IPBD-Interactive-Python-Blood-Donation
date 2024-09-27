
#função que lista os locais de doação de sangue com base no json que está no arquivo locations.json

import json
from colorama import init, Fore, Style
from messages import clear_screen

def list_locations():
    clear_screen()
    with open('./data/locations.json', 'r', encoding='utf-8') as file:
        locations = json.load(file)

    print(Fore.RED + "=" * 60)
    print(Fore.RED + "          Locais de Doação de Sangue")
    print(Fore.RED + "=" * 60)
    print(Style.BRIGHT + "\nEncontre o local de doação mais próximo de você:")
    for location in locations:
        print(Style.BRIGHT + f"\nNome: {location['name']}")
        print(Style.BRIGHT + f"Endereço: {location['address']}")
        print(Style.BRIGHT + f"Telefone: {location['phone']}")
        print(Style.BRIGHT + f"Estado: {location['state']}")
        print(Style.BRIGHT + f"Horário de Funcionamento: {location['hours']}")
        print(Fore.RED + "-" * 60)

    input("\nPressione Enter para voltar ao Menu Principal...")