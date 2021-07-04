from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import datetime
import test
import pandas as pd
import numpy as np


def FootballCritic():
    try:
        driver = webdriver.Chrome(executable_path="../drivers/chromdriver-4")
        driver.get("https://www.footballcritic.com/")
        element = driver.find_element_by_id("bb-search-input")
        element.send_keys(player, Keys.ENTER)
        FootballCritic_rating_na = driver.execute_script(
            "return document.getElementsByClassName('rating')[0].innerText;")
        if FootballCritic_rating_na == "N/A":
            FootballCritic_rating.append(None)
        else:
            FootballCritic_rating.append(FootballCritic_rating_na)
        driver.close()
    except:
        print("{} was not found at football criting therefore there is no rating for him".format(player))
        FootballCritic_rating.append(None)
        driver.close()


WonderKids = pd.read_csv("WonderKidsListAll.csv")
player_withInfo = list()
player_only_tm_info = list()
notfound = list()
player_arr = list()
age = list()
birthday = list()
astrolog = list()
club = list()
game_value = list()
wage = list()
foot = list()
height = list()
game_rating = list()
real_est_value = list()
nation = list()
position = list()
predicted_rate = list()
youth_value = list()
WKListYear = list()
FootballCritic_rating = list()

i = 3500

while (i <= 3900):

    player = WonderKids.at[i + 1, 'name']
    if "," in player:
        first_name = player.rsplit(', ', 1)[1]
        last_name = player.split(',', 1)[0]
        player = first_name + " " + last_name
        # player = "ayad habashi"
        print(player)
        if " " in player:
            try:
                driver = webdriver.Chrome(executable_path="../drivers/chromdriver-4")
                driver.get("https://www.fmscout.com/players.html/")
                element = driver.find_element_by_id("name")
                element.send_keys(player, Keys.ENTER)
                time.sleep(3)
                # player_url = driver.find_element_by_link_text(player).get_attribute("href")
                player_url = driver.execute_script(
                    "return document.getElementsByClassName('link')[0].querySelectorAll('tbody')[0].rows[0].cells["
                    "1].querySelector('a').href")
                print(player_url)
                driver.get(player_url)
                time.sleep(3)
                ageTemp = driver.execute_script(
                    "return document.getElementsByClassName('large-4 medium-6 columns')[0].querySelectorAll('tbody')["
                    "1].rows[2].cells[1].innerText;")
                full_birthdate = driver.execute_script(
                    "return document.getElementsByClassName('large-4 medium-6 columns')[0].querySelectorAll('tbody')["
                    "1].rows[3].cells[1].innerText;")
                day = full_birthdate.split("-")[0]
                month = full_birthdate.split("-")[1]
                month = datetime.datetime.strptime(month, "%b").month
                birthdayTemp = month
                clubTemp = driver.execute_script(
                    "return document.getElementsByClassName('large-4 medium-6 columns')[1].querySelectorAll('tbody')["
                    "0].rows[1].cells[1].innerText;")
                game_valueTemp = driver.execute_script(
                    "return document.getElementsByClassName('large-4 medium-6 columns')[1].querySelectorAll('tbody')["
                    "0].rows[3].cells[1].innerText;")
                wageTemp = driver.execute_script(
                    "return document.getElementsByClassName('large-4 medium-6 columns')[1].querySelectorAll('tbody')["
                    "0].rows[4].cells[1].innerText;")
                footTemp = driver.execute_script(
                    "return document.getElementsByClassName('large-5 medium-6 small-12 columns')[0].querySelectorAll("
                    "'tbody')[0].rows[2].cells[1].innerText;")
                heightTemp = driver.execute_script(
                    "return document.getElementsByClassName('large-5 medium-6 small-12 columns')[0].querySelectorAll("
                    "'tbody')[0].rows[3].cells[1].innerText;")
                game_ratingTemp = driver.execute_script(
                    "return document.getElementsByClassName('large-7 medium-6 small-12 columns')[0].querySelectorAll("
                    "'tbody')[0].rows[1].cells[0].innerText;")
                player_arrTemp = player
                astrolog.append(test.astro(int(day), month))
                age.append(ageTemp)
                birthday.append(birthdayTemp)
                club.append(clubTemp)
                game_value.append(game_valueTemp)
                wage.append(wageTemp)
                foot.append(footTemp)
                height.append(heightTemp)
                game_rating.append(game_ratingTemp)
                player_arr.append(player_arrTemp)
                driver.close()
                try:
                    driver = webdriver.Chrome(executable_path="../drivers/chromdriver-4")
                    driver.get("https://www.transfermarkt.com/")
                    element = driver.find_element_by_class_name("header-suche")
                    driver.implicitly_wait(20)
                    element.send_keys(player, Keys.ENTER)
                    real_est_value.append(driver.execute_script("return document.getElementsByClassName('rechts "
                                                                "hauptlink')[0].innerText"))
                    player_withInfo.append(player)
                    driver.close()
                except:
                    print("faild to get value from transfermarket")
                    real_est_value.append(None)
                    player_withInfo.append(player)
                FootballCritic()
            except:
                try:
                    print("{} was not found at FMscout 21 searching at transfer-market...".format(player))
                    transferMarket_url = "https://www.transfermarkt.com/"
                    driver = webdriver.Chrome(executable_path="../drivers/chromdriver-4")
                    driver.get(transferMarket_url)
                    element = driver.find_element_by_class_name("header-suche")
                    element.send_keys(player, Keys.ENTER)
                    player_url = driver.execute_script(
                        "return document.getElementsByClassName('inline-table')["
                        "0].querySelectorAll('tbody')[0].rows[0].cells["
                        "1].querySelector('a').href")
                    driver.get(player_url)
                    time.sleep(3)
                    # the command below is to check if there is missing data in the transfer market or not
                    driver.execute_script(
                        "return document.getElementsByClassName('auflistung')[2].querySelector('tbody').rows["
                        "12].cells[1].innerText;")
                    ageTemp = driver.execute_script(
                        "return document.getElementsByClassName('auflistung')[2].querySelector('tbody').rows["
                        "3].cells[1].innerText;")
                    full_birthdate = driver.execute_script(
                        "return document.getElementsByClassName('auflistung')[2].querySelector('tbody').rows["
                        "1].cells[1].innerText;")
                    noyear_birthday = full_birthdate.split(",")[0]
                    day = noyear_birthday.split(" ")[1]
                    month = noyear_birthday.split(" ")[0]
                    month = datetime.datetime.strptime(month, "%b").month
                    # print(month)
                    birthdayTemp = month
                    clubTemp = driver.execute_script(
                        "return document.getElementsByClassName('auflistung')[2].querySelector('tbody').rows["
                        "9].cells[1].innerText;")
                    game_valueTemp = None
                    wageTemp = None
                    footTemp = driver.execute_script(
                        "return document.getElementsByClassName('auflistung')[2].querySelector('tbody').rows["
                        "7].cells[1].innerText;")
                    heightTemp = driver.execute_script(
                        "return document.getElementsByClassName('auflistung')[2].querySelector('tbody').rows["
                        "4].cells[1].innerText;")
                    game_ratingTemp = (None)
                    player_arrTemp = player
                    astrolog.append(test.astro(int(day), month))
                    age.append(ageTemp)
                    birthday.append(birthdayTemp)
                    club.append(clubTemp)
                    game_value.append(game_valueTemp)
                    wage.append(wageTemp)
                    foot.append(footTemp)
                    height.append(heightTemp)
                    game_rating.append(game_ratingTemp)
                    player_arr.append(player_arrTemp)
                    try:
                        real_est_value.append(
                            driver.execute_script("return document.getElementsByClassName('right-td')[0].innerText"))
                    except:
                        real_est_value.append(None)
                    player_withInfo.append(player)
                    driver.close()

                    FootballCritic()

                except:
                    print("there are missing data in the transfer market not filling this praticular player")
                    player_arr.append(player)
                    notfound.append(player)
                    age.append(None)
                    birthday.append(None)
                    astrolog.append(None)
                    club.append(None)
                    game_value.append(None)
                    wage.append(None)
                    foot.append(None)
                    height.append(None)
                    game_rating.append(None)
                    real_est_value.append(None)
                    FootballCritic_rating.append(None)
                    driver.close()

            nation.append(WonderKids.at[i + 1, 'nation'])
            position.append(WonderKids.at[i + 1, 'role'])
            predicted_rate.append(WonderKids.at[i + 1, 'rate'])
            youth_value.append(WonderKids.at[i + 1, 'value'])
            WKListYear.append(WonderKids.at[i + 1, 'WK list year'])

    else:
        notfound.append(player)

    i += 1
    print("index = {}".format(i))
    print("player_arr len: {}".format(len(player_arr)))
    print("player that was not found at all array: {}".format(notfound))
    print("player that was not found at all: {}".format(len(notfound)))
    print("player with all data array: {}".format(player_withInfo))
    print("player with all data: {}".format(len(player_withInfo)))
    print("age len: {}".format(len(age)))
    print("birthday len: {}".format(len(birthday)))
    print("astrolog len: {}".format(len(astrolog)))
    print("club len: {}".format(len(club)))
    print("game_value: {}".format(len(game_value)))
    print("wage len: {}".format(len(wage)))
    print("foot len: {}".format(len(foot)))
    print("height len: {}".format(len(height)))
    print("game_rating len: {}".format(len(game_rating)))
    print("nation len: {}".format(len(nation)))
    print("position len: {}".format(len(position)))
    print("predicted_rate len: {}".format(len(predicted_rate)))
    print("youth_value len: {}".format(len(youth_value)))
    print("WKListYear len: {}".format(len(WKListYear)))
    print("real_est_value len : {}".format(len(real_est_value)))
    print("FootballCritic_rating len : {}".format(len(FootballCritic_rating)))

df = pd.DataFrame(
    {"Player": pd.Series(player_arr), "Age": pd.Series(age), "Nation": pd.Series(nation),
    "Position": pd.Series(position), "Club": pd.Series(club), "Birthday": pd.Series(birthday),
    "Astrology": pd.Series(astrolog), "Foot": pd.Series(foot), "Height": pd.Series(height),
    "Wage": pd.Series(wage), "youth_value": pd.Series(youth_value), "Game Value": game_value,
    "TransferMarket Value": pd.Series(real_est_value), "predicted_rate": pd.Series(predicted_rate),
    "Game Rating": pd.Series(game_rating), "Fotball Critic rating": pd.Series(FootballCritic_rating)})
df.to_csv("PresnetDay3500_3900.csv", mode='w',index=False)
