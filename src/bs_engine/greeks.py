import math
from bs_engine.bs import d1
from bs_engine.utils import normal_cdf, normal_pdf

def call_delta(S, K, T, r, sigma):
    """
    Black-Scholes delta for a call option
    """
    return normal_cdf(d1(S, K, T, r, sigma))

def call_gamma(S, K, T, r, sigma):
    """
    Black-Scholes gamma for a call option
    """
    return normal_pdf(d1(S, K, T, r, sigma)) / (S * sigma * math.sqrt(T))

def call_theta(S, K, T, r, sigma):
    """
    Black-Scholes theta for a call option (per day)
    """
    D1 = d1(S, K, T, r, sigma)
    D2 = D1 - sigma*math.sqrt(T)

    term1 = - (S * normal_pdf(D1) * sigma) / (2 * math.sqrt(T))
    term2 = - r * K * math.exp(-r * T) * normal_cdf(D2)

    return (term1+term2) / 365
