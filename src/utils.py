# src/utils.py
import pandas as pd
import matplotlib.pyplot as plt

def load_oil_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=['Date'], dayfirst=True)
    df.sort_values("Date", inplace=True)
    return df

def plot_price_trend(df: pd.DataFrame):
    plt.figure(figsize=(12, 5))
    plt.plot(df['Date'], df['Price'], label='Brent Oil Price', color='navy')
    plt.title("Brent Oil Price Over Time")
    plt.xlabel("Date")
    plt.ylabel("Price (USD/barrel)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
