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

def _d1_black76(F, K, T, sigma):
    return (math.log(F / K) + 0.5 * sigma * sigma * T) / (sigma * math.sqrt(T))


def _d2_black76(d1, T, sigma):
    return d1 - sigma * math.sqrt(T)


def black76_call_delta(F, K, T, r, sigma):
    """
    Delta of a call option under Black-76
    (delta w.r.t futures price)
    """
    if T <= 0:
        return 1.0 if F > K else 0.0

    d1 = _d1_black76(F, K, T, sigma)
    return math.exp(-r * T) * normal_cdf(d1)


def black76_call_gamma(F, K, T, r, sigma):
    """
    Gamma of a call option under Black-76
    """
    if T <= 0:
        return 0.0

    d1 = _d1_black76(F, K, T, sigma)
    return (
        math.exp(-r * T)
        * normal_pdf(d1)
        / (F * sigma * math.sqrt(T))
    )


def black76_call_theta(F, K, T, r, sigma):
    """
    Theta of a call option under Black-76
    (per year)
    """
    if T <= 0:
        return 0.0

    d1 = _d1_black76(F, K, T, sigma)
    d2 = _d2_black76(d1, T, sigma)

    term1 = -(
        math.exp(-r * T)
        * F
        * normal_pdf(d1)
        * sigma
        / (2 * math.sqrt(T))
    )

    term2 = r * math.exp(-r * T) * (
        F * normal_cdf(d1) - K * normal_cdf(d2)
    )

    return term1 + term2
