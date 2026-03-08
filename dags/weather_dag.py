from datetime import datetime, timedelta
from airflow.decorators import dag, task
from pathlib import Path
import sys, os

sys.path.insert(0, '/opt/airflow/src') # Adiciona o caminho para o diretório src

from extract_data import extract_weather_data
from load_data import load_weather_data
from transform_data import data_transformation  # Verify this function exists in transform_data.py
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parent.parent / 'config' / '.env'
load_dotenv(env_path)

API_KEY = os.getenv('API_KEY')
url = f'https://api.openweathermap.org/data/2.5/weather?q=Sao Paulo,BR&units=metric&appid={API_KEY}'

@dag(
    dag_id='weather_etl_pipeline',
    default_args={
        'owner': 'airflow',
        'depends_on_past': False,
        'start_date': datetime(2024, 1, 1),
        'retries': 2,
        'retry_delay': timedelta(minutes=5),
    },
    description='ETL pipeline para extrair, transformar e carregar dados de clima de São Paulo',
    schedule = '0 * * * *',  # ✅ a cada hora (ex: 13:00, 14:00, 15:00...)
    start_date=datetime(2026, 3, 9),
    catchup=False,
    tags=['weather', 'etl', 'airflow']
)
def weather_etl_pipeline():
    @task()
    def extract():
        return extract_weather_data(url)  # Retorna o caminho do arquivo extraído para a próxima tarefa

    @task()
    def transform(extracted_path):
        df = data_transformation(extracted_path)
        df.to_parquet('/opt/airflow/data/transformed_weather_data.parquet', index=False)  # Salva o DataFrame transformado em um arquivo Parquet
        return '/opt/airflow/data/transformed_weather_data.parquet'  # Retorna o caminho do arquivo transformado para a próxima tarefa

    @task()
    def load(parquet_path):
        import pandas as pd
        df = pd.read_parquet(parquet_path)  # Lê o arquivo Parquet transformado
        load_weather_data('sp_weather', df)

    extracted_path = extract()
    parquet_path = transform(extracted_path)
    load(parquet_path)

weather_etl_pipeline()