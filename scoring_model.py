import pandas as pd

def compute_score(df):
    """
    Assigns credit score (0–1000) based on features:
    - More deposits, repays → higher score
    - More borrows, liquidations → lower score
    """

    # Start with base score = 500
    df["credit_score"] = 500

    # Positive behavior
    df["credit_score"] += df["deposits"] * 10
    df["credit_score"] += df["repays"] * 15
    df["credit_score"] += df["repay_ratio"] * 50

    # Negative behavior
    df["credit_score"] -= df["borrows"] * 5
    df["credit_score"] -= df["liquidations"] * 50

    # Clamp scores between 0 and 1000
    df["credit_score"] = df["credit_score"].clip(0, 1000)

    return df
