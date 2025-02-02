# Sistema de Cadastro de Corretores

Este é um sistema de cadastro de corretores desenvolvido com Flask. O sistema permite adicionar, editar, deletar e listar corretores, além de buscar endereços pelo CEP e exportar os dados para um arquivo Excel.

## Funcionalidades

- Adicionar corretores
- Editar corretores
- Deletar corretores
- Listar corretores cadastrados
- Buscar endereço pelo CEP
- Exportar dados para um arquivo Excel

## Requisitos

- Python 3.x
- Flask
- SQLite
- Pandas
- openpyxl

## Instalação

1. Clone o repositório:

```sh
git clone https://github.com/YOUR_GITHUB_USERNAME/REPOSITORY_NAME.git
cd REPOSITORY_NAME

2. Crie um ambiente virtual e ative-o:
python -m venv venv
# No Windows
venv\Scripts\activate
# No macOS/Linux
source venv/bin/activate

3. Instale as dependências:
pip install -r requirements.txt

4. Inicie o servidor Flask:
python app.py

sistema_cadastro/
│
├── app.py
├── export_to_excel.py
├── requirements.txt
├── templates/
│   └── index.html
└── static/
    └── js/
        └── script.js
Endpoints
/ - Página inicial com o formulário de cadastro e a lista de corretores
/add_corretor - Endpoint para adicionar ou editar corretores (POST)
/get_corretores - Endpoint para obter a lista de corretores (GET)
/get_corretor/<int:id> - Endpoint para obter os dados de um corretor específico (GET)
/delete_corretor/<int:id> - Endpoint para deletar um corretor (DELETE)
/enviar_corretores - Endpoint para enviar os corretores cadastrados (POST)
/export_excel - Endpoint para exportar os dados dos corretores para um arquivo Excel (POST)
Como Usar
Preencha o formulário de cadastro e clique em "Adicionar Corretor".
Os corretores cadastrados aparecerão na tabela abaixo do formulário.
Para editar um corretor, clique no botão "Editar" ao lado do corretor na tabela.
Para deletar um corretor, clique no botão "Deletar" ao lado do corretor na tabela.