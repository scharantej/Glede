
from flask import Flask, render_template, request, redirect, url_for
import yfinance as yf

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    ticker = request.form.get('ticker')
    period = request.form.get('period')
    interval = request.form.get('interval')

    stock = yf.Ticker(ticker)
    hist = stock.history(period=period, interval=interval)

    return render_template('results.html', stock=stock, hist=hist)

if __name__ == '__main__':
    app.run(debug=True)
