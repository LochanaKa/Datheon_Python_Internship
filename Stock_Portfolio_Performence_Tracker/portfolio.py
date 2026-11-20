import csv
import requests

def get_stock_data(symbol):
    url="https://www.cse.lk/api/todaySharePrice"

    try:
        response=requests.post(url,data={},timeout=10)
        response.raise_for_status()
        data=response.json()


        print("Data type: ",type(data))
        if isinstance(data,list):
            print("Total records:",len(data))

            if len(data)>0:
                print("First stock record: ")
                print(data[0])
        elif isinstance(data,dict):
            print("Available keys: ")
            print(data.keys())
        return data

    except requests.exceptions.RequestException as e:
        print("CSE API request failed: ",e)
        return None

    except ValueError:
        print("The server did not return valid JSON.")
        return None

def find_stock_price(market_data,symbol):

    if market_data is None:
        return None

    if not isinstance(market_data,list):
        return None

    for stock in market_data:
        if stock["Symbol"]==symbol:
            return stock["current_price"]
    return None

def save_portfolio(portfolio):
    with open("portfolio_summary.csv","w",newline="") as file:
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
        with open("portfolio_summary.csv","r") as file:
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

while True:

    print("\n1. Add Stock ")
    print("2. View Portfolio ")
    print("3. Calculate Total Investment")
    print("4. Exit ")

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

    #OPTION 4 - Exit
    elif choice=="4":
        save_portfolio(portfolio)
        print("thank you for using application!")
        break
    else:
        print("Invalid option Please Try again!")
