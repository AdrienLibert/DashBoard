from flask import Flask
import yfinance as yf

app = Flask(__name__)

@app.route("/")
def hello_world():
    apple_ticker = yf.Ticker("AAPL")
    # Extracting some basic info to display. You can adjust this as needed.
    info = apple_ticker.info
    name = info['shortName']
    current_price = info['currentPrice']
    market_cap = info['marketCap']
    
    # Creating a response string
    response = f"Name: {name}, Current Price: {current_price}, Market Cap: {market_cap}"
    
    return response