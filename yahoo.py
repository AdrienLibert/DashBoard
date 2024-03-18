from flask import Flask, jsonify
from flask_cors import CORS
import yfinance as yf
import requests


app = Flask(__name__)
CORS(app)

@app.route("/<symbol>")
def action(symbol):
    action = yf.Ticker(symbol)
    info = action.info
    name = info.get('shortName', 'Unknown Symbol')
    return f"Name: {name}"

@app.route("/<symbol>/history/<period>")
def historical(symbol, period):
    action = yf.Ticker(symbol)
    hist = action.history(period=period)

    return hist.to_json()


def symbol_from_name(company_name):
    API_KEY = '0EWWU2Y3S30J87SK'
    base_url = "https://www.alphavantage.co/query"
    function = "SYMBOL_SEARCH"
    params = {
        "function": function,
        "keywords": company_name,
        "apikey": API_KEY
    }

    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if 'bestMatches' in data and len(data['bestMatches']) > 0:
            return data['bestMatches'][0]['1. symbol']
        else:
            return "Symbol not found"
    else:
        return "Error fetching symbol"

@app.route("/symbol/<company_name>")
def get_symbol(company_name):
    symbol = symbol_from_name(company_name)
    if symbol:
        return jsonify({'symbol': symbol})
    else:
        return jsonify({'error': 'Symbol not found'}), 404
