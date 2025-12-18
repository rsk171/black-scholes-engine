from bs_engine.bs import call_price

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
