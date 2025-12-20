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
