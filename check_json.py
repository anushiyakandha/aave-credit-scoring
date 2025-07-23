import json

file_path = r"D:\DataScience\aave_credit_scoring\data\user_wallet_transaction.json"

with open(file_path, "r") as f:
    data = json.load(f)

# Show structure
if isinstance(data, dict):
    print("Top-level keys:", data.keys())
    # If nested, print first key's data
    first_key = next(iter(data))
    print("First key data type:", type(data[first_key]))
    if isinstance(data[first_key], list):
        print("First record inside list:", data[first_key][0])
elif isinstance(data, list):
    print("First record in list:", data[0])
else:
    print("Unknown structure:", type(data))

