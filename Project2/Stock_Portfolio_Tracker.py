stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "AMZN": 190,
    "MSFT": 420
}

print("==" * 30)
print(" Stock Portfolio Tracker")
print("==" * 30)

print("Available Stocks:")
print("Stocks:",",".join(stocks.keys()))

total=0

while True:
    symbol=input("Enter stock symbol to add to your portfolio (or type 'done' to finish): ").upper()

    if symbol == 'DONE':
        break

    if symbol in stocks:
        shares = int(input(f"Enter number of shares for {symbol}: "))
        total += shares * stocks[symbol]
        print(f"Added {shares} shares of {symbol} at ${stocks[symbol]} each.")
    else:
        print("Invalid stock symbol. Please try again.")

print()
print("==" *30)
print("Portfolio Summary")
print("==" * 30)
print(f"Total Investment: ${total}")