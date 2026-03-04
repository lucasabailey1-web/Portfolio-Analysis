import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
tickers = ['GLD', 'BIL', 'EFA', 'VPL', 'SPY' ]

data = yf.download(tickers, start='2025-04-01', end='2025-06-30')
prices = data['Close']#takes closing price at end of trading day
print(data.shape)#sanity check
print(data.head())#sanity check
print(prices.head())
returns = prices.pct_change()
returns = returns.dropna()#pct_change has a null first value, fixed by dropna. 

portfolio_returns = returns[['GLD', 'BIL', 'EFA', 'VPL']]
spy_returns = returns['SPY']
weights = [.375, .1, .325, .20] #indexed accurately to reflect portfolio weight scaled to $1)
portfolio_daily = (portfolio_returns * weights).sum(axis=1)
#sharpe ratio formula: (return - risk free rate)/volatility

#risk free rate at the end of Q2 2025 was roughly 4.3%
risk_free_rate = 0.043 / 252

#avg daily return below
portfolio_avg_return = portfolio_daily.mean()
spy_avg_return = spy_returns.mean()

#volatility (stddev) for portfolio and spy
portfolio_vol = portfolio_daily.std()
spy_vol = spy_returns.std()

# sharpe ratio calculation, multiplied by the square root of 252 to annualize
portfolio_sharpe = (portfolio_avg_return - risk_free_rate) / portfolio_vol * (252**0.5)
spy_sharpe = (spy_avg_return - risk_free_rate) / spy_vol * (252**0.5)

print(f'Portfolio Sharpe Ratio: {portfolio_sharpe:.2f}')
print(f'SPY Sharpe Ratio: {spy_sharpe:.2f}')
if portfolio_sharpe < 1:
    print("My portfolio: Return per unit of risk is weak")
elif 1 <= portfolio_sharpe <= 2:
    print("My portfolio: Return per unit of risk is Strong")
if 2 < portfolio_sharpe <= 3:
    print("My portfolio: Return per unit of risk is Very Strong")
if 3 < portfolio_sharpe:
    print("My portfolio: Return per unit of risk is Excellent")
