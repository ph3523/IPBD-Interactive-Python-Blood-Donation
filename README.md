# IPBD-Interactive-Python-Blood-Donation

## Descrição
O **IPBD-Interactive-Python-Blood-Donation** é um programa interativo desenvolvido para incentivar e educar sobre a importância da doação de sangue. Este projeto foi criado para o curso de Lógica de Programação do TIC 20 e oferece diversas funcionalidades, incluindo verificação de elegibilidade, localização de centros de doação, informações sobre procedimentos de doação, dicas úteis e um quiz interativo.

## Estrutura do Projeto
A estrutura do projeto é organizada da seguinte forma:
````bash
IPBD-Interactive-Python-Blood-Donation/
│
├── app/
│   ├── __pycache__/                 # Arquivos de cache do Python
│   ├── eligibility.py               # Lógica de verificação de elegibilidade (idade, peso, etc.)
│   ├── locations.py                 # Função para listar locais e horários de doação
│   ├── main.py                      # Ponto de entrada do programa
│   ├── messages.py                  # Mensagens de agradecimento e encerramento
│   ├── procedures.py                # Procedimentos de doação de sangue (descrição passo a passo)
│   ├── quiz.py                      # Seção de quiz com perguntas sobre doação
│   ├── tips.py                      # Dicas úteis para doadores
│   └── utils.py                     # Funções auxiliares (e.g., validação de entradas)
│
├── data/
│   ├── locations.json               # Dados dos locais de doação (nome, endereço, horário, etc.)
│   ├── procedures.json              # Dados sobre os procedimentos de doação
│   ├── quiz.json                    # Perguntas e respostas para o quiz
│   └── tips.json                    # Database de dicas para doadores
│
├── docs/
│   └── README.md                    # Documentação sobre o projeto
│
├── .gitignore                       # Arquivos/pastas a serem ignorados pelo Git
├── LICENSE                          # Licença do projeto
├── README.md                        # Descrição do projeto
└── requirements.txt                 # Lista de dependências
````
Funcionalidades
1. Verificação de Elegibilidade
Arquivo: ``app/eligibility.py``

Verifica se o usuário está apto para doar sangue com base em critérios como idade e peso.

2. Localização de Centros de Doação
Arquivo: ``app/locations.py``

Lista os locais e horários de doação de sangue com base nos dados fornecidos no arquivo ``data/locations.json``.

3. Procedimentos de Doação
Arquivo: ``app/procedures.py``

Descreve os procedimentos de doação de sangue, incluindo preparação, coleta e cuidados pós-doação.

4. Dicas para Doadores
Arquivo: ``app/tips.py``

Exibe dicas úteis para doadores de sangue, como hidratação, alimentação adequada e cuidados após a doação.

5. Quiz Interativo
Arquivo: ``app/quiz.py``

Um quiz interativo com perguntas sobre doação de sangue, baseado nos dados fornecidos no arquivo data/quiz.json.

6. Mensagens de Agradecimento e Encerramento
Arquivo: ``app/messages.py``

Exibe mensagens de boas-vindas, agradecimento e encerramento ao usuário.

## Instalação

Para instalar as dependências necessárias, execute o seguinte comando:
```bash
pip install -r requirements.txt
```
Como Executar
Para iniciar o programa, execute o arquivo main.py:
```bash
python app/main.py
```

## Licença
Este projeto está licenciado sob a Licença GNU General Public License. Veja o arquivo LICENSE para mais detalhes.

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

<table>
  <tr>
    <td align="center"><a href="https://github.com/ph3523"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/80484091?v=4" width="100px;" alt=""/><br /><sub><b>Pedro Barroso</b></sub></a><br /><a href="mailto:ph.barroso3523@gmail.com" title="Email">✉️</a></td>
  </tr>
 
</table>