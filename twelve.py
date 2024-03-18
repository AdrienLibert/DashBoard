import requests
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

API_KEY = '0501613bd7084336810ea318ff512f3a'

@app.route('/api/v1/quote/<symbol>')
def get_daily_time_series(symbol):
    if not symbol:
        return jsonify({'error': 'Aucun symbole fourni'}), 400  # Retourne une erreur 400
    BASE_URL = "https://www.alphavantage.co/query"
    response = requests.get(BASE_URL, params={
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": API_KEY
    })
    data = response.json()
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
