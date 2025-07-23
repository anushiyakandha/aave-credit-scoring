from preprocess import extract_features
from scoring_model import compute_score
import os

def main():
    # Input file path
    input_path = r"D:\DataScience\aave_credit_scoring\data\user_wallet_transaction.json"

    # Output file path (relative path)
    output_path = "../output/wallet_scores.csv"

    # Debug: check if input file exists
    print("Checking file exists:", os.path.exists(input_path))
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"File not found: {input_path}")

    print("Step 1: Extracting features...")
    df = extract_features(input_path)
    print(f"Extracted features for {len(df)} wallets")

    print("Step 2: Computing credit scores...")
    df = compute_score(df)

    print("Step 3: Saving results...")

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save scores
    df[["wallet", "credit_score"]].to_csv(output_path, index=False)
    print(f"✅ Scores saved to {output_path}")

if __name__ == "__main__":
    main()

