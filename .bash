blood_donation_program/
│
├── app/
│   ├── __init__.py                  # Torna 'app' um pacote Python
│   ├── main.py                      # Ponto de entrada do programa
│   ├── eligibility.py               # Lógica de verificação de elegibilidade (idade, peso, etc.)
│   ├── locations.py                 # Função para listar locais e horários de doação
│   ├── procedures.py                # Procedimentos de doação de sangue (descrição passo a passo)
│   ├── tips.py                      # Dicas úteis para doadores
│   ├── quiz.py                      # Seção de quiz com perguntas sobre doação
│   ├── utils.py                     # Funções auxiliares (e.g., validação de entradas)
│   └── messages.py                  # Mensagens de agradecimento e encerramento
│
├── data/
│   ├── locations.json               # Dados dos locais de doação (nome, endereço, horário, etc.)
│   └── quiz_questions.json          # Perguntas e respostas para o quiz
│
├── config/
│   └── settings.py                  # Configurações gerais, se necessário (e.g., limites de idade/peso)
│
├── tests/
│   ├── test_eligibility.py           # Testes para verificação de elegibilidade
│   ├── test_locations.py            # Testes para locais de doação
│   ├── test_procedures.py           # Testes para procedimentos
│   ├── test_tips.py                 # Testes para as dicas de doação
│   ├── test_quiz.py                 # Testes para a lógica do quiz
│   └── test_utils.py                # Testes para funções auxiliares
│
├── docs/
│   └── README.md                    # Documentação sobre o projeto
│
├── .gitignore                       # Arquivos/pastas a serem ignorados pelo Git
├── requirements.txt                 # Lista de dependências
└── README.md                        # Descrição do projeto

Descrição dos Arquivos:
app/main.py: Contém o código que inicia o programa, apresentando a interface inicial.
app/eligibility.py: Lida com a verificação de elegibilidade, considerando a idade e o peso do usuário.
app/locations.py: Fornece a lógica para listar os locais e horários de doação de sangue.
app/procedures.py: Descreve os procedimentos de doação, com detalhes sobre preparação, coleta e cuidados pós-doação.
app/tips.py: Exibe dicas úteis para doadores.
app/quiz.py: Contém a lógica para criar e avaliar um quiz sobre doação de sangue.
app/utils.py: Funções auxiliares, como validações de entradas do usuário.
app/messages.py: Exibe mensagens de agradecimento e de encerramento ao final do programa.
data/locations.json: Armazena os dados dos locais de doação (nome, endereço, horário).
data/quiz_questions.json: Contém as perguntas e respostas do quiz.