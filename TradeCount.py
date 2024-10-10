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




# Split the s3_path column by '/'
split_columns = df['s3_path'].str.split('/', expand=True)

# Assign split components to new columns
df['protocol'] = split_columns[0] + '//'  # Adds the '//' back to protocol
df['bucket_name'] = split_columns[2]
df['customer_data'] = split_columns[3]
df['region'] = split_columns[4]
df['year'] = split_columns[5]
df['month'] = split_columns[6]
df['day'] = split_columns[7]
df['hour'] = split_columns[8]
df['minute'] = split_columns[9]
df['second'] = split_columns[10]
df['event_type'] = split_columns[11]
df['segment'] = split_columns[12]
df['project'] = split_columns[13]
df['object_key'] = split_columns[14]

# Drop the original s3_path if no longer needed
# df.drop(columns=['s3_path'], inplace=True)

# Display the DataFrame with new columns
print(df)

# Apply the function to each row in the DataFrame
df[['schema', 'table']] = df['query'].apply(lambda query: pd.Series(extract_schema_table(query)))

print(df)
