import math

def normal_cdf(x: float) -> float:
    """
    Standard normal cumulative distribution function N(x)
    """
    return 0.5 * (1.0 + math.erf(x/math.sqrt(2.0)))

def normal_pdf(x: float) -> float:
    """
    Standard normal probability density function N'(x)
    """
    return (1 / math.sqrt(2 * math.pi)) * math.exp(-0.5 * x * x)

def put_call_parity_black_scholes(S, K, T, r, call_price, put_price):
    """
    Put-Call Parity check for Black-Scholes (spot-based)

    Returns:
        parity_gap = C - P - (S - K * e^(-rT))

    if parity_gap ≈ 0, no arbitrage holds.
    """
    return call_price - put_price - (S - K * math.exp(-r*T))
