from colorama import init, Fore, Style
from messages import clear_screen
import time

def elegebility_check():

    clear_screen()
    while True:
        init(autoreset=True)
        print(Fore.RED + "=" * 70)
        print(Fore.RED + "          Verificação de Elegibilidade para Doação de Sangue")
        print(Fore.RED + "=" * 70)
        print(Style.BRIGHT + "\nPara doar sangue, você precisa atender aos seguintes requisitos:")
        print(Style.BRIGHT + "1 - Ter entre 16 e 69 anos de idade")
        print(Style.BRIGHT + "2 - Pesar no mínimo 50 kg")
        print(Style.BRIGHT + "3 - Estar descansado (ter dormido pelo menos 6 horas nas últimas 24 horas)")
        print(Style.BRIGHT + "4 - Estar alimentado (evitar alimentação gordurosa nas 4 horas que antecedem a doação)")
        print(Style.BRIGHT + "5 - Apresentar documento original com foto recente, que permita a identificação do candidato, emitido por órgão oficial")


        try:
            age = int(input("Digite sua idade: "))
            weight = int(input("Digite seu peso: "))

            if age < 16:
                print(Fore.RED + "Você não tem idade suficiente para doar sangue.")
                time.sleep(7)
                break
            elif age >= 16 and age < 18 and weight >= 50:
                print(Fore.LIGHTGREEN_EX + "Você tem idade suficiente, mas precisa de um autorização formal de um responsável.")
                print(Style.BRIGHT + "Acesse o site https://www.prosangue.sp.gov.br/artigos/requisitos_basicos_para_doacao.html para mais informações.")
                time.sleep(7)
                break
            elif age >= 18 and age <= 69 and weight >= 50:
                print(Fore.LIGHTGREEN_EX + "Você está apto para doar sangue.")
                print(Fore.LIGHTBLUE_EX + "Procure no Menu Principal a opção de locais de doação proximo a você.")
                time.sleep(7)
                break    
            else:
                print(Fore.RED + "Você não está apto para doar sangue.")
                print(Style.BRIGHT + "Acesse o site https://www.prosangue.sp.gov.br/artigos/requisitos_basicos_para_doacao.html para mais informações.")
                time.sleep(7)
                break

        except ValueError:
            print(Fore.RED + "Valores inválidos. Tente novamente.")
            time.sleep(3)

        