import pandas as pd
from pathlib import Path
import numpy as np
import os
import requests
import json
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
from MCForecastTools import MCSimulation


load_dotenv()

alpaca_api_key = os.getenv("ALPACA_API_KEY")
alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")

alpaca = tradeapi.REST(
    alpaca_api_key,
    alpaca_secret_key,
    api_version="v2")

def eth_analysis(tickers,timeframe,start_date,end_date):
    load_dotenv()

    alpaca_api_key = os.getenv("ALPACA_API_KEY")
    alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")

    alpaca = tradeapi.REST(
    alpaca_api_key,
    alpaca_secret_key,
    api_version="v2")
    
    
    
    df_eth = alpaca.get_crypto_bars(
    tickers,
    timeframe,
    start_date,
    end_date
    ).df


#     ETHUSD = df_eth[df_eth['symbol']=='ETHUSD'].drop('symbol', axis=1)
    
    df_eth.describe()

    eth_analysis_plot = df_eth.plot(y='vwap', x='volume', title='ETH Volume Weighted Avg. Price vs Volume transacted')
    eth_analysis_plot
    
def production_rate_analysis(tickers,timeframe,start_date,end_date):
    load_dotenv()

    alpaca_api_key = os.getenv("ALPACA_API_KEY")
    alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")

    alpaca = tradeapi.REST(
    alpaca_api_key,
    alpaca_secret_key,
    api_version="v2")
    
    df_eth = alpaca.get_crypto_bars(
    tickers,
    timeframe,
    start_date,
    end_date
    ).df
    
    value = 6285.00
    average_growth_rate = .097
    days=365
    production_rate = value*(1+average_growth_rate)**days
    growth = df_eth['volume'] * production_rate
    
    growth_plot=growth.plot(kind='line',figsize=(20,10), title="Daily Growth of Coin Supply")
    growth_plot
    
def daily_returns_analysis(tickers,timeframe,start_date,end_date):
    load_dotenv()

    alpaca_api_key = os.getenv("ALPACA_API_KEY")
    alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")

    alpaca = tradeapi.REST(
    alpaca_api_key,
    alpaca_secret_key,
    api_version="v2")
    
    df_eth = alpaca.get_crypto_bars(
    tickers,
    timeframe,
    start_date,
    end_date
    ).df
    
    eth_daily_returns = df_eth['vwap'].pct_change().dropna()
    eth_cumulative_return = (1 + eth_daily_returns).cumprod()
    
#     eth_daily_returns.plot(figsize=(20,10), title="Daily Returns", ylabel="Percent")
    eth_cumulative_return.plot(figsize=(20,10), title="Cumulative Returns", xlabel="year", ylabel="percent of original investment (eg. 1.0=100%)")
    
    