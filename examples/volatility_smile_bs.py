import json
from bs_engine.nse_data import get_nifty_option_chain, parse_nifty_data
from bs_engine.implied_vol import implied_vol_call

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

    spot, _, options = parse_nifty_data(data)

    r = 0.06
    T = 7/365 # fixed expiry for volatility smile

    print("NIFTY Spot:", spot)
    print("-"*40)
    print("Strike | Market Price | Implied Vol")
    print("-"*40)

    for opt in options:
        K = opt["strike"]
        price = opt["price"]

        try:
            iv = implied_vol_call(price, spot, K, T, r)
            print(f"{K:6} | {price: 13.2f} | {iv:.4f}")
        except Exception:
            print(f"{K:6} | {price: 13.2f} | IV error")

if __name__ == "__main__":
    main()
