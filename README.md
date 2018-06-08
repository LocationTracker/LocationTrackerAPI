# Configurando o ambiente de desenvolvimento
## Requisitos
- Python > 3.0
- PostgreSQL 
- MongoDB

## PostgreSQL
### Windows
#### Instalação
Baixe e instale do [site oficial do PostgreSQL](https://www.postgresql.org/download/)
#### Configuração
Abra o pgAdmin e crie o db `LocationTracker`
#### Rodando
execute o comando `pg_ctl.exe restart -D "C:\Program Files\PostgreSQL\9.6\data"`

### Linux (Debian based)
#### Instalação
Instale atraves do `sudo apt-get install postgresql`
#### Configuração
> Crie um novo usuario com seu nome de usuario do linux
- `sudo su`
- `sudo passwd postgres`
- `su - postgres`
- `createuser --pwprompt --interactive nome_usuario`

> Crie o db `LocationTracker`
- `createdb LocationTracker -O nome_usuario`
- `psql LocationTracker`
    - na primeira vez execute `\password` dentro do shell do psql
#### Rodando
- `sudo systemctl start postgresql`
- `sudo systemctl stop postgresql`
- `sudo systemctl restart postgresql`
    - `sudo /etc/init.d/postgresql restart`
- `sudo systemctl status postgresql`

## MongoDB
### Windows
#### Instalação
- baixe do [site oficial do MongoDB](https://www.mongodb.com/download-center#community)
#### Configuração
- adicionar a pasta bin do mongo ao PATH do windows
- criar pasta `/data/db` no disco que o mongo foi instalado

### Linux (Debian based)
#### Instalação
instale através do `sudo apt-get install mongodb`
### Rodando
execute o comando `mongod`

### Mongo Compass
baixe e instale o mongo compass para ajudar na visualização dos dados

## Python
### Criando ambiente virtual
Crie um ambiente virtual com o comando `python -m venv env`

Ative o ambiente virtual (e você irá precisar refazer este único passo sempre que executar usar o sistema):
- No Windows, execute no prompt (cmd): `env\Scripts\activate.bat`
- No Unix ou MacOS, execute no terminal (bash): `source env/bin/activate`
### Instalando dependências
Execute o comando `pip install -r requirements.txt` com o ambiente virtual ativo
### Configurando Conexão com o psql e mongo
Crie o arquivo `config.py` (com as informações de conexão configuradas do psql e mongo) na pasta `LocationTrackerAPI` usando o arquivo `config_example.py` de exemplo
### Gerando migrações iniciais
- Execute o comando `python manage.py makemigrations`
- Execute o comando `python manage.py migrate`
- Execute o comando `python manage.py migrate location --database=location_db`
### Populando o banco de dados
- Execute o comando `python script.py`
### Iniciando o servidor
Utilize o comando `python manage.py runserver` e leia o output que lhe dirá em qual endereço IP e porta a aplicação está rodando
- Se rodar com o comando `manage.py runserver 0.0.0.0:8000` significa que está aberto para toda sua rede interna, e você deve encontrar seu IP público (no Linux, use ```ifconfig```)
# Rodando a aplicação
Considerando que todo o ambiente foi corretamente instalado e configurado, sempre que for executar o sistema:
- Execute novamente o passo de ativação do ambiente virtual
- Inicie o MongoDB
- Inicie o PostgreSQL 
- Inicie o servidor
