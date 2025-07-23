import pandas as pd
import json

def extract_features(file_path):
    """
    Reads raw transaction JSON and generates wallet-level features:
    - total transactions
    - counts of deposits/borrows/repays/redeems/liquidations
    - net borrow vs repay balance
    """

    print(f"Loading JSON file: {file_path}")

    # Load JSON
    with open(file_path, "r") as f:
        data = json.load(f)

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Rename userWallet → wallet
    if "userWallet" in df.columns:
        df.rename(columns={"userWallet": "wallet"}, inplace=True)

    # Validate required columns
    if "wallet" not in df.columns or "action" not in df.columns:
        raise ValueError("JSON still missing required columns: 'wallet' and 'action'")

    # Create features
    features = df.groupby("wallet").agg(
        total_tx=("action", "count"),
        deposits=("action", lambda x: (x == "deposit").sum()),
        borrows=("action", lambda x: (x == "borrow").sum()),
        repays=("action", lambda x: (x == "repay").sum()),
        redeems=("action", lambda x: (x == "redeemunderlying").sum()),
        liquidations=("action", lambda x: (x == "liquidationcall").sum())
    ).reset_index()

    # Repay ratio (avoid divide by zero)
    features["repay_ratio"] = features["repays"] / features["borrows"].replace(0, 1)

    return features


