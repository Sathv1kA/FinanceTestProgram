import tkinter as tk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import yfinance as yf
with open("commands.txt","r") as file:
    commands=file.read().splitlines()
    file.close()
    pass
def is_valid_ticker(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol)
    try:
        info = ticker.info
        if len(info) > 1:
            return True
        else:
            return False
    except Exception:
        return False
def on_button_click():
    print( input_value )

def grabinfo(curstock):
    if is_valid_ticker(curstock) is False:
        print("Invalid Ticker Symbol")
        return
    temp = yf.Ticker(curstock)
    print(f"---{curstock}---")
    for actions in commands:
        print(f"{actions}: {temp.info[actions]}")
    print(f"Price of {curstock} : {temp.info["currentPrice"]}")

root= tk.Tk()
root.title("Finance Test Program")
root.geometry("400x300")

lbl=tk.Label(root,text="Finance Test Program")
lbl.grid()

btn=tk.Button(root,text="Run Program", command=lambda: grabinfo(entry_widget.get()))
btn.grid()

entry_widget = tk.Entry(root)
entry_widget.grid()
entry_widget.insert(0, "Default Text")
input_value = entry_widget.get()


root.mainloop()
