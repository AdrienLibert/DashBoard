import pandas as pd
import requests

def fetch_sp500_tickers():
    table = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    df = table[0]
    return df['Symbol'].tolist()

sp500_tickers = fetch_sp500_tickers()
print(sp500_tickers)
