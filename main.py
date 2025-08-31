import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
plt.style.use('seaborn-v0_8')
import yfinance as yf
with open("stock.txt","r") as file:
    stocks=file.read().splitlines()
    file.close()
    pass
with open("commands.txt","r") as file:
    commands=file.read().splitlines()
    file.close()
    pass
with open("history.txt","a") as hist:
    hist.write(datetime.now().strftime("%Y-%m-%d Hours:%H: Mins:%M\n"))
    hist.close()
    pass
for curstock in stocks:
    temp = yf.Ticker(curstock)
    print(f"---{curstock}---")
    for actions in commands:
        print(f"{actions}: {temp.info[actions]}")
    print(f"Price of {curstock} : {temp.info["currentPrice"]}")
    hist = temp.history(period="6mo")
    plt.figure(figsize=(10, 5))
    plt.plot(hist.index, hist["Close"], label=f"{curstock} Close Price")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.title(f"{curstock} Price Over Time")
    plt.legend()
    plt.show()
    
