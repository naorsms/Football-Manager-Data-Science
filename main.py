from configclass import YouthPlayer
from configclass import PresentPlayer
from configclass import FinalPlayer
import pandas as pd

wk_list = pd.read_csv("WonderKidsListAll.csv")

youth_player = []
for i in range(len(wk_list)):
    youth_player.append(YouthPlayer(*list(wk_list.iloc[i][1:])))

final_player_list = []
for i in range(1,6):
    print(i)
    if " " in youth_player[i].name:
        present_player = PresentPlayer(youth_player[i].name)
        if present_player.name != "error":
            print(present_player.__dict__)
            final_player = FinalPlayer(present_player.name, present_player.currage,youth_player[i].nation,youth_player[i].role,
                                       present_player.currclub,present_player.birthday,present_player.astrolog,present_player.foot,
                                       present_player.height,present_player.currwage,youth_player[i].value,present_player.currvalue,
                                       present_player.real_est_value,youth_player[i].rate,present_player.currrate,present_player.real_rating)
            final_player_list.append(final_player.__dict__)
df = pd.DataFrame(final_player_list)

df.to_csv('yourfile.csv', index=False)