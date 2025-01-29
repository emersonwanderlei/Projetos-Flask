# Projetos-Flask
 Esse repositório é para meus projetos e aulas no flask

 # Cadastro de Secretários

Este é um projeto simples de um sistema de gerenciamento de dados de secretários(as). Ele permite visualizar, adicionar, editar e excluir informações de secretários(as) armazenadas em um banco de dados.

Funcionalidades

Listagem de secretários(as): Visualiza todos os dados cadastrados.

Criação de registros: Permite adicionar novos secretários(as).

Edição de registros: Atualiza dados existentes.

Exclusão de registros: Remove secretários(as) do sistema.

Tecnologias Utilizadas

Flask: Framework backend.

Flask-WTF: Criação e validação de formulários.

SQLAlchemy: ORM para interação com o banco de dados.

HTML e Bootstrap: Frontend responsivo.

Requisitos

Certifique-se de ter o Python 3.7+ instalado. Para instalar as dependências, execute:

pip install -r requirements.txt

Arquivo requirements.txt:

Flask==2.3.3
Flask-SQLAlchemy==3.0.3
Flask-WTF==1.0.1

Instruções de Instalação

Clone este repositório:

git clone https://github.com/seuusuario/cadastro-secretarios.git
cd cadastro-secretarios

Ative um ambiente virtual:

python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

Instale as dependências:

pip install -r requirements.txt

Execute o aplicativo:

flask run

Acesse o sistema em http://localhost:5000.

Estrutura de Arquivos

.
├── app.py                  # Arquivo principal
├── templates/
│   └── home.html           # Interface do sistema
├── static/
│   └── style.css           # Estilizações (opcional)
└── models.py               # Modelo de banco de dados

Capturas de Tela

Tela Principal:
Exibe a lista de secretários(as) cadastrados.

Formulário de Edição:
Permite editar os dados de um registro existente.

Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

Se tiver alguma sugestão ou dúvida, fique à vontade para abrir uma issue.


