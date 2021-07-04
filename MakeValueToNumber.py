import requests
import bs4
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
import datetime
import test
import numpy as np
import pandas as pd
cnt = 0
TransferMarket = list()
wage_per_month = list()
youth_value = list()
Game_value = list()
height = list()
df = pd.read_csv("data_newnew_2014.csv")
TransferMarketValue = df["TransferMarket Value"].to_numpy()
wage = df["Wage"].to_numpy()
youthValue = df["youth_value"].to_numpy()
football_value = df["Game Value"].to_numpy()
Height = df["Height"]
j=len(TransferMarketValue)
for i in range(j):
    if (TransferMarketValue[i] != TransferMarketValue[i]):
        z=""
        TransferMarket.append(z)
    else:
         if TransferMarketValue[i].find("Th") != -1:
           z = TransferMarketValue[i].split("Th", 1)[0]
           z = z.split("€", 1)[1]
           TransferMarket.append(float(z)*1000)
         if TransferMarketValue[i].find("m") != -1:
            z = TransferMarketValue[i].split("m", 1)[0]
            z = z.split("€", 1)[1]
            TransferMarket.append(float(z)*1000000)
for i in range(j):
    try:
        if football_value[i].find("K") != -1:
           z = football_value[i].split("K", 1)[0]
           z = z.split("£", 1)[1]
           Game_value.append(float(z)*1000)
        elif football_value[i].find("M") != -1:
            z = football_value[i].split("M", 1)[0]
            z = z.split("£", 1)[1]
            Game_value.append(float(z)*1000000)
        else:
            z=" "
            Game_value.append(z)
    except:
        print("faild")
        z= " "
        Game_value.append(z)
for i in range(j):
    try:
           z = wage[i].split("K", 1)[0]
           z = z.split("£", 1)[1]
           wage_per_month.append(float(z)*4000)
    except:
        print("faild")
        z= " "
        wage_per_month.append(z)
for i in range(j):
    try:
        z= youthValue[i]
        youth_value.append(float(z)*1000000)
    except:
        print("faild")
        z= " "
        youth_value.append(z)
for i in range(j):
    z = Height[i].split("cm", 1)[0]
    height.append(z)
# index = TransferMarketValue[1].find("Th")
# z = TransferMarketValue[1].split("Th", 1)[0] + 'K'
# z = z.split("€", 1)[1]

print(Game_value)
print(youth_value)
print(wage_per_month)
print(TransferMarketValue)
print(len(Game_value))
print(len(youth_value))
print(len(height))
print(len(wage_per_month))
print(len(TransferMarket))
df["Wage"] = wage_per_month
df["youth_value"] = youth_value
df["TransferMarket Value"] = TransferMarket
df["Game Value"] = Game_value

df["Height"] = height
# del df["TransferMarket Value"]
# del df["Wage"]
# del df["youth_value"]
# del df["Game Value"]

df.to_csv("data_newnew_2014.csv")