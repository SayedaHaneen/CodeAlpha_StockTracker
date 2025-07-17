# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 300,
    "AMZN": 130
}

portfolio = {}
total_investment = 0

print("=== Stock Portfolio Tracker ===")
print("Available stocks: ", ', '.join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock symbol (or type 'done' to finish): ").upper()
    if stock == 'DONE':
        break

    if stock not in stock_prices:
        print("⚠️ Stock not found. Please enter a valid symbol.")
        continue

    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
        if quantity < 0:
            print("Quantity can't be negative.")
            continue
    except ValueError:
        print("⚠️ Please enter a valid number.")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity
    total_investment += stock_prices[stock] * quantity

# Display result
print("\n=== Portfolio Summary ===")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    print(f"{stock}: {qty} shares × ${price} = ${value}")

print(f"\n💰 Total Investment Value: ${total_investment}")

# Option to save result
save = input("\nDo you want to save the result to a file? (yes/no): ").lower()
if save == 'yes':
    filename = "portfolio_summary.txt"
    with open(filename, 'w') as file:
        file.write("=== Portfolio Summary ===\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            file.write(f"{stock}: {qty} shares × ${price} = ${value}\n")
        file.write(f"\nTotal Investment Value: ${total_investment}\n")
    print(f"✅ Portfolio summary saved to '{filename}'.")

