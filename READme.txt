# Classificador de Emails com IA

## Descrição
Este projeto é uma aplicação web desenvolvida em **Python/Flask** que classifica emails em **Produtivo** ou **Improdutivo**, com base no conteúdo textual. O sistema aceita três tipos de entrada:

- Texto digitado diretamente na interface
- Arquivos `.txt`
- Arquivos `.pdf` com texto

O frontend é simples, responsivo e feito em HTML e CSS puros.

---

## Estrutura do projeto

projeto_email_ai/
│
├── app.py # Backend Flask
├── requirements.txt # Dependências do projeto
├── README.md # Este arquivo
├── templates/
│ └── index.html # Frontend
├── static/
│ └── style.css # Estilos CSS
└── exemplos/
├── exemplo1.txt # Arquivo de teste 1
├── exemplo2.pdf # Arquivo de teste 2


---

## Tecnologias utilizadas

- **Python 3**
- **Flask**: framework web
- **PyPDF2**: para leitura de PDFs
- **HTML5 e CSS3**: frontend

---

## Como executar localmente

1. **Clonar o repositório:**

```bash
git clone https://github.com/SEU_USUARIO/projeto_email_ai.git
cd projeto_email_ai

Criar e ativar o ambiente virtual:

Windows:

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

pip install -r requirements.txt

Rodar a aplicação:

python app.py

Acessar no navegador:

http://127.0.0.1:5000/

Observações:

PDFs com muitas formatações complexas podem apresentar problemas de extração de texto.

Arquivos de imagem (jpg, png) não são suportados neste projeto.

O algoritmo de classificação é simples, baseado em palavras-chave, e pode ser aprimorado futuramente.

Contato:

Pedro Henrique Carneiro Gomes da Silva

E-mail: pedrohcg.silva@gmail.com

LinkedIn: https://www.linkedin.com/in/pedro-henrique-gomes-a77a19179/

