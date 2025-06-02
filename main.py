import pandas as pd
import numpy as np


#Read values
#nfl_data = pd.read_csv("NFL Play by Play 2009-2017 (v4).csv",low_memory=False)
wt_sales = pd.read_csv("Walmart_Sales.csv") 
#return the same random records
np.random.seed(0)

#Check missing values 
missing_values_count = wt_sales.isnull().sum()

total_cells = np.product(wt_sales.shape)
total_missing = missing_values_count.sum()

# percent of data that is missing
percent_missing = (total_missing/total_cells) * 100

#Check duplicates
duplicates = wt_sales.duplicated()

#Check date format
date_cols = ["Date"]

wt_sales_date = pd.read_csv('Walmart_Sales.csv', parse_dates = date_cols)

#Create column 'Year'
wt_sales_date['Date'] = pd.to_datetime(wt_sales_date['Date'], format='%d-%m-%Y', errors='coerce')

wt_sales_date['Year'] = wt_sales_date['Date'].dt.year

#Create column 'Month'
wt_sales_date['Month'] = wt_sales_date['Date'].dt.month

#Create column 'Day'
wt_sales_date['Day'] = wt_sales_date['Date'].dt.day

#Create column 'Dayofweek'
wt_sales_date['Days_of_week'] = wt_sales_date['Date'].dt.dayofweek

#Create column 'Daysofweek's names'
wt_sales_date['Days_of_week_names'] = wt_sales_date['Date'].dt.day_name()

#Create column 'year's week'
wt_sales_date['Year_of_week'] = wt_sales_date['Date'].dt.isocalendar().week

#Create column 'Quarter'
wt_sales_date['Quarter'] = wt_sales_date['Date'].dt.quarter

#Create column 'Name of month'
wt_sales_date['Name_of_month'] = wt_sales_date['Date'].dt.month_name()

#Create colummn 'Saison'
def get_saison(date):
    month = date.month
    if month in [12,1,2]:
        return 'winter'
    elif month in [3,4,5]:
        return 'spring'
    elif month in [6,7,8,9]:
        return 'summer'
    else:
        return 'automn'

wt_sales_date['Saison'] = wt_sales_date['Date'].apply(get_saison)

#Average of sales by month
monthly_avg = wt_sales_date.groupby('Month')["Weekly_Sales"].mean()
monthly_avg_df = monthly_avg.reset_index()
monthly_avg_df.columns = ['Month', 'Average_Sales']

print(monthly_avg_df)


