import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
ticker = 'SPY'
data = yf.download(ticker, start='2025-01-01', end='2025-12-31')
prices = data['Close'] #squeeze forces it into a clean Series but it is not needed and makes no change now
print(data.shape)  #sanity check that we got more than 1 row
#daily return/volatility
daily_returns = prices.pct_change().dropna()
avg_daily_return = daily_returns.mean().item()  #.item() pulls single number out instead of forming a float
daily_volatility = daily_returns.std().item() #spy volatility is crucial to premium pricing

#option variables
current_price = prices.iloc[-1].item()
strike_price = current_price * 1.05 #option starts out of the money
#
days_to_expiry = 30
risk_free_rate = 0.043 / 252
simulations = 10000

#simulations
final_prices = []

for i in range(simulations): #for every values in all 10000 loops
    price = current_price #resets price every sim
    for day in range(days_to_expiry):
        random_shock = np.random.normal(0, 1) #pull random number from bell curve for varability
        daily_move = avg_daily_return + daily_volatility * random_shock #ties in all for a realisitc market sim
        price = price * (1 + daily_move)
    final_prices.append(price)

#option payoffs
final_prices = np.array(final_prices)
payoffs = np.maximum(final_prices - strike_price, 0) 
#this is the in-the-money of the calculation (or out of the money).
#to make this a PUT OPTION pricer, do strike_price-final_prices.

#discount back to today
option_price = np.mean(payoffs) * np.exp(-risk_free_rate * days_to_expiry)

print(f'Current SPY Price: ${current_price:.2f}')
print(f'Strike Price: ${strike_price:.2f}')
print(f'Estimated Call Option Price: ${option_price:.2f}')

# plot
plt.figure(figsize=(12, 6))
plt.hist(final_prices, bins=60, color='black', alpha=0.65)
plt.axvline(strike_price, color='red', linestyle='--', label='Strike Price')
plt.axvline(current_price, color='green', linestyle='--', label='Current Price')
plt.title('Monte Carlo Simulation: SPY Price Distribution at Expiry')
plt.xlabel('Price at Expiry')
plt.ylabel('Frequency')
plt.legend()
plt.show()