import tkinter as tk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import yfinance as yf
from tkinter import Entry, END
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

def grabinfo(curstock):
    text_widget.delete("1.0", END)
    if is_valid_ticker(curstock) is False:
        print("Invalid Ticker Symbol")
        text_widget.insert(tk.END, "Invalid Ticker Symbol\n")
        return
    temp = yf.Ticker(curstock)
    print(f"---{curstock}---")
    for actions in commands:
        print(f"{actions}: {temp.info[actions]}")
        text_widget.insert(tk.END, f"{actions}: {temp.info[actions]}\n")
    print(f"Price of {curstock} : {temp.info["currentPrice"]}")
    text_widget.insert(tk.END, f"Price of {curstock} : {temp.info['currentPrice']}\n")
def close_window():
        root.destroy()
root= tk.Tk()
root.title("Finance Test Program")
root.geometry("600x600")
lbl=tk.Label(root,text="Finance Test Program")
lbl.grid(row=0,column=0)
text_widget = tk.Text(root, width=40, height=10, wrap=tk.WORD, font=("Times New Roman", 10))
text_widget.grid(row=3, column=0, padx=10, pady=10)
btn=tk.Button(root,text="Run Program", command=lambda: grabinfo(entry_widget.get()))
btn.grid(row=2,column=0)
close_button = tk.Button(root, text="Close Window", command=close_window)
close_button.grid(row=2, column=1, padx=10, pady=10)
entry_widget = tk.Entry(root)
entry_widget.grid(row=1, column=0, padx=10, pady=10)
entry_widget.insert(0, "Default Text")


root.mainloop()
