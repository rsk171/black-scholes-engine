import time
import requests


NSE_OPTION_CHAIN_URL = "https://www.nseindia.com/api/option-chain-v3?type=Indices&symbol=NIFTY&expiry=30-Dec-2025"
NSE_HOME_URL = "https://www.nseindia.com"


def get_nifty_option_chain():
    session = requests.Session()

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept": "application/json,text/plain,*/*",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.nseindia.com/api/option-chain",
        "Connection": "keep-alive",
    }

    # Step 1: Warm up session (VERY IMPORTANT)
    session.get(NSE_HOME_URL, headers=headers, timeout=10)

    # Small delay helps avoid empty response
    time.sleep(1)

    # Step 2: Fetch option chain
    response = session.get(
        NSE_OPTION_CHAIN_URL,
        headers=headers,
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    if not data:
        raise ValueError("Empty response from NSE (likely blocked). Try again later.")

    return data


def parse_nifty_data(data):
    if "records" not in data:
        raise ValueError("Invalid NSE response: 'records' missing")

    records = data["records"]
    spot_price = records.get("underlyingValue")

    options = []

    for entry in records.get("data", []):
        strike = entry.get("strikePrice")
        ce = entry.get("CE")

        if ce and ce.get("lastPrice", 0) > 0:
            options.append({
                "type": "CE",
                "strike": strike,
                "price": ce["lastPrice"],
                "expiry": ce.get("expiryDate"),
            })

    futures_price = spot_price  # fallback: treating spot as futures
    return spot_price, futures_price, options
