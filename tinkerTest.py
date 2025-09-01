import tkinter as tk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import yfinance as yf
from tkinter import Entry, END
import main

root= tk.Tk()
root.title("Finance Test Program")
root.geometry("600x600")

lbl=tk.Label(root,text="Finance Test Program")
lbl.grid(row=0,column=0)

infodis = tk.Text(root, width=40, height=10, wrap=tk.WORD, font=("Times New Roman", 10))
infodis.grid(row=3, column=0, padx=10, pady=10)

btn=tk.Button(root,text="Run Program", command=lambda: main.grabinfo(entry_widget.get(),infodis))
btn.grid(row=2,column=0)

close_button = tk.Button(root, text="Close Window", command=lambda: main.close_window(root))
close_button.grid(row=2, column=1, padx=10, pady=10)

# Button to plot stock price over last year
plot_button = tk.Button(root, text="Plot Price (1 Year)", command=lambda: main.plot_stock_price(entry_widget.get(),infodis))
plot_button.grid(row=2, column=2, padx=10, pady=10)

entry_widget = tk.Entry(root)
entry_widget.grid(row=1, column=0, padx=10, pady=10)
entry_widget.insert(0, "Default Text")


root.mainloop()
