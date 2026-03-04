#starting with the portfolio VS SPY code(drawdown begins at ln 33)
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


weights = [.375, .1, .325, .20] #indexed accurately to reflect portfolio weight scaled to $1)
portfolio_daily = (portfolio_returns * weights).sum(axis=1)

portfolio_cumulative = (1 + portfolio_daily).cumprod()
spy_cumulative = (1 + spy_returns).cumprod()


#now beginning drawdown
rolling_max = portfolio_cumulative.cummax()
drawdown = (portfolio_cumulative - rolling_max) / rolling_max
rolling_SPY = spy_cumulative.cummax()
spydrawdown=(spy_cumulative - rolling_SPY) / rolling_SPY
plt.figure(figsize=(12, 6))
plt.fill_between(drawdown.index, drawdown, 0, color='green', alpha=0.7, label = 'My Portfolio')
plt.fill_between(spydrawdown.index, spydrawdown, 0, color = 'pink', alpha=0.3, label = 'SPY return')
plt.title('Portfolio Drawdown')
plt.xlabel('Date') 
plt.ylabel('Drawdown %')
plt.legend()
plt.show()