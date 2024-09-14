import yfinance as yf
import pandas as pd

class StockPortfolio:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, ticker, quantity):
        if ticker in self.stocks:
            self.stocks[ticker] += quantity
        else:
            self.stocks[ticker] = quantity

    def remove_stock(self, ticker, quantity):
        if ticker in self.stocks:
            if self.stocks[ticker] >= quantity:
                self.stocks[ticker] -= quantity
            else:
                print("You don't have enough shares to sell.")
        else:
            print("You don't own this stock.")

    def track_performance(self):
        for ticker, quantity in self.stocks.items():
            stock = yf.Ticker(ticker)
            data = stock.history(period="1d")
            current_price = data.iloc[-1]['Close']
            print(f"Stock: {ticker}, Quantity: {quantity}, Current Price: {current_price}")

    def get_portfolio_value(self):
        total_value = 0
        for ticker, quantity in self.stocks.items():
            stock = yf.Ticker(ticker)
            data = stock.history(period="1d")
            current_price = data.iloc[-1]['Close']
            total_value += current_price * quantity
        return total_value

portfolio = StockPortfolio()
while True:
    print("1. Add stock")
    print("2. Remove stock")
    print("3. Track performance")
    print("4. Get portfolio value")
    print("5. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        ticker = input("Enter the stock ticker: ")
        quantity = int(input("Enter the quantity: "))
        portfolio.add_stock(ticker, quantity)
    elif choice == "2":
        ticker = input("Enter the stock ticker: ")
        quantity = int(input("Enter the quantity: "))
        portfolio.remove_stock(ticker, quantity)
    elif choice == "3":
        portfolio.track_performance()
    elif choice == "4":
        print(f"Portfolio value: {portfolio.get_portfolio_value()}")
    elif choice == "5":
        break
    else:
        print("Invalid option. Please choose again.")