import math

def normal_cdf(x: float) -> float:
    """
    Standard normal cumulative distribution function N(x)
    """
    return 0.5 * (1.0 + math.erf(x/math.sqrt(2.0)))
