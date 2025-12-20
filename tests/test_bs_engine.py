import math
from bs_engine.bs import call_price
from bs_engine.implied_vol import implied_vol_call
from bs_engine.greeks import call_delta, call_gamma, call_theta

# Common test inputs
S = 26000
K = 26400
T = 10 / 365
r = 0.06

def test_call_price_increases_with_volatility():
    price_low_vol = call_price(S, K, T, r, 0.15)
    price_high_vol = call_price(S, K, T, r, 0.30)
    assert price_high_vol > price_low_vol

def test_implied_volatility_recovers_original_vol():
    true_sigma = 0.20
    price = call_price(S, K, T, r, true_sigma)
    recovered_iv = implied_vol_call(price, S, K, T, r)
    assert abs(recovered_iv - true_sigma) < 1e-4

def test_delta_bounds():
    delta = call_delta(S, K, T, r, 0.20)

    assert 0.0 <= delta <= 1.0

def test_gamma_positive_theta_negative():
    gamma = call_gamma(S, K, T, r, 0.20)
    theta = call_theta(S, K, T, r, 0.20)

    assert gamma > 0
    assert theta < 0
