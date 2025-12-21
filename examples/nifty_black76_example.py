"""
Example: Pricing NIFTY index options using Black-76

Why Black-76?
- Indian index options are based on futures, not spot
- Hedging is done using index futures
- Hence Black-76 is the correct model
"""

from bs_engine.black_76 import black76_call, black76_put


def main():

    F = 26000.0        # NIFTY futures price
    r = 0.06           # Risk-free rate (6% annualized)
    sigma = 0.15       # Implied volatility (15%)
    T = 30 / 365       # 30 days to expiry

    strikes = [25600, 25800, 26000, 26200, 26400]

    print("NIFTY Black-76 Option Pricing")
    print("----------------------------------")
    print(f"Futures Price (F): {F}")
    print(f"Risk-free Rate (r): {r}")
    print(f"Volatility (σ): {sigma}")
    print(f"Time to Expiry (T): {T:.4f} years\n")

    for K in strikes:
        call_price = black76_call(F, K, T, r, sigma)
        put_price = black76_put(F, K, T, r, sigma)

        print(f"Strike {K}")
        print(f"  Call Price: {call_price:.2f}")
        print(f"  Put  Price: {put_price:.2f}\n")


if __name__ == "__main__":
    main()
