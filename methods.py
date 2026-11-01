import numpy as np
import scipy.stats as stats

def calculate_aux_var(S,K,r,sigma,T):
    d1=(np.log(S/K)+(r+0.5*sigma**2)*T)/(sigma*np.sqrt(T))
    d2=d1-sigma*np.sqrt(T)
    return d1, d2

def calculate_option_prices(S, K, r, sigma, T):
    d1,d2 =calculate_aux_var(S, K, r, sigma, T)
    call_price=S*stats.norm.cdf(d1)-K*np.exp(-r*T)*stats.norm.cdf(d2)
    put_price=K*np.exp(-r*T)*stats.norm.cdf(-d2)-S*stats.norm.cdf(-d1)
    return call_price, put_price

def monte_carlo_option_pricing(S, K, r, sigma, T, num_simulations=10000):
    z=np.random.standard_normal(num_simulations)
    S_T=S*np.exp((r-0.5*sigma**2)*T+sigma*np.sqrt(T)*z)
    call_payoffs=np.maximum(S_T-K,0)
    put_payoffs=np.maximum(K-S_T,0)
    call_price=np.exp(-r*T)*np.mean(call_payoffs)
    put_price=np.exp(-r*T)*np.mean(put_payoffs)
    return call_price, put_price, S_T


    