# import
import yfinance as yf
import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv



# import das variaveis de ambiente

commodities = ['CL=F', 'GC=F', 'SI=F']

DB_HOST = os.getenv('DB_HOST_PROD')
DB_HOST_PROD= os.getenv
DB_PORT_PROD= os.getenv
DB_NAME_PROD= os.getenv
DB_USER_PROD= os.getenv
DB_PASS_PROD= os.getenv
DB_SCHEMA_PROD= os.getenv
DB_THREADS_PROD= os.getenv
DB_TYPE_PROD= os.getenv
DBT_PROFILES_DIR = os.getenv



def buscar_dados_commodities(simbolo, periodo='5d', intervalo='1d'):
    ticker = yf.Ticker(simbolo)
    dados = ticker.history(period=periodo, interval=intervalo)[['Close']]
    dados['simbolo']= simbolo
    return dados

def buscar_todos_dados_commodities(commodities):
    todos_dados = []
    for simbolo in commodities:
        dados = buscar_dados_commodities(simbolo)
        todos_dados.append(dados)
    return pd.concat(todos_dados)

def salvar_no_postgress(def):
    df.to_sql('commodities', engine, if_exists='replace', index=True, index_label='Date', schema=schema)


if __name__ == "__main__":
    dadods_concatenados = buscar_todos_dados_commodities(commodities)
    print(dadods_concatenados)

# pegar a cotacao dos meus ativos


# concatenar os meus ativos 



# salvar no banco de dados