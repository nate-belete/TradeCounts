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



Hi [Recipient Name],

This email outlines the current state of HomeView reporting and proposes changes to optimize its process and resource allocation.

Background:

HomeView is Fannie Mae's free online homeownership education course.  To fulfill Fair Lending requirements and track equitable access, we collect demographic information (race, gender, age, etc.) from enrollees.

Currently, our process involves:

Data Collection: Demographic data is collected during enrollment.
Data Transfer: Encrypted enrollment data is stored in a marketing data lake.
Report Generation: We use a Python script to generate reports from the encrypted data. This script requires periodic updates due to the free-form nature of race attribute entries.
Report Distribution: The Marketing team and Steven H. (for Equitable Reporting) are the primary consumers of this report.
Challenges:

Demand for the HomeView report from Marketing has significantly decreased.
Maintaining the script due to free-form race entries requires manual updates.
Our team's involvement in generating this report diverts resources from other Fair Lending tasks.
Proposed Solutions:

1. Offload HomeView reporting to Steven H.'s team:

Pros:
Steven is familiar with the dataset and its purpose.
Aligns with and enhances their existing Equitable Reporting workflow.
Cons:
Steven's team may need to rewrite the script in their preferred language.
They will need to manage updates for free-form race entries.
2.  Generate reports on an as-needed basis:

Pros:
We retain control over the demographic data.
Cons:
Periodic updates to the script still require resources.
We continue to produce reports with minimal demand.
Recommendation:

I recommend offloading HomeView reporting to Steven H.'s team (option 1). This allows them to fully own the Equitable Reporting process, improves efficiency, and frees our team to focus on other priorities. Carla concurs with this recommendation.

Please share your thoughts and feedback on this proposal.

Thanks,
Nate
