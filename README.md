# Configurando o ambiente de desenvolvimento
## Requisitos
- Python > 3.6
- PostgreSQL 
- MongoDB

## Instalando e configurando PostgreSQL
- Windows
  - baixe e instale do [site oficial do PostgreSQL](https://www.postgresql.org/download/)
- Linux (debian based)
  - instale atraves do `sudo apt-get install postgresql`
### Configurando
> É criado um usuario com o nome `postgres` após a instalação. Utilize esse usuario para se conectar ao banco.
- Windows

Abra o pgAdmin e crie o db `LocationTracker`
- Linux

Crie o db `LocationTracker` seguindo os comandos do arquivo `postgresql_database_example.txt`

## Instalando e configurando MongoDB
- Windows
  - baixe do [site oficial do MongoDB](https://www.mongodb.com/download-center#community)
  - instalar
  - adicionar a pasta bin do mongo ao PATH do windows
  - criar pasta `/data/db` no disco que o mongo foi instalado
- Linux 
  - instale atraves do `sudo apt-get install mongo`

### Mongo Compass
baixe e instale o mongo compass para ajudar na visualização dos dados

## Configurando o ambiente virtual do Python
### Instalando depêndencias
- Criar um ambiente virtual com o comando `python -m venv env`
- Ative o ambiente virtual (e você irá precisar refazer este único passo sempre que executar usar o sistema):
    - No Windows, execute no prompt (cmd): `env\Scripts\activate.bat`
    - No Unix ou MacOS, execute no terminal (bash): `source env/bin/activate`
- Instalar as dependências pelo comando `pip install -r requirements.txt`
### Configurando Conexão com o psql
- Criar o arquivo `config.py` (com as informações de conexão configuradas do psql) na pasta `LocationTrackerAPI` usando o arquivo `config_example.py` de exemplo
### Gerando migrações iniciais
- Execute o comando `python manage.py makemigrations`
- Execute o comando `python manage.py migrate`
- Execute o comando `python manage.py migrate location --database=location_db`
### Populando o banco de dados
- Execute o comando `python script.py`

# Rodando a aplicação
Considerando que todo o ambiente foi corretamente instalado e configurado, sempre que for executar o sistema:
- Execute novamente o passo de ativação do ambiente virtual
- Inicie o servidor com `python manage.py runserver` e leia o output que lhe dirá em qual endereço IP e porta a aplicação está rodando
    - Se for "0.0.0.0" significa que está aberto para toda sua rede interna, e você deve encontrar seu IP público (no Linux, use ```ifconfig```)
- Se você souber como usar aplicações RESTful, consulte nossa documentação, e o comando ```curl``` poderá lhe ajudar a formar as requisições
