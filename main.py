import yfinance as yf
import numpy as np
import warnings
import methods
import plots
warnings.filterwarnings("ignore", message=".*inplace keyword.*")

ticker=input("Enter the stock ticker symbol: ").upper()
prices = yf.download(ticker, progress=False, start='2020-01-01')['Close'].squeeze()
current_price=float(prices.iloc[-1])
returns = np.log(prices / prices.shift(1)).iloc[1:]
print(f"Current Price of {ticker}: ${current_price:.2f}")
strike_price=float(input(f"Enter strike price for {ticker}: "))
time_to_maturity=float(input("Enter time to maturity in years: "))
risk_free_rate=yf.download('^IRX', progress=False)['Close'].squeeze().iloc[-1]/100
volatility=returns.std()*np.sqrt(252)

call_price, put_price = methods.calculate_option_prices(current_price, strike_price, risk_free_rate, volatility, time_to_maturity)
print(f"Call Option Price: ${call_price:.2f}")
print(f"Put Option Price: ${put_price:.2f}")

call_price_mc, put_price_mc, mc_S_T = methods.monte_carlo_option_pricing(current_price, strike_price, risk_free_rate, volatility, time_to_maturity)
print(f"Monte Carlo Call Option Price: ${call_price_mc:.2f}")
print(f"Monte Carlo Put Option Price: ${put_price_mc:.2f}")

plots.plot_hist(mc_S_T, current_price, strike_price, ticker)

