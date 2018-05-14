# LocationTrackerAPI

# Instruções
### Configurando o ambiente de desenvolvimento
#### Requisitos
Instale os requisitos:
- Python > 3.6
- PostgreSQL 
- MongoDB

##### PostgreSQL
Crie o db `LocationTracker` seguindo os comandos do arquivo `postgresql_database_example.txt`

##### MongoDB
Não é necessária a criação de nenhum db

##### Python
###### Instalando depêndencias
- Criar um ambiente virtual com o comando `python -m venv env`
- Ative o ambiente virtual (e você irá precisar refazer este único passo sempre que executar usar o sistema):
    - No Windows, execute no prompt (cmd): `env\Scripts\activate.bat`
    - No Unix ou MacOS, execute no terminal (bash): `source env/bin/activate`
- Instalar as dependências pelo comando `pip install -r requirements.txt`
###### Configurando Conexão com o psql
- Criar o arquivo `config.py` (com as informações de conexão configuradas do psql) na pasta `LocationTrackerAPI` usando o arquivo `config_example.py` de exemplo
###### Gerando migrações iniciais
- Execute o comando `python manage.py makemigrations`
- Execute o comando `python manage.py migrate`
- Execute o comando `python manage.py migrate location --database=location_db`
###### Populando o banco de dados
- Execute o comando `python script.py`

### Rodando a aplicação
Considerando que todo o ambiente foi corretamente instalado e configurado, sempre que for executar o sistema:
- Execute novamente o passo de ativação do ambiente virtual
- Inicie o servidor com `python manage.py runserver` e leia o output que lhe dirá em qual endereço IP e porta a aplicação está rodando
    - Se for "0.0.0.0" significa que está aberto para toda sua rede interna, e você deve encontrar seu IP público (no Linux, use ```ifconfig```)
- Se você souber como usar aplicações RESTful, consulte nossa documentação, e o comando ```curl``` poderá lhe ajudar a formar as requisições
