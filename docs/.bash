IPBD-Interactive-Python-Blood-Donation/
│
├── app/
│   ├── eligibility.py               # Lógica de verificação de elegibilidade (idade, peso, etc.)
│   ├── locations.py                 # Função para listar locais e horários de doação
│   ├── main.py                      # Ponto de entrada do programa
│   ├── messages.py                  # Mensagens de agradecimento e encerramento
│   ├── procedures.py                # Procedimentos de doação de sangue (descrição passo a passo)
│   ├── quiz.py                      # Seção de quiz com perguntas sobre doação
│   ├── tips.py                      # Dicas úteis para doadores
│   └── utils.py                     # Funções de menu, validação de entradas, etc.
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
├── requirements.txt                 # Lista de dependências
└── README.md                        # Descrição do projeto

Descrição dos Arquivos:
app/eligibility.py: Lida com a verificação de elegibilidade, considerando a idade e o peso do usuário.
app/locations.py: Fornece a lógica para listar os locais e horários de doação de sangue.
app/main.py: Contém o código que inicia o programa, apresentando a interface inicial.
app/messages.py: Exibe mensagens de agradecimento e de encerramento ao final do programa.
app/procedures.py: Descreve os procedimentos de doação, com detalhes sobre preparação, coleta e cuidados pós-doação.
app/quiz.py: Contém a lógica para criar e avaliar um quiz sobre doação de sangue.
app/tips.py: Exibe dicas úteis para doadores.
app/utils.py: Funções auxiliares, como validações de entradas do usuário.
data/locations.json: Armazena os dados dos locais de doação (nome, endereço, horário).
data/procedures.json: Contém os dados sobre os procedimentos de doação.
data/quiz.json: Contém as perguntas e respostas do quiz.
data/tips.json: Contém as dicas para doadores.
docs/README.md: Documentação sobre o projeto.
.gitignore: Arquivos/pastas a serem ignorados pelo Git.
README.md: Descrição do projeto.
requirements.txt: Lista de dependências.