#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


import pandas as pd
from pathlib import Path
import hvplot.pandas
import os
#get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


def get_data_file_name(exchange,coin,year):
    current_dir=os. getcwd()
    #print(f' Current Directory is {current_dir}')
    s1 ='./Arbitrage/Resources/'
    s2=exchange+'_'
    s3=coin+'USD_'
#    datem = datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
#    print(datem.year)
#    s4=datem.year
    fname=s1+s2+s3+year+'_1min.csv'
    return fname


# In[3]:


def get_coin_onexchng(coin, exchange,year):
    this_df=pd.read_csv(get_data_file_name(exchange,coin,year),index_col='Timestamp',parse_dates=True,infer_datetime_format=True)
    this_df.dropna()
    this_df.reset_index().drop_duplicates(subset='Timestamp').set_index('Timestamp')
    this_df.loc[:,'close']=this_df.loc[:,'close'].astype('float')
    this_df_sliced=this_df.loc[:,'close']
    this_df_sliced=this_df_sliced.rename(exchange)

    return this_df_sliced
    
    


# In[4]:


def get_coin_data(coin, start,end,year):
    exchanges = ['bitstamp','gemini']
   # print(f' {len(exchanges)} supported are {exchanges}')
    bitstamp_close = get_coin_onexchng(coin,'bitstamp',year)
    gemini_close = get_coin_onexchng(coin,'gemini',year)
    merged_btc_df= pd.concat([gemini_close,bitstamp_close],axis=1)
    merged_btc_df=merged_btc_df.dropna()
    merged_btc_df=merged_btc_df[start:end]
    #print(merged_btc_df.describe())
    return merged_btc_df
    


# In[5]:


def get_one_coin_data(coin,start,end,year):
    if (coin=="BTC"):
        print("Supported from exchanges Bitstamp and Gemini")
        price_df=get_coin_data(coin,start,end,year)
     
    elif (coin=="ETH"):
        print("Supported from exchanges Bitstamp and Gemini")
        price_df=get_coin_data(coin,start,end,year)
    else:
        print("Not Supported")
    return price_df


# In[6]:


import panel as pn
import datetime
def arbitrage_crypto (coin, start_date, end_date):
    datem = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    arbitrage_df = get_one_coin_data(coin,start_date,end_date,str(datem.year))
    arbitrage_diff=arbitrage_df['bitstamp']-arbitrage_df['gemini']
    arbitrage_diff_perc=(arbitrage_diff/arbitrage_df['gemini'])*100
    arbitrage_df['arbitrage diff']=arbitrage_diff
    arbitrage_df['arbitrage diff %']= arbitrage_diff_perc
    arbitrage_df['price change']=arbitrage_df['gemini'].pct_change()*100
    arbitrage_df.dropna()
    arbitrage_df['abs_arb_diff'] = abs(arbitrage_df['arbitrage diff'])
    arbitrage_df['abs_price_change']=abs(arbitrage_df['price change'])
    return arbitrage_df
   


# In[11]:


#This call arbitrage_df=arbitrage_crypto (coin, start_date,end_date) needs to be included in the main module being developed by John
#Restiriction Currently only supporting 2 coins BTC and ETH.
# BTC Data is available from second half of 2015 to present
# ETH data is spotty till 2018. So ETH I would stay 2019 or later
# start_data and end_date needs to be in the same calendar year. There are more than 500,000 bars in each year. As we do not have adatabase implementation, 
#these are being read out of csv files
# For Graph Generation performance I recomend 2/3 monthts between start and end
# It is important that start and end date be sent in the format shown below. If this needs to change let me know as the function may have t be changed to handle the format
coin='BTC'
start_date='2021-05-01'
end_date='2021-05-31'
arbitrage_df=arbitrage_crypto (coin, start_date,end_date)
arbitrage_df


# In[12]:


#I could not figure out how to render plots in Jupyter notebook when this call is in a function. Unless someone knows how to do it for Thursday presntation this cell and the 2 cells below will need to be in the main Jupyter notebook 
#outside of any function
arbitrage_df.hvplot.line(x='Timestamp', y= ['gemini', 'bitstamp'],figsize=(40,14),title=f'Plot of {coin} on different exchanges')


# In[13]:


arbitrage_df.hvplot(x='Timestamp',y=['arbitrage diff'],selection_color='Red',figsize=(40,14),title='Price Difference on the Different Exchanges')


# In[14]:


arbitrage_df.hvplot(x='Timestamp',y=['abs_arb_diff'],figsize=(40,14),title='Absolute Price Difference between the differnt Exchanges')


# In[ ]:




