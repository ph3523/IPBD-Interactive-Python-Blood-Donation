from messages import clear_screen, goodbye_message
from colorama import init, Fore, Style
from elegilibility import elegebility_check
from procedures import display_procedures
from locations import list_locations
from tips import display_tips
import time


def menu():
    clear_screen()
    print(Fore.RED + "=" * 50)
    print(Fore.RED + "          Menu Principal - Doação de Sangue")
    print(Fore.RED + "=" * 50)
    print(Style.BRIGHT + "\nEscolha uma das opções abaixo:")
    print(Style.BRIGHT + "1 - Verificar se você está apto para doar sangue")
    print(Style.BRIGHT + "2 - Encontrar locais de doação de sangue")
    print(Style.BRIGHT + "3 - Aprender sobre o processo de doação de sangue")
    print(Style.BRIGHT + "4 - Visualizar dicas úteis sobre doação de sangue")
    print(Style.BRIGHT + "5 - Fazer um quiz sobre doação de sangue")
    print(Style.BRIGHT + "6 - Sair do programa")

    try:
        choice = input("\nDigite o número da opção desejada: ")
        return choice
    except KeyboardInterrupt:
        raise 

def handler_menu():
    while True:
        try:
            choice = menu()
            if choice == "1":
                # Chame a função para verificar se o usuário pode doar sangue
                elegebility_check()
            elif choice == "2":
                # Chame a função para encontrar locais de doação
                list_locations()
            elif choice == "3":
                # Chame a função para aprender sobre o processo de doação
                display_procedures()
            elif choice == "4":
                # Chame a função para vizualizar dicas uteis sobre doação de sangue
                display_tips()
            elif choice == "5":
                # Chame a função para fazer um quiz sobre doação de sangue
                pass
            elif choice == "6":
                goodbye_message()
                break
            else:
                print(Fore.RED + "Opção inválida. Tente novamente.")
                time.sleep(2)
        except KeyboardInterrupt:
            clear_screen()
            print(Fore.RED + "\n\nOperação interrompida pelo usuário. Saindo...")
            time.sleep(2)
            goodbye_message()
            break