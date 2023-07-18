# Stock Data Visualization

This script allows you to fetch and visualize historical stock data using the Yahoo Finance API.

## Table of Contents
- [Installation Tips](#installation-tips)
- [Validation Testing](#validation-testing)
- [Usage information](#usage-information)
- [Function Descriptions](#function-descriptions)
- [Example](#example)

## Installation Tips <a name="installation-tips"></a>
Before running the code, make sure you have installed the following: `yfinance` and `matplotlib`. If you haven't installed them yet, you can do so using `pip`:

```bash
pip install yfinance 
pip install matplotlib
```

## Usage information <a name="usage-information"></a>
1. Make sure you have installed `yfinacnce` and `matplotlib`
2. Download and run the script using the Python interpreter:
```bash 
python stocks.py
```
3. Enter the stock symbol when prompted. If the symbol is not valid, you will be asked to enter a valid one.

4. Enter the start date and end date in the  `YYYY-MM-DD` format. If the dates are not valid, you will be asked to re-enter them.

5. Choose the layout you want to view the data in: 'Grid' or 'Graph'. To exit the program, type 'exit'.

## Function Descriptions <a name="function-descriptions"></a>
1. `gridFormat(data)`
This function takes the historical stock data in a Pandas DataFrame format and displays it in a grid format. The rows and columns have been adjusted to print all of the data.

2. `graphFormat(data, symbol)`
This function takes the historical stock data in a Pandas DataFrame format and the stock symbol as input. It then generates a line graph showing the closing price of the stock over the selected date range.

3. `dateValidation(date)`
This function performs date validation for the entered date. It checks if the input is in the format `YYYY-MM-DD` using Pandas' `pd.to_datetime()` method. If the date format is invalid, the user will be prompted to re-enter a valid date.

## Validation Testing <a name="validation-testing"></a>
The script includes some validation functions to ensure correct user input. These are the validation checks performed:
1. `Stock Symbol Validation`:The script prompts the user to enter the stock symbol. It checks whether the entered symbol is a valid stock symbol by querying the Yahoo Finance API. If the symbol is invalid, the user will be asked to enter a valid stock symbol.
2. `Date Validation`:The user is asked to input a start date and an end date in the format `YYYY-MM-DD`. The script uses the `pd.to_datetime()` method to validate the date format. If the entered date is not in the correct format, the user will be prompted to re-enter a valid date.

## Example <a name="example"></a>
```
Enter the stock symbol: AAPL
Enter start date (YYYY-MM-DD): 2020-01-01
Enter end date (YYYY-MM-DD): 2021-01-01
[*********************100%***********************]  1 of 1 completed
Do you want to view data in a 'Grid' or 'Graph' layout (or type 'exit' to quit)? GRAPH
```
In this Example we query for the `Apple Inc.(AAPL)` closing stock price from `2020-01-01` to `2021-01-01` in a `GRAPH` format.
