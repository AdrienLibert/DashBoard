import requests
from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

API_KEY = '0EWWU2Y3S30J87SK'

@app.route('/api/v1/quote/<symbol>')
def get_daily_time_series(symbol):
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
