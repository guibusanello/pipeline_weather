# from src.extract_data import extract_weather_data # importa a função extract_weather_data do módulo src.extract_data, que é responsável por extrair os dados de clima da API
# from src.load_data import load_weather_data # importa a função load_weather_data do módulo src.load_data, que é responsável por carregar os dados transformados para o banco de dados
# from src.transform_data import data_transformation # importa a função data_transformation do módulo src.transform_data, que é responsável por transformar os dados extraídos em um formato adequado para o carregamento no banco de dados

# import os # biblioteca para acessar variáveis de ambiente, como as credenciais do banco de dados
# from pathlib import Path # biblioteca para manipular caminhos de arquivos, garantindo compatibilidade entre diferentes sistemas operacionais
# from dotenv import load_dotenv # biblioteca para carregar variáveis de ambiente a partir de um arquivo .env, facilitando a configuração do ambiente de desenvolvimento

# import logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# env_path = Path(__file__).resolve().parent.parent / 'config' / '.env' 
# load_dotenv(env_path)

# API_KEY = os.getenv('API_KEY') # obtém a chave da API a partir das variáveis de ambiente

# url = f'https://api.openweathermap.org/data/2.5/weather?q=Sao Paulo,BR&units=metric&appid={API_KEY}' # define a URL para a API de clima, incluindo a cidade de São Paulo e a chave da API
# table_name = 'sp_weather' # define o nome da tabela onde os dados transformados serão carregados no banco de dados

# def pipeline():
#     try:
#         logging.info("Etapa 1: Extract - Extraindo dados da API de clima...") # registra uma mensagem de log indicando o início da etapa de extração dos dados
#         extract_weather_data(url) # chama a função extract_weather_data para extrair

#         logging.info("Etapa 2: Transform - Transformando os dados extraídos...") # registra uma mensagem de log indicando o início da etapa de transformação dos dados
#         df = data_transformation('data/weather_data.json') # chama a função data_transformation para transformar os dados extraídos e armazena o resultado em um DataFrame

#         logging.info("Etapa 3: Load - Carregando os dados transformados para o banco de dados...") # registra uma mensagem de log indicando o início da etapa de carregamento dos dados
#         load_weather_data(table_name, df) # chama a função load_weather_data para carregar os dados transformados para o banco de dados, especificando o nome da tabela e o DataFrame contendo os dados
    
#     except Exception as e:
#         logging.error(f"Ocorreu um erro durante a execução do pipeline: {e}") # registra uma mensagem de log de erro caso ocorra uma exceção durante a execução do pipeline
#         import traceback
#         traceback.print_exc() # imprime o rastreamento da pilha para ajudar na depuração

# pipeline() # chama a função pipeline para executar todo o processo de ETL (Extract, Transform, Load)