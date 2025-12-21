import math
from .utils import normal_cdf


def _d1(F, K, T, sigma):
    """
    d1 for Black-76
    F     : Futures price
    K     : Strike price
    T     : Time to expiry (in years)
    sigma : Volatility (annualized)
    """
    return (math.log(F / K) + 0.5 * sigma * sigma * T) / (sigma * math.sqrt(T))


def _d2(d1, T, sigma):
    """
    d2 for Black-76
    """
    return d1 - sigma * math.sqrt(T)


def black76_call(F, K, T, r, sigma):
    """
    Black-76 Call Option Price

    F     : Futures price
    K     : Strike price
    T     : Time to expiry (years)
    r     : Risk-free rate (annualized)
    sigma : Volatility (annualized)
    """
    if T <= 0:
        return max(F - K, 0.0)

    d1 = _d1(F, K, T, sigma)
    d2 = _d2(d1, T, sigma)

    discounted_factor = math.exp(-r * T)

    return discounted_factor * (
        F * normal_cdf(d1) - K * normal_cdf(d2)
    )


def black76_put(F, K, T, r, sigma):
    """
    Black-76 Put Option Price

    F     : Futures price
    K     : Strike price
    T     : Time to expiry (years)
    r     : Risk-free rate (annualized)
    sigma : Volatility (annualized)
    """
    if T <= 0:
        return max(K - F, 0.0)

    d1 = _d1(F, K, T, sigma)
    d2 = _d2(d1, T, sigma)

    discounted_factor = math.exp(-r * T)

    return discounted_factor * (
        K * normal_cdf(-d2) - F * normal_cdf(-d1)
    )
