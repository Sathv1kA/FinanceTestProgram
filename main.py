import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
plt.style.use('seaborn-v0_8')
import yfinance as yf
import tkinter as tk
from tkinter import Entry, END
def is_valid_ticker(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol)
    try:
        info = ticker.info
        if len(info) > 1 and "currentPrice" in info:
            return True
        else:
            return False
    except Exception:
        return False
def grabinfo(curstock,text_widget):
    temp = yf.Ticker(curstock)
    text_widget.delete("1.0", END)
    if is_valid_ticker(curstock) is False:
        print("Invalid Ticker Symbol")
        text_widget.insert(tk.END, "Invalid Ticker Symbol\n")
        return
    print(f"---{curstock}---")
    for actions in commands:
        print(f"{actions}: {temp.info[actions]}")
        text_widget.insert(tk.END, f"{actions}: {temp.info[actions]}\n")
    print(f"Price of {curstock} : {temp.info["currentPrice"]}")
    text_widget.insert(tk.END, f"Price of {curstock} : {temp.info['currentPrice']}\n")
def close_window(root):
        root.destroy()
def plot_stock_price(ticker_symbol,text_widget=None):
    if not is_valid_ticker(ticker_symbol):
        text_widget.delete("1.0", END)
        text_widget.insert(tk.END, "Invalid Ticker Symbol\n")
        print("Invalid Ticker Symbol")
        return
    grabinfo(ticker_symbol,text_widget)
    ticker = yf.Ticker(ticker_symbol)
    hist = ticker.history(period="1y")
    if hist.empty:
        print("No historical data available.")
        return
    plt.figure(figsize=(10, 5))
    plt.plot(hist.index, hist["Close"], label=f"{ticker_symbol} Close Price")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.title(f"{ticker_symbol} Price Over Last Year")
    plt.legend()
    plt.tight_layout()
    plt.show()
with open("stock.txt","r") as file:
    stocks=file.read().splitlines()
    file.close()
    pass
with open("commands.txt","r") as file:
    commands=file.read().splitlines()
    file.close()
    pass
