from bs import d1
from utils import normal_cdf

def call_delta(S, K, T, r, sigma):
    """
    Black-Scholes delta for a call option
    """
    return normal_cdf(d1(S, K, T, r, sigma))
