from bs_engine.bs import call_price, put_price
from bs_engine.utils import put_call_parity_black_scholes

def main():
    S = 26000.0
    K = 26000.0
    r = 0.06
    sigma = 0.15
    T = 30/365

    call = call_price(S, K, T, r, sigma)
    put = put_price(S, K, T, r, sigma)

    parity_gap = put_call_parity_black_scholes(S, K, T, r, call, put)

    print("Black-Scholes Put-Call Parity check")
    print("---------------------------------------")
    print(f"Call Price: {call:.6f}")
    print(f"Put Price: {put:.6f}")
    print(f"Parity Gap: {parity_gap:.10f}")

if __name__ == "__main__":
    main()
