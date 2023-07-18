import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def gridFormat(data):
    # print(data)
    pd.set_option("display.max_rows", None)
    pd.set_option("display.max_columns", None)
    print(data.to_string())

def graphFormat(data, symbol):
    plt.plot(data.index, data["Close"])
    plt.xlabel("Date")
    plt.ylabel("Closing Price")
    plt.title(f"{symbol} Stock Price")
    plt.grid(True)
    plt.show()

def dateValidation(date):
    while True:
        storedate = input(date)
        try:
            pd.to_datetime(storedate)
            return storedate
        except ValueError:
            print("Invalid date format. Please enter a date in the format YYYY-MM-DD.")

while True:
    stockname = input("Enter the stock symbol: ").upper().strip()
    try:
        yf.Ticker(stockname).info
        break
    except Exception as e:
        print("Invalid company name. Please enter a valid stock symbol.")

while True:
    startdate = dateValidation("Enter start date (YYYY-MM-DD): ")
    enddate = dateValidation("Enter end date (YYYY-MM-DD): ")
    try:
        stockinfo = yf.download(stockname, start=startdate, end=enddate)
        break
    except Exception as e:
        print("Please check your date inputs.")

while True:
    choice = input("Do you want to view data in a 'Grid' or 'Graph' layout (or type 'exit' to quit)? ").lower().strip()

    if choice == "grid":
        gridFormat(stockinfo)
        break
    elif choice == "graph":
        graphFormat(stockinfo, stockname)
        break
    elif choice == "exit":
        print("Exiting the program...")
        exit()
    else:
        print("Invalid choice. Please enter 'Grid' for grid layout, 'Graph' for graph layout, or 'exit' to quit the program.")
