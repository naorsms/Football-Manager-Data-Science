import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import array
old = pd.read_csv("2014 (2).csv")
Fotball_Critic_rating= old["Fotball Critic rating"]
Game_Rating = old["Game Rating"]
G_values = old["Game Value"]
T_values = old["TransferMarket Value"]
predicted_rate = old["predicted_rate"]
Foot = old["Foot"]
Astrology = old["Astrology"]
astro = list()
value_avg = list()
rate_avg = list()
ratio_predicted = list()
label = list()
foot = list()
j = len(G_values)
for i in range(j):
    if Fotball_Critic_rating[i] != Fotball_Critic_rating[i]  or Fotball_Critic_rating[i]== 99:
        x= Game_Rating[i]
    elif Game_Rating[i] != Game_Rating[i]:
        x = Fotball_Critic_rating[i]
    else:
       x = (Fotball_Critic_rating[i] + Game_Rating[i])/2
    rate_avg.append(x)
# old["value_avg"] = value_avg
old["rate avg"] = rate_avg
# df = old.dropna(subset = ['value_avg'])
for i in range(j):
    z = rate_avg[i]/predicted_rate[i]
    ratio_predicted.append(z)
old["ratio predicted"] = ratio_predicted
ratio = len(ratio_predicted)
for i in range(ratio):
    if Foot[i]=="Right" or Foot[i]=="Right Only":
        z="Right"
    elif Foot[i]=="Left" or Foot[i]=="Left Only":
        z="Left"
    else:
        z="Either"
    foot.append(z)
    if ratio_predicted[i] > 0.92:
        label.append(1)
    else:
        label.append(0)
print(label)
old["label"] = label
old["Foot"] = foot
j= len(Astrology)
for i in range(j):
    if Astrology[i] == "Sagittarius" or Astrology[i] == "sagittarius":
        z= "Sagittarius"
    if Astrology[i] == "Capricorn" or Astrology[i] == "capricorn":
        z= "Capricorn"
    if Astrology[i] == "Aquarius" or Astrology[i] == "aquarius":
        z= "Aquarius"
    if Astrology[i] == "Pisces" or Astrology[i] == "pisces":
        z= "Pisces"
    if Astrology[i] == "Aries" or Astrology[i] == "aries":
        z= "Aries"
    if Astrology[i] == "Taurus" or Astrology[i] == "taurus":
        z= "Taurus"
    if Astrology[i] == "Gemini" or Astrology[i] == "gemini":
        z= "Gemini"
    if Astrology[i] == "Cancer" or Astrology[i] == "cancer":
        z= "Cancer"
    if Astrology[i] == "Leo" or Astrology[i] == "leo":
        z= "Leo"
    if Astrology[i] == "Virgo" or Astrology[i] == "virgo":
        z= "Virgo"
    if Astrology[i] == "Libra" or Astrology[i] == "libra":
        z= "Libra"
    if Astrology[i] == "scorpio" or Astrology[i] == "Scorpio":
        z = "Scorpio"
    astro.append(z)
old["Astrology"] = astro
old.Astrology = pd.Categorical(old.Astrology)
old.Position = pd.Categorical(old.Position)
old.Foot = pd.Categorical(old.Foot)
old['numeric astrology1'] = old.Astrology.cat.codes
old['numeric position'] = old.Position.cat.codes
old['numeric foot'] = old.Foot.cat.codes
# old['numeric wage'].fillna(old['Wage'].median(), inplace=True)
# print(old.Foot[1])
old.to_csv("data_newnew_2014.csv")
# print(old)