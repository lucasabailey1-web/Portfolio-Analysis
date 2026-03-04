# Portfolio-Analysis for Q2 of 2025
### Created March 2026
## Cumulative Vs Benchmark: 
###     The first and most simple program I am running here is a 2-line pyplot graph for Q2 of 2025. It takes all Yfinance data for SPY (State Street SPDR ETF Trust), and uses the percent changed function to scale both SPY and my weighted portfolio to the growth of a hypothetical $1. 
## Sharpe Ratio: 
###      This ratio uses the risk free rate (3-month T-bill), average investment return, and volatility of portfolio. It shows us the performance of our investments compared to the risk free T-bill rate and gives us an answer that says: Your investment is performing at X units of return for each unit of risk taken. 
## Monte Carlo Options Pricing:
### This program, prices a 45-day (but adjustable) call option on SPY, but could easily be used for any ticker or date. The program calculates historical daily return (from Jan 1 2025 to March 3 2026) and volatility and then runs fifty-thousand sims of possible price paths foward 45 days. Each simulation uses a random shock created from a bell curve containing scaled SPY real historical volatility. Strike price is set at 5% out-of-the-money. The program returns estimated premium price and a histogram of simulated SPY prices at expiry.
## Drawdown Graph
###     The next useful piece of data is a drawdown graph, where filled in line graphs can be used to measure a portfolio's percentage decline from its previous peak value to its lowest point before a new peak is reached. This is an easy tool to visualize how severe losses become on both my portfolio as it compares to SPY (still scaled to percentage gain/decline). At a drawdown value of zero, the portfolio has reached a new peak. 
## Correlation Heatmap:
###      This map uses Covariance and stddev to measure correlation between activity of every stock. It then builds a heatmap to show how correlated each asset is. Correct math can be seen by the diagonal values of 1 showing identical assets have a maximum correlation of 1. 
## Rolling 30-day Volatility:
###      Volatility, for this context, is just standard deviation. The .rolling function uses the past 29 and current observation for each point. To make this annualized, we take the square root of the amount of trading days per year as volatility scales to square root of time. 


## A problem I encountered and how it was solved:
### Monte carlo options:  yfinance returned the last avaliable data point creating an index with 1 value. 10000 data points created by the sim were not able to fit and the return didnt run even 1 full loop. 
### I originally thought i could '.squeeze' on the first varaible of prices, but that did not work, because the number was in a double container and float only reached through one of those containers. I fixed this by changing the avg_daily_return variable from a float to .item, pulling out a single number for each loop. 
