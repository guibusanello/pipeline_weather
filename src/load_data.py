from sqlalchemy import create_engine, text # biblioteca para conectar a base de dados e executar consultas SQL
from urllib.parse import quote_plus # biblioteca para codificar a senha do banco de dados, garantindo que caracteres especiais sejam tratados corretamente
import os # biblioteca para acessar variáveis de ambiente, como as credenciais do banco de dados
from pathlib import Path # biblioteca para manipular caminhos de arquivos, garantindo compatibilidade entre diferentes sistemas operacionais
import pandas as pd # biblioteca para manipulação de dados, leitura de arquivos CSV e operações de DataFrame
from dotenv import load_dotenv # biblioteca para carregar variáveis de ambiente a partir de um arquivo .env, facilitando a configuração do ambiente de desenvolvimento

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s') # configura o logging para exibir mensagens de informação, incluindo a data e hora, o nível de log e a mensagem em si. Isso é útil para acompanhar o processo de carregamento dos dados e identificar possíveis problemas.

env_path = Path(__file__).resolve().parent.parent / 'config' / '.env' # define o caminho para o arquivo .env, que deve estar no mesmo diretório do script
load_dotenv(env_path) # carrega as variáveis de ambiente do arquivo .env

user = os.getenv('user') # obtém o nome de usuário do banco de dados a partir das variáveis de ambiente
password = os.getenv('password') # obtém a senha do banco de dados a partir das variáveis de ambiente
database = os.getenv('database') # obtém o nome da base de dados a partir das variáveis de ambiente
host = 'host.docker.internal' # define o host para se conectar ao banco de dados, usando 'host.docker.internal' para acessar o host a partir de um contêiner Docker

def get_engine():
    return create_engine(
        f"postgresql+psycopg2://{user}:{quote_plus(password or '')}@{host}:5432/{database}" # cria a string de conexão para o banco de dados PostgreSQL usando as credenciais e o host definidos, e retorna uma instância do engine do SQLAlchemy
    )

engine = get_engine() # cria uma instância do engine do SQLAlchemy para se conectar ao banco de dados

def load_data(table_name:str, df):
    df.to_sql(name=table_name, con=engine, if_exists='append', index=False) # função para carregar um DataFrame do pandas para uma tabela no banco de dados, usando o método to_sql do pandas. O parâmetro if_exists='append' garante que os dados sejam adicionados à tabela existente sem sobrescrevê-la, e index=False evita que o índice do DataFrame seja adicionado como uma coluna na tabela do banco de dados.
    logging.info(f"Dados carregados com sucesso para a tabela {table_name}") # registra uma mensagem de log indicando que os dados foram carregados com sucesso para a tabela especificada
    df_check = pd.read_sql(f'SELECT * FROM {table_name} LIMIT 5', con=engine) # executa uma consulta SQL para selecionar os primeiros 5 registros da tabela especificada, usando a função read_sql do pandas para ler os resultados diretamente em um DataFrame
    logging.info(f"Total de registros na tabela {table_name}: {len(df_check)}") # registra uma mensagem de log indicando o total de registros na tabela após o carregamento dos dados, usando a função len para contar o número de registros no DataFrame resultante da consulta SQL