import csv
import os
import json
import matplotlib.pyplot as plt

from bs_engine.nse_data import get_nifty_option_chain, parse_nifty_data
from bs_engine.implied_vol import implied_vol_call_black76

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

    # Using spot as futures fallback (explicit choice)
    spot, futures_price, options = parse_nifty_data(data)

    r = 0.06
    T = 7/365

    strikes = []
    ivs = []
    prices = []

    print("NIFTY Spot:", spot)
    print("NIFTY Futures:", futures_price)
    print("-"*40)
    print("Strike | Market Price  | Black-76 IV")
    print("-"*40)

    for opt in options:
        K = opt["strike"]
        price = opt["price"]

        try:
            iv = implied_vol_call_black76(
                market_price = price,
                F = futures_price,
                K = K,
                T = T,
                r = r,
            )

            strikes.append(K)
            prices.append(price)
            ivs.append(iv)

            print(f"{K:6} | {price: 13.2f} | {iv:.4f}")
        except Exception:
            print(f"{K:6} | {price: 13.2f} | IV error")

    # ---- Plotting layer ----
    if strikes:
        plt.figure(figsize=(9, 5))
        plt.plot(strikes, ivs, marker = "o")
        plt.xlabel("Strike")
        plt.ylabel("Implied Volatility")
        plt.title("NIFTY Volatility Skew (Black-76)")
        plt.grid(True)
        plt.show()

    # ---- CSV export ----
    os.makedirs("data/derived", exist_ok=True)
    csv_path = "data/derived/nifty_volatility_skew_black76.csv"

    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["strike", "market_price", "implied_vol"])

        for K, price, iv in zip(strikes, prices, ivs):
            writer.writerow([K, price, iv])

    print(f"\nVolatility skew exported to {csv_path}")

if __name__ == "__main__":
    main()
