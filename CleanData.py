import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data = pd.read_csv("data_after_clean 2.csv")
data['Game Rating'].fillna(68, inplace=True)
data['Fotball Critic rating'].fillna(68, inplace=True)
Game_Rating = data["Game Rating"]
Fotball_Critic_rating = data["Fotball Critic rating"]
predicted_rate = data["predicted_rate"]
label = list()
rate_avg = list()
j = len(Game_Rating)
for i in range(j):
    if Fotball_Critic_rating[i] != Fotball_Critic_rating[i]  or Fotball_Critic_rating[i]== 99:
        x= Game_Rating[i]
    elif Game_Rating[i] != Game_Rating[i]:
        x = Fotball_Critic_rating[i]
    else:
       x = (Fotball_Critic_rating[i] + Game_Rating[i])/2
    rate_avg.append(x)
data["rate avg"] = rate_avg
ratio_predicted = list()
for i in range(j):
    z = rate_avg[i]/predicted_rate[i]
    ratio_predicted.append(z)
data["ratio predicted"] = ratio_predicted
ratio = data["ratio predicted"]
j= len(ratio)
for i in range(j):
    if ratio[i] > 0.93:
        label.append(1)
    else:
        label.append(0)
data["label"] = label
# data.Position = pd.Categorical(data.Position)
# data['numeric position'] = data.Position.cat.codes
data.to_csv("data_after_clean.csv")