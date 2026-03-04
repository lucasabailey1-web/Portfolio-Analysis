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
weights = [.375, .1, .325, .20] #portfolio weight scaled to $1)
portfolio_daily = (portfolio_returns * weights).sum(axis=1)
portfolio_cumulative = (1 + portfolio_daily).cumprod()
spy_cumulative = (1 + spy_returns).cumprod()

rolling_vol_portfolio = portfolio_daily.rolling(30).std() * (252**0.5) #TRADING DAYS/YEAR
rolling_vol_spy = spy_returns.rolling(30).std() * (252**0.5)
#Historical volatility= sqrt(time) is how volatility is scaled
plt.figure(figsize=(12, 6))
plt.plot(rolling_vol_portfolio, label='My Portfolio', color='blue')
plt.plot(rolling_vol_spy, label='SPY', color='orange')
plt.title('Rolling 30-Day Volatility')
plt.xlabel('Date')
plt.ylabel('Annualized Volatility')
plt.legend()
plt.show()