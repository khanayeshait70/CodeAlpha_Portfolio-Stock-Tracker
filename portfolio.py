# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 400
}

# User input
stock_name = input("Enter stock symbol: ").upper()
quantity = int(input("Enter quantity: "))

# Calculate total value
if stock_name in stock_prices:
    total_value = stock_prices[stock_name] * quantity

    print("\nPortfolio Summary")
    print("Stock:", stock_name)
    print("Quantity:", quantity)
    print("Price per share: $", stock_prices[stock_name])
    print("Total Investment Value: $", total_value)

else:
    print("Stock not found!")
    