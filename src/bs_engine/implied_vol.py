from bs_engine.bs import call_price
from .black_76 import black76_call


def implied_vol_call(
    market_price: float,
    S: float,
    K: float,
    T: float,
    r: float,
    tol: float = 1e-6,
    max_iter: int = 100
) -> float:
    """
    Compute implied volatility for a call option using binary search.
    """

    low = 0.0001  # almost zero volatility
    high = 5.0    # 500% volatility (safe upper bound)

    for _ in range(max_iter):
        mid = (low + high)/2
        price = call_price(S, K, T, r, mid)

        if price > market_price:
            high = mid
        else:
            low = mid

    return (low+high)/2

def implied_vol_call_black76(
    market_price,
    F,
    K,
    T,
    r,
    tol=1e-6,
    max_iter=100,
):
    """
    Implied volatility for a CALL option using Black-76

    market_price : Observed option price
    F             : Futures price
    K             : Strike price
    T             : Time to expiry (years)
    r             : Risk-free rate
    """

    if market_price <= 0:
        return 0.0

    # Volatility bounds
    low = 1e-6
    high = 5.0

    for _ in range(max_iter):
        mid = 0.5 * (low + high)
        price = black76_call(F, K, T, r, mid)

        if abs(price - market_price) < tol:
            return mid

        if price > market_price:
            high = mid
        else:
            low = mid

    return mid
