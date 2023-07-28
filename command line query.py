import time
import datetime
import pandas as pd
import numpy as np
from IPython.display import display
import matplotlib.pyplot as plt 
#from scipy import linregress

time_start = int(time.mktime(datetime.datetime(2020, 1, 1, 23, 59).timetuple()))
time_end = int(time.mktime(datetime.datetime(2023, 1, 1, 23, 59).timetuple()))
interval = "1wk"
stock_ls = []
ticker_list=[]
y = "y"
while y == "y":
    ticker_list.append(input("What ticker symbols?"))
    y = input("Add another stock y/n?")

for ticker in ticker_list:
    query_string = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={time_start}&period2={time_end}&interval={interval}&events=history&includeAdjustedClose=true"
    loop_df= pd.read_csv(query_string)  
    loop_df = loop_df [["Date","Close","Volume"]]
    loop_df ['Ticker'] = ticker
    stock_ls.append(loop_df)
stock_df = pd.concat(stock_ls)  
display(stock_df)
stock_df['Date'] = pd.to_datetime(stock_df['Date']).astype(np.int64)
#(slope, intercept, r_value, p_value, std_err) = linregress(x_values, y_values)
for ticker in ticker_list:
    loop_df =stock_df.loc[stock_df["Ticker"] == ticker] 
    f = np.polyfit(loop_df['Date'], loop_df['Close'], deg=1)
    print(f"The trend line slope of {ticker} is {f[0]}")       
    #display(loop_df)         
               

