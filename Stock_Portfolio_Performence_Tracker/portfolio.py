

print("===================STOCK PORTFOLIO TRACKER====================")

portfolio = []

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

            stock = {"stock": symbol,
                     "quantity": quantity,
                     "Buying_price": buy_price}
            portfolio.append(stock)

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
                f"{stock['stock']} | "
                f"{stock['quantity']} Shares | "
                f"Rs.{stock['Buying_price']:.2f}"
            )

def calculate_investment(portfolio):
    total_investment = 0

    for stock in portfolio:
        investment = stock["quantity"] * stock["Buying_price"]
        total_investment += investment
    print(f"\nTotal Investment: Rs.{total_investment:.2f}")

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
        calculate_investment(portfolio)

    #OPTION 4 - Exit
    elif choice=="4":
        print("thank you for using application!")
        break
    else:
        print("Invalid option Please Try again!")
