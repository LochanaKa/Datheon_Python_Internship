import csv
import requests

def get_stock_data():

        url = "https://www.cse.lk/api/tradeSummary"

        headers = {
            "User-Agent": "Mozilla/5.0",
            "Referer": "https://www.cse.lk/",
            "Origin": "https://www.cse.lk",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        try:
            response = requests.post(
                url,
                data={},
                headers=headers,
                timeout=15
            )

            response.raise_for_status()
            data = response.json()

            if isinstance(data, dict):

                stocks = data.get("reqTradeSummery", [])

                print("\nTotal CSE records:", len(stocks))

                if len(stocks) > 0:
                    print("\nFirst stock record:")
                    print(stocks[0])

                return stocks

            print("Unexpected API response format.")
            return None

        except requests.exceptions.RequestException as e:
            print("CSE API request failed:", e)
            return None

        except ValueError:
            print("The server did not return valid JSON.")
            return None


def find_stock_price(market_data, symbol):

    if market_data is None:
        return None

    if not isinstance(market_data, list):
        return None

    for stock in market_data:

        api_symbol = stock.get("symbol", "").upper()

        if api_symbol == symbol.upper():
            return stock.get("price")

        if api_symbol.startswith(symbol.upper() + "."):
            return stock.get("price")

    return None

def save_portfolio(portfolio):
    with open("portfolio.csv","w",newline="") as file:
        writer=csv.writer(file)
        writer.writerow(["Stock","Quantity","Buying_Price"])
        for stock in portfolio:
            writer.writerow([
                stock["Stock"],
                stock["Quantity"],
                stock["Buying_price"]
            ])

def load_portfolio():
    portfolio=[]
    try:
        with open("portfolio.csv","r") as file:
            reader=csv.reader(file)
            next(reader,None) #Skip Header
            for row in reader:
                stock={
                    "Stock":row[0],
                    "Quantity":int(row[1]),
                    "Buying_price":float(row[2])
                }
                portfolio.append(stock)
    except FileNotFoundError:
        print("No previous found. Starting a new one")
    return portfolio

print("\n===================STOCK PORTFOLIO TRACKER====================")

portfolio = load_portfolio()

def calculate_market_value(quantity,current_price):
    market_value=quantity*current_price
    return market_value

def calculate_profit_loss(buy_price,current_price,quantity):
    investment=buy_price*quantity
    market_value=current_price*quantity
    profit_loss=market_value-investment
    return profit_loss

def calculate_return_percentage(buy_price,current_price):
    return_percentage=(
    ((current_price-buy_price)/buy_price)*100
    )
    return return_percentage

def add_stock(portfolio):
        print("\nYou Selected Add Stock")


        while True:

            #Validate stock symbol
            while True:
                symbol = input("Enter the Stock Ticker: ").strip().upper()
                if symbol=="":
                    print("Ticker cannot be empty!")
                else:
                    break

            #Validate Quantity
            while True:
                try:
                    quantity = int(input("Enter the Quantity: "))
                    if quantity<=0:
                        print("Quantity must be positive!")
                        continue
                    break
                except ValueError:
                    print("Enter a Valid Whole Number!")

            #Validate Buying Price
            while True:
                try:
                    buy_price = float(input("Enter the Buying Price: "))
                    if buy_price<=0:
                        print("Price must be Positive!")
                        continue
                    break
                except ValueError:
                    print("Enter a Valid Price!")

            stock = {"Stock": symbol,
                     "Quantity": quantity,
                     "Buying_price": buy_price}
            portfolio.append(stock)
            save_portfolio(portfolio)

            print("\nStock added Successfully!")

            end = input("\nAre there any stocks to add? (Y/N)").lower().strip()
            if end == "y":
                continue
            else:
                back_to_main=input("\nGo back to Main Menu (Y/N): ").lower().strip()
                if back_to_main=="y":
                    break
                else:
                    continue

def view_portfolio(portfolio):
    print("\n=====================YOUR PORTFOLIO=======================")

    if len(portfolio) == 0:
        print("Portfolio is empty!")
    else:
        for stock in portfolio:
            print(
                f"{stock['Stock']} | "
                f"{stock['Quantity']} Shares | "
                f"Rs.{stock['Buying_price']:.2f}"
            )

def calculate_investment(portfolio):
    total_investment = 0

    for stock in portfolio:
        investment = stock["Quantity"] * stock["Buying_price"]
        total_investment += investment

    return total_investment

def calculate_portfolio_performance(portfolio, market_data):

    print("\n========== PORTFOLIO PERFORMANCE ==========")

    if len(portfolio) == 0:
        print("Your portfolio is empty!")
        return

    total_investment = 0
    total_market_value = 0
    total_profit_loss = 0

    for stock in portfolio:

        symbol = stock["Stock"]
        quantity = stock["Quantity"]
        buy_price = stock["Buying_price"]

        # Find current CSE price
        current_price = find_stock_price(market_data, symbol)

        if current_price is None:
            print(f"\n{symbol}: Current price not available.")
            continue

        # Calculate investment
        investment = buy_price * quantity

        # Calculate market value
        market_value = calculate_market_value(
            quantity, current_price
        )

        # Calculate profit or loss
        profit_loss = calculate_profit_loss(
            buy_price, current_price, quantity
        )
        total_investment += investment
        total_market_value += market_value
        total_profit_loss += profit_loss

        # Calculate return percentage
        return_percentage = calculate_return_percentage(
            buy_price, current_price
        )

        print(f"\nStock: {symbol}")
        print(f"Quantity: {quantity}")
        print(f"Buying Price: Rs. {buy_price:.2f}")
        print(f"Current Price: Rs. {current_price:.2f}")
        print(f"Investment: Rs. {investment:.2f}")
        print(f"Market Value: Rs. {market_value:.2f}")
        print(f"Profit/Loss: Rs. {profit_loss:.2f}")
        print(f"Return: {return_percentage:.2f}%")

    print("\n========== OVERALL PORTFOLIO ==========")

    print(f"Total Investment: Rs. {total_investment:.2f}")
    print(f"Total Market Value: Rs. {total_market_value:.2f}")
    print(f"Total Profit/Loss: Rs. {total_profit_loss:.2f}")

    if total_investment > 0:
        total_return = (total_profit_loss / total_investment) * 100
        print(f"Overall Return: {total_return:.2f}%")

def remove_stock(portfolio):

    print("\n========== REMOVE STOCK ==========")

    if len(portfolio) == 0:
        print("Your portfolio is empty!")
        return

    view_portfolio(portfolio)

    symbol = input("\nEnter the stock ticker to remove: ").strip().upper()

    for stock in portfolio:

        if stock["Stock"].upper() == symbol:

            portfolio.remove(stock)

            save_portfolio(portfolio)

            print(f"\n{symbol} removed successfully!")
            return

    print(f"\n{symbol} not found in your portfolio.")

while True:

    print("\n1. Add Stock ")
    print("2. View Portfolio ")
    print("3. Calculate Total Investment")
    print("4. Calculate Portfolio Performance")
    print("5. Remove Stock")
    print("5. Exit ")

    choice = input("Select an option: ")

    #Option 1 : ADD STOCK
    if choice=="1":
        add_stock(portfolio)

    #OPTION 02 - VIEW PORTFOLIO
    elif choice=="2":
        view_portfolio(portfolio)

    #OPTION 3 - CALCULATE TOTAL INVESTMENT
    elif choice=="3":
        total=calculate_investment(portfolio)
        print(f"\nTotal Investment: Rs.{total:.2f}")

    # OPTION 4 - Calculate portfolio Performence
    elif choice == "4":
        market_data = get_stock_data()
        calculate_portfolio_performance(portfolio, market_data)

    #OPTION 5 - Remove Stock
    elif choice == "5":
        remove_stock(portfolio)

    elif choice == "6":
        save_portfolio(portfolio)
        print("Thank you for using application!")
        break


    #OPTION 6 - Exit
    elif choice=="6":
        save_portfolio(portfolio)
        print("thank you for using application!")
        break
    else:
        print("Invalid option Please Try again!")
