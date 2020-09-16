# Description : Stock market dashboard to show charts and Data

import streamlit as st
import pandas as pd
from PIL import Image


# Add title and Image
st.write("""# Stock Market Web Application
 **Visually** show data on a stock! Date range from Aug 15, 2019 - Aug 14, 2020
 Created by **Suhas Paunikar**""")

image = Image.open("C:/Users/Joshua Lindsay/PycharmProjects/Python_project/stock_image.jpg")
st.image(image, use_column_width=True)

# Create a Sidebar Header
st.sidebar.header('User Input')


# Create a function to get the user input
def get_input():
    start_date = st.sidebar.text_input("Start Date", "2019-08-15")
    end_date = st.sidebar.text_input("End Date", "2020-08-14")
    stock_symbol = st.sidebar.text_input("Stock Symbol", "DJI")
    return start_date, end_date, stock_symbol


# Create a function to get the Company Name
def get_company_name(symbol):
    if symbol == 'DJI':
        return 'Dow Jones Industrial'
    elif symbol == 'BTC-USD':
        return 'Coin Market Cap (Bitcoin)'
    elif symbol == 'CL=F':
        return 'NY Mercantile (Crude Oil)'
    elif symbol == 'GC=F':
        return 'COMEX (Gold)'
    elif symbol == 'SL=F':
        return 'COMEX (Silver)'
    else:
        'None'


# Create a function to get tye proper company data and the proper time-frame from the user to start
def get_data(symbol, start, end):
    # Load the Data
    if symbol.upper() == 'DJI':
        df = pd.read_csv("C:/Users/Joshua Lindsay/PycharmProjects/Python_project/DJI.csv")
    elif symbol.upper() == 'BTC-USD':
        df = pd.read_csv("C:/Users/Joshua Lindsay/PycharmProjects/Python_project/BTC-USD.csv")
    elif symbol.upper() == 'CL=F':
        df = pd.read_csv("C:/Users/Joshua Lindsay/PycharmProjects/Python_project/CL=F.csv")
    elif symbol.upper() == 'GC=F':
        df = pd.read_csv("C:/Users/Joshua Lindsay/PycharmProjects/Python_project/GC=F.csv")
    elif symbol.upper() == 'SL=F':
        df = pd.read_csv("C:/Users/Joshua Lindsay/PycharmProjects/Python_project/SL=F.csv")
    else:
        df = pd.DataFrame(columns=['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'])

    # Get the Date Range
    start = pd.to_datetime(start)
    end = pd.to_datetime(end)

    # Set the start and end index rows both to 0
    start_row = 0
    end_row = 0

    # start the date from the top of the data set and go down to see if the users start date is less than or equal to the date in the data set
    for i in range(0, len(df)):
        if start <= pd.to_datetime(df['Date'][i]):
            start_row = i
            break

    # Start from the bottom of the data set ang go up to see if the users end date is greater than or equal to date in the data set
    for j in range(0, len(df)):
        if end >= pd.to_datetime(df['Date'][len(df) - 1 - j]):
            end_row = len(df) - 1 - j
            break

    # Set the index to be the date
    df = df.set_index(pd.to_datetime(df['Date'].values))

    return df.iloc[start_row:end_row + 1, :]


# get the user Input
start, end, symbol = get_input()
# Get the Date
df = get_data(symbol, start, end)
# Get the Company name
company_name = get_company_name(symbol.upper())

# display the close price
st.header(company_name + "Close Price\n")
st.line_chart(df['Close'])

# display the Volume
st.header(company_name + "Volume\n")
st.line_chart(df['Volume'])

# Get stats on data
st.header('Data Statistics')
st.write(df.describe())
