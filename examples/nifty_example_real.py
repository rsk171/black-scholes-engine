import json
from bs_engine.nse_data import get_nifty_option_chain, parse_nifty_data
from bs_engine.implied_vol import implied_vol_call
from bs_engine.greeks import call_delta, call_gamma, call_theta


def load_sample_data():
    with open("data/nifty_sample.json", "r") as f:
        return json.load(f)


def main():
    try:
        data = get_nifty_option_chain()
        print("Fetched live NSE data")
    except Exception as e:
        print("Live NSE blocked, using sample data")
        data = load_sample_data()

    spot, _, options = parse_nifty_data(data)

    r = 0.06
    T = 7 / 365

    print("NIFTY Spot:", spot)
    print("-" * 40)

    for opt in options:
        K = opt["strike"]
        price = opt["price"]

        iv = implied_vol_call(price, spot, K, T, r)
        delta = call_delta(spot, K, T, r, iv)
        gamma = call_gamma(spot, K, T, r, iv)
        theta = call_theta(spot, K, T, r, iv)

        print(f"Strike {K} | Price {price}")
        print(f"  IV: {iv:.3f}, Delta: {delta:.3f}, Gamma: {gamma:.6f}, Theta: {theta:.3f}")
        print()


if __name__ == "__main__":
    main()
