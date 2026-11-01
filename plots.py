import matplotlib.pyplot as plot
import matplotlib.ticker as mtick

def plot_hist(s_t, current_price, strike_price, ticker):
    plot.figure(num='Monte Carlo Simulation of Stock Price', figsize=(9, 6))
    plot.style.use('bmh')
    plot.hist(s_t, bins=100, color='#660033', label='Simulated Stock Prices at Maturity')
    plot.axvline(x=current_price, color='#fcba03', linestyle='--', label=f'Current Price: ${current_price:.2f}')
    plot.axvline(x=strike_price, color='#d66d22', linestyle='--', label=f'Strike Price: ${strike_price:.2f}')
    plot.xlabel('Stock Price at Maturity', fontsize=14)
    plot.ylabel('Number of Simulations', fontsize=14)
    plot.legend()
    plot.title(f"Monte Carlo Simulation of {ticker} Stock Price at Maturity", fontsize=16)
    plot.savefig(f'monte_carlo_simulation_{ticker}.png', dpi=150)
    plot.show()