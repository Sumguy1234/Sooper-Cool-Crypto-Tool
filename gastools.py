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
def create_gas_chart(coin_list):
    coin_df = pd.DataFrame(eth_historic_gas_response)
    coin_df = coin_df[['timestamp', 'gasPrice']]
    timeframe = coin_df['timestamp']
    gas_stats = []
    for row in coin_df['gasPrice']:
        gas_stats.append(row['close'])
    df['ETH'] = gas_stats
    index = pd.to_datetime(timeframe.astype(str))
    df.index = index

    df2 = pd.DataFrame(avax_historic_gas_response)
    df2 = df2[['timestamp', 'gasPrice']]
    timeframe = df2['timestamp']
    gas_stats = []
    for row in df2['gasPrice']:
        gas_stats.append(row['close'])
    df['AVAX'] = gas_stats
    index = pd.to_datetime(timeframe.astype(str))
    df.index = index

    df4 = pd.DataFrame(poly_historic_gas_response)
    df4 = df4[['timestamp', 'gasPrice']]
    timeframe = df4['timestamp']
    gas_stats = []
    for row in df4['gasPrice']:
        gas_stats.append(row['close'])
    df['POLY'] = gas_stats
    index = pd.to_datetime(timeframe.astype(str))
    df.index = index

    df.hvplot(title='Gas Trends for ETH, AVAX & POLY', value_label='Gas in gwei', legend='top', height=500, width=700, color=['black','red','purple'])
        
    return