# Sooper-Cool-Crypto-Tool

#Task breakdowns:

#1 person builds a module for the frontend of the final product, creates the bokeh interactions, and organizes a jupyter notebook creating the structure or ‘bones’ of the code.

#1 - Jack -  digs into the gas tracker and first finds a way to display the gas by using a function. By building functions, we can then import the functions for gas into the main notebook when everything is ready. Iterate on top of the first accomplishment of displaying gas and begin building functions that go deeper and deeper into functionality. Gas usd price differences between chains plot, transaction fees across chains.

#1 - Michael -  analyzes ethereum burn rate and production rate to find the difference between the two and historical effects/correlations with price. General Ethereum analysis, std deviation, monte carlo of future returns based on mean reversion. Parse all of this into functions for modularization.

#1 - Jeff - Builds charting tool function to take input of cryptocurrency and time frame to build a plot. Maybe add options for trend analysis, TA, std deviations, moving averages, etc. Use functions for this that can be called on demand from the main book.

#-change - basic charting function that takes inputs for the function of: cryptocurrency, start date, end date, tracks daily prices at closing. Basically API would need ability to call by cryptocurrency name, date, close price etc to accomplish.

#1 Centralized exchange arbitrage opportunity tracker, analysis of reduction of arbitrage over time, arbitrage on non-major cryptocurrencies traded across exchanges potentially exists now in more speculative markets. This may have a stretch goal to be more of a python app in command line than on jupyter since it would have to be running and repeatedly checking prices across exchanges to identify arbitrage opportunities to provide relevant information. 