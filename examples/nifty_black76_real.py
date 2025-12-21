import json
from bs_engine.nse_data import get_nifty_option_chain, parse_nifty_data
from bs_engine.implied_vol import implied_vol_call_black76
from bs_engine.greeks import (
    black76_call_delta,
    black76_call_gamma,
    black76_call_theta,
)


def load_sample_data():
    with open("data/nifty_sample.json", "r") as f:
        return json.load(f)


def main():
    try:
        data = get_nifty_option_chain()
        print("Fetched live NSE data")
    except Exception:
        print("Live NSE blocked, using sample data")
        data = load_sample_data()

    # Parse data
    spot, futures_price, options = parse_nifty_data(data)

    r = 0.06          # risk-free rate
    T = 7 / 365       # time to expiry (7 days)

    print(f"NIFTY Spot: {spot}")
    print(f"NIFTY Futures: {futures_price}")
    print("-" * 50)

    for opt in options:
        K = opt["strike"]
        price = opt["price"]

        # ---- Black-76 implied volatility ----
        iv = implied_vol_call_black76(
            market_price=price,
            F=futures_price,
            K=K,
            T=T,
            r=r,
        )

        # ---- Black-76 Greeks ----
        delta = black76_call_delta(futures_price, K, T, r, iv)
        gamma = black76_call_gamma(futures_price, K, T, r, iv)
        theta = black76_call_theta(futures_price, K, T, r, iv)

        print(f"Strike {K} | Market Price {price}")
        print(
            f"  IV: {iv:.3f}, "
            f"Delta: {delta:.3f}, "
            f"Gamma: {gamma:.6f}, "
            f"Theta: {theta:.3f}"
        )
        print()


if __name__ == "__main__":
    main()
