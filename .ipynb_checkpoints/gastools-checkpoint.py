#Imports
import pandas as pd
import hvplot.pandas
from pathlib import Path
import os
import json
import requests
from dotenv import load_dotenv
import matplotlib.pyplot as plt

# Current Gas prices
def get_current_gas(coin):
    url = f"https://owlracle.info/{str(coin).lower()}/gas"
    response = requests.get(url).json()
    gas_gwei = response['speeds'][1]['gasPrice']
    gas_eth = gas_gwei/1000000000
    gas_avax = gas_gwei*.00000006
    gas_poly = gas_gwei*.00000354
    if coin == 'eth':
        print(f"The current standard ETH gas price is {gas_gwei:.2f} gwei or {gas_eth:.8f} ETH")
    elif coin == 'avax':
        print(f"The current standard AVAX gas price is {gas_gwei:.2f} gwei or {gas_avax:.8f} AVAX")
    elif coin == 'poly':
        print(f"The current standard POLY gas price is {gas_gwei:.2f} gwei or {gas_poly:.8f} MATIC")
              
    return

# Chart Gas History
def create_gas_chart():
    eth_historic_gas_url = f"https://owlracle.info/eth/history"
    eth_historic_gas_response = requests.get(eth_historic_gas_url).json()
    eth_df = pd.DataFrame(eth_historic_gas_response)
    eth_df = eth_df[['timestamp', 'gasPrice']]
    timeframe = eth_df['timestamp']
    gas_stats_eth = []
    for row in eth_df['gasPrice']:
        gas_stats_eth.append(row['close'])
    gas_df = pd.DataFrame(gas_stats_eth)
    gas_df['ETH'] = gas_df
    index = pd.to_datetime(timeframe.astype(str))
    gas_df.index = index

    avax_historic_gas_url = f"https://owlracle.info/avax/history"
    avax_historic_gas_response = requests.get(avax_historic_gas_url).json()
    avax_df = pd.DataFrame(avax_historic_gas_response)
    avax_df = avax_df[['timestamp', 'gasPrice']]
    timeframe = avax_df['timestamp']
    gas_stats_avax = []
    for row in avax_df['gasPrice']:
        gas_stats_avax.append(row['close'])
    gas_df['AVAX'] = gas_stats_avax
    index = pd.to_datetime(timeframe.astype(str))
    gas_df.index = index

    bsc_historic_gas_url = f"https://owlracle.info/bsc/history"
    bsc_historic_gas_response = requests.get(bsc_historic_gas_url).json()
    bsc_df = pd.DataFrame(bsc_historic_gas_response)
    bsf_df = bsc_df[['timestamp', 'gasPrice']]
    timeframe = bsc_df['timestamp']
    gas_stats_bsc = []
    for row in bsc_df['gasPrice']:
        gas_stats_bsc.append(row['close'])
    gas_df['BSC'] = gas_stats_bsc
    index = pd.to_datetime(timeframe.astype(str))
    gas_df.index = index

    poly_historic_gas_url = f"https://owlracle.info/poly/history"
    poly_historic_gas_response = requests.get(poly_historic_gas_url).json()
    poly_df = pd.DataFrame(poly_historic_gas_response)
    poly_df = poly_df[['timestamp', 'gasPrice']]
    timeframe = poly_df['timestamp']
    gas_stats_poly = []
    for row in poly_df['gasPrice']:
        gas_stats_poly.append(row['close'])
    gas_df['POLY'] = gas_stats_poly
    index = pd.to_datetime(timeframe.astype(str))
    gas_df.index = index

    gas_df.hvplot(title='Gas Trends for ETH, AVAX, BSC & POLY', value_label='Gas in gwei', legend='top', height=500, width=700, color=['black','black','red','gold','purple'])
    return