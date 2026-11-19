# print(portfolio[0]["stock"])
# total_investment=0
# for stock in portfolio:
#     investment=stock["quantity"]*stock["Buying_price"]
#     total_investment=total_investment+investment
# print("Total Investment: ",total_investment)

print("===================STOCK PORTFOLIO TRACKER====================")

portfolio = []
total_investment = 0

while True:
    print("1. Add Stock ")
    print("2. View Portfolio ")
    print("3. Calculate Total Investment")
    print("4. Exit ")

    choice = input("Select an option: ")
    if choice=="1":
        print("You Selected Add Stock")
        while True:
            symbol = input("Enter the Stock Ticker: ")
            quantity = int(input("Enter the Quantity: "))
            buy_price = float(input("Enter the Buying Price: "))

            stock = {"stock": symbol, "quantity": quantity, "Buying_price": buy_price}
            portfolio.append(stock)

            print("\nStock added Successfully!")
            end = input("\nAre there any stocks to add? (Y/N)").lower()
            if end == "y":
                continue
            else:
                back_to_main=input("\nGo back to Main Menu (Y/N): ").lower()
                if back_to_main=="y":
                    break
                else:
                    continue

    elif choice=="2":
        print("You Selected View Portfolio")
        print("\n=====================YOUR PORTFOLIO=======================")
        for stock in portfolio:
            print(f"{stock['stock']} | {stock['quantity']} Shares | Rs.{stock['Buying_price']}")

        back_to_main = input("\nGo back to Main Menu (Y/N): ").lower()
        if back_to_main == "y":
            break
        else:
            continue

    elif choice=="3":
        for stock in portfolio:
            investment = stock["quantity"] * stock["Buying_price"]
            total_investment += investment


        back_to_main = input("\nGo back to Main Menu (Press Any Key): ").lower()
        if back_to_main == "y":
            continue
        else:
            continue

    elif choice=="4":
        print("thank you for using application!")
        break
    else:
        print("Invalid option Please Try again!")
