# Aave Credit Scoring

**Credit scoring system for wallets interacting with the Aave V2 protocol**  
Generates credit scores (0–1000) based on historical DeFi transaction behavior such as deposits, borrows, repayments, and liquidations.

---

## Table of Contents
- [Problem Statement](#problem-statement)  
- [Approach](#approach)  
- [Folder Structure](#folder-structure)  
- [How to Run](#how-to-run)  
- [Requirements](#requirements)  
- [Output](#output)

---

## Problem Statement

We are provided with ~100K raw transaction-level data from the **Aave V2 protocol**, where each record represents wallet actions:  
- `deposit`  
- `borrow`  
- `repay`  
- `redeemunderlying`  
- `liquidationcall`

**Goal**: Build a robust machine learning-based scoring system that assigns a **credit score (0–1000)** for each wallet.  
- **High scores** → Reliable and responsible usage  
- **Low scores** → Risky, bot-like, or exploitative behavior  

---

## Approach

### Feature Engineering
- Total transactions per

