import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
tickers = ['GLD', 'BIL', 'EFA', 'VPL', 'SPY' ]

data = yf.download(tickers, start='2025-04-01', end='2025-06-30')
prices = data['Close']
print(data.shape)
print(data.head())
print(prices.head())
returns = prices.pct_change()
returns = returns.dropna()

portfolio_returns = returns[['GLD', 'BIL', 'EFA', 'VPL']]
spy_returns = returns['SPY']


weights = [.375, .1, .325, .20]
portfolio_daily = (portfolio_returns * weights).sum(axis=1)

portfolio_cumulative = (1 + portfolio_daily).cumprod()
spy_cumulative = (1 + spy_returns).cumprod()

plt.figure(figsize=(12, 6))
plt.plot(portfolio_cumulative, label='My Portfolio')
plt.plot(spy_cumulative, label='SPY')
plt.title('My Portfolio vs SPY')
plt.xlabel('Date')
plt.ylabel('Growth of $1')
plt.legend()
plt.show()