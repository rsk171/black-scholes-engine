from bs_engine.bs import call_price, put_price

def main():
    S = 26000.0
    K = 26000.0
    r = 0.06
    sigma = 0.15
    T = 30/365

    call = call_price(S, K, T, r, sigma)
    put = put_price(S, K, T, r, sigma)

    print("Black-Scholes Call & Put Demo")
    print("------------------------------------")
    print(f"Spot: {S}")
    print(f"Strike: {K}")
    print(f"Call: {call:.4f}")
    print(f"Put: {put: .4f}")


if __name__ == "__main__":
    main()
