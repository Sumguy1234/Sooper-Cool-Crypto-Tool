# Arbitrage Analysis as part of Sooper-Cool-Crypto-Tool 
## This Branch of the Sooper-Cool-Crypto-Tool investigates the historical pricing data of Crypto Coins on different exchanges to see if Arbitrage opportuinities were available. It then tries to find corelation betwee differnt conditions to see if there is a pattern which can be used for predicitng Arbitrage conditions in the future

## Code Modularity : The code has modularized. This allow for easy extensions. Current limited number of Coints (BTC and ETH) will be supported on 2 exchanges. THe code has been written in a fashion that to extend the number of exchanges a new function has to be written to get the pricing data from the exchange and return it as a Data Frame

## By the time of submission by eend of this week, I will be extending it 3 coins on 2 exchanges each.

## THe Main Module being handled by John will need to collect the Coin Symbol, Start Date and End Date for the analysis and call the function Sooper-Cool-Crypto-Tool_arbitrage (coin, start_date, end_date). I stilll need to write this wrapper function. If any of you care to you could run this version which has hard coded coin, Start_date and end_date
