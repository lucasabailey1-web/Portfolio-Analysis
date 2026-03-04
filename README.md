# Portfolio-Analysis for Q2 of 2025
# Cumulative Vs Benchmark: 
#    The first and most simple program I am running here is a 2-line pyplot graph for Q2 of 2025. It takes all Yfinance data for SPY (State Street SPDR ETF Trust), and uses the percent changed function to scale both SPY and my weighted portfolio to the growth a hypothetical $1. 
#    The next useful piece of data is a drawdown graph, where filled in line graphs can be used to measure a portfolio's percentage decline from its previous peak value to its lowest point before a new peak is reached. This is an easy tool to visualize how severe losses become on both my portfolio as it compares to SPY (still scaled to percentage gain/decline). At a drawdown value of zero, the portfolio has reached a new peak. 
#Rolling 30-day Volatility:
#      Volatility, for this context, is just standard deviation. The .rolling function uses the past 29 and current observations for each point. To make this annualized, we take the SQ RT of the amount of trading days per year as volatility scales to square root of time. 
