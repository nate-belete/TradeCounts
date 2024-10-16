import yfinance as yf
import pandas as pd
import numpy as np

class SwingTrading:
    """
    A class for Swing Trading using Python
    """
    
    def __init__(self, ticker, start_date, end_date, period, max_increase, min_decrease, number_of_days):
        """
        Initialize a SwingTrading object

        Parameters
        ----------
        ticker : string
            The ticker name of the stock
        start_date : string
            The start date in the YYYY-MM-DD format
        end_date : string
            The end date in the YYYY-MM-DD format
        period : int
            The period of the data (daily, weekly, monthly)
        max_increase : float
            The max percentage of increase
        min_decrease : float
            The min percentage of decrease
        number_of_days : int
            The number of days to check for target
        """
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.period = period
        self.max_increase = max_increase
        self.min_decrease = min_decrease
        self.number_of_days = number_of_days
    
    def get_data(self):
        """
        Retrieves the data from yahoo finance

        Parameters
        ----------
        None
        
        Returns
        -------
        DataFrame
            A pandas DataFrame containing the stock data
        """
        self.data = yf.download(self.ticker, start=self.start_date, end=self.end_date, interval =self.period)
        self.data.reset_index(inplace=True)
        return self.data



df = yf.download('es=F','2023-01-18','2023-01-19',interval='5m')
df.reset_index(inplace=True)

df_preMarket_range = df[0:77].copy()
df_tarding_range = df[77:156].copy()
df_tarding_range.reset_index(inplace=True)

# define min and max values
max_ = int(np.ceil(df_preMarket_range['High'].max()))
min_ = int(np.floor(df_preMarket_range['Low'].min()))

trade_counts = []
for i in range(min_,max_+1,1):
    trade_counts.append({"Price":i,
                        "trade_count": count_price(i, df_tarding_range)})
trade_counts_df = pd.DataFrame(trade_counts) 

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
sns.scatterplot(x='Price',y='trade_count',data=trade_counts_df)
plt.show()

print("Min is {}\nMax is {} \nMean is {}".format(min_,max_,(max_+min_)/2))








import gzip
import shutil
import pyreadstat
import os

# Define file paths
compressed_file = 'your_file.sas7bdat.gz'
decompressed_file = 'your_file_decompressed.sas7bdat'

# Decompress the file to a temporary location
with gzip.open(compressed_file, 'rb') as f_in:
    with open(decompressed_file, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

# Read the decompressed SAS file
df, meta = pyreadstat.read_sas7bdat(decompressed_file)

# Display the DataFrame
print(df.head())

# Clean up: remove the decompressed file if you don't need it anymore
os.remove(decompressed_file)
