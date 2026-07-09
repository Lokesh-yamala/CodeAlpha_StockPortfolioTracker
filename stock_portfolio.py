# Stock Portfolio Tracker

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 300,
    "AMZN": 170
}

total = 0

print("===== Stock Portfolio Tracker =====")
print("Available Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

n = int(input("\nHow many different stocks do you own? "))

for i in range(n):
    stock = input("\nEnter Stock Name: ").upper()

    if stock in stock_prices:
        quantity = int(input("Enter Quantity: "))
        value = stock_prices[stock] * quantity
        total += value
        print(f"Value of {stock}: ${value}")
    else:
        print("Stock not found!")

print("\n-----------------------------")
print(f"Total Investment Value = ${total}")

# Save result to a file
file = open("portfolio.txt", "w")
file.write(f"Total Investment Value = ${total}")
file.close()

print("Result saved to portfolio.txt")