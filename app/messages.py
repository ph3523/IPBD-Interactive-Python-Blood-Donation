from colorama import init, Fore, Style
import time
import os

def clear_screen():
    """Limpa a tela (compatível com Windows e Unix)."""
    os.system('cls' if os.name == 'nt' else 'clear')

def welcome_message():
    init(autoreset=True)
    clear_screen()
    print(Fore.RED + "=" * 60)
    print(Fore.RED + "          Bem-vindo ao Programa de Doação de Sangue")
    print(Fore.RED + "=" * 60)
    print(Style.BRIGHT + "\nA doação de sangue é um ato de solidariedade que salva vidas.")
    print(Style.BRIGHT + "Neste programa, você poderá verificar se está apto para doar,")
    print(Style.BRIGHT + "encontrar locais de doação, aprender sobre os procedimentos")
    print(Style.BRIGHT + "de doação, e até fazer um quiz sobre o processo.")
    print(Fore.GREEN + "\nAgradecemos por estar aqui e considerar a doação de sangue!\n")
    time.sleep(3)
    input("Pressione Enter para continuar...")

def goodbye_message():
    print(Fore.LIGHTBLUE_EX + "\nObrigado por usar o Programa de Doação de Sangue!")
    print(Fore.LIGHTBLUE_EX + "Esperamos que você tenha aprendido muito sobre a doação de sangue.")
    print(Fore.LIGHTBLUE_EX + "Até a próxima!\n")