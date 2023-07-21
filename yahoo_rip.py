import time
import datetime
import pandas  as pd

ticker = "DRI"
period1 = int(time.mktime(datetime.datetime(2015, 1,1,23,59).timetuple()))
period2 = int(time.mktime(datetime.datetime(2023, 1,1,23,59).timetuple()))
interval = "1wk" # 1d, 1m

query_string = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true"

df = pd.read_csv(query_string)
print(df)