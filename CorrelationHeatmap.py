import seaborn as sns
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
correlation = returns[['GLD', 'BIL', 'EFA', 'VPL', 'SPY']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
#Correlation = covariance(A,B) / (StdDev(A) × StdDev(B))
#covariance(x,y)=sum(chosen x minus avg x)*(chosen y minus average y) all over N-1
plt.title('Asset Correlation Heatmap')
plt.tight_layout()
plt.show()