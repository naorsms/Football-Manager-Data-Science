from selenium import webdriver
from datetime import date
from datetime import datetime
import time
from selenium.webdriver.common.keys import Keys
from astrology import astro
import re


option = webdriver.ChromeOptions()
option.add_argument('headless')


class YouthPlayer:
    """contains player arrtibutes from when he was youth"""

    def __init__(self, rate, name, age, nation, club, role, value, wk_year):
        if "," in name:
            first_name = name.rsplit(', ', 1)[1]
            last_name = name.split(',', 1)[0]
            self.name = first_name + " " + last_name
        else:
            self.name = name
        self.rate = rate
        self.value = value
        self.nation = nation
        self.role = role
        self.age = age
        self.club = club
        self.wk_year = wk_year

    def __repr__(self):
        return f"name:{self.name} age:{self.age} value:{self.value}"


#
class WebScrape():
    """contains scrape functions"""

    def scrape_fmscout(self):
        fmscout = {"birthday": (4, "", 0, 1, 3, 1), "club": (4, "", 1, 0, 1, 1), "game": (4, "", 1, 0, 3, 1),
                   "wage": (4, "", 1, 0, 4, 1),
                   "foot": (5, "small-12 ", 0, 0, 2, 1), "height": (5, "small-12 ", 0, 0, 3, 1),
                   "game_rating": (7, "small-12 ", 0, 0, 1, 0)}
        driver = webdriver.Chrome(options=option)
        driver.get("https://www.fmscout.com/players.html/")
        element = driver.find_element_by_id("name")
        element.send_keys(self.name, Keys.ENTER)
        time.sleep(3)
        player_url = driver.execute_script(
            "return document.getElementsByClassName('link')[0].querySelectorAll('tbody')[0].rows[0].cells["
            "1].querySelector('a').href")
        print(player_url)
        driver.get(player_url)
        time.sleep(3)

        keys = list(fmscout.keys())
        for i in range(len(fmscout)):
            fmscout[keys[i]] = f"return document.getElementsByClassName('large-{fmscout[keys[i]][0]} " \
                               f"medium-6 {fmscout[keys[i]][1]}columns')[{fmscout[keys[i]][2]}].querySelectorAll('tbody')[{fmscout[keys[i]][3]}].rows[{fmscout[keys[i]][4]}].cells[{fmscout[keys[i]][5]}].innerText;"
        player_arrtibutes = []
        for i in fmscout:
            player_arrtibutes.append(driver.execute_script(fmscout[i]))
        self.birthday, self.currclub, self.currvalue, self.currwage, self.foot, self.height, self.currrate = player_arrtibutes
        self.currage = int(date.today().year) - int(self.birthday.split("-")[2])
        month = datetime.strptime(self.birthday.split("-")[1], "%b").month
        self.astrolog = astro(int(self.birthday.split("-")[0]), month)
        driver.close()

    def scrape_trasfermarket(self):
        transfer_market = {"full_birthday": 0, "club": 8, "foot": 6, "height": 3}
        driver = webdriver.Chrome(options=option)
        driver.get("https://www.transfermarkt.com/")
        element = driver.find_element_by_class_name("tm-header__input--search-field")
        element.send_keys(self.name, Keys.ENTER)
        player_url = driver.execute_script(
            "return document.getElementsByClassName('inline-table')["
            "0].querySelectorAll('tbody')[0].rows[0].cells["
            "1].querySelector('a').href")
        driver.get(player_url)
        time.sleep(3)
        keys = list(transfer_market.keys())
        for i in range(len(transfer_market)):
            transfer_market[keys[i]] = driver.execute_script(f"return document.getElementsByClassName" \
                                                             f"('info-table__content info-table__content--bold')[{transfer_market[keys[i]]}].innerText")
        self.real_est_value = driver.execute_script("return document.getElementsByClassName('auflistung')"
                                                    "[0].getElementsByClassName('right-td')[0].innerText")
        player_attributes = []
        for i in transfer_market:
            player_attributes.append(transfer_market[i])
        self.birthday, self.currclub, self.foot, self.height = player_attributes
        self.currwage, self.currrate, self.currvalue = None, None, None
        self.currage = int(date.today().year) - int(self.birthday.split(",")[1])
        month = datetime.strptime(self.birthday.split(" ")[0], "%b").month
        day = self.birthday.split(" ")[1].split(",")[0]
        self.astrolog = astro(int(day), month)
        driver.close()

    def real_est_only(self):
        try:
            driver = webdriver.Chrome(options=option)
            driver.get("https://www.transfermarkt.com/")
            element = driver.find_element_by_class_name("tm-header__input--search-field")
            print(self.name)
            # driver.implicitly_wait(20)
            element.send_keys(self.name, Keys.ENTER)
            self.real_est_value = driver.execute_script(
                "return document.getElementsByClassName('rechts hauptlink')[0].innerText")
            driver.close()
        except:
            print("faild to get value from transfermarket")
            driver.close()
            self.real_est_value = None

    def football_critic(self):
        try:

            driver = webdriver.Chrome(options=option)
            driver.get("https://www.footballcritic.com/")
            element = driver.find_element_by_id("bb-search-input")
            element.send_keys(self.name, Keys.ENTER)
            FootballCritic_rating_na = driver.execute_script(
                "return document.getElementsByClassName('rating')[0].innerText;")
            driver.close()
            if FootballCritic_rating_na == "N/A":
                self.real_rating = None
            else:
                self.real_rating = FootballCritic_rating_na
        except:
            print(f"{self.name} was not found at football criting therefore there is no rating for him")
            driver.close()
            self.real_rating = None


class PresentPlayer(WebScrape, YouthPlayer):
    """the class contains the player's present attributes"""

    def __init__(self, name):
        super(YouthPlayer).__init__()
        self.name = name
        try:
            super().scrape_fmscout()
            super().real_est_only()
            super().football_critic()
        except:
            try:
                super().scrape_trasfermarket()
                super().football_critic()
            except:
                self.name = "error"

    def __repr__(self):
        return f"name:{self.name}age:{self.currage} value:{self.real_rating}"


class FinalPlayer:
    """takes all relevant attributes from 'YouthPlayer' and 'PresentPlayer' modifies some of the attributes
        and writes them into CSV.
    """
    def __init__(self, player, age, nation, position, club, birthday, astrology, foot,
                 height, wage, youth_value, game_value, transfermarket_value,
                 predicted_rate, game_rating, fotball_critic_rating):
        self.player = player
        self.age = age
        self.nation = nation
        self.position = position
        self.club = club
        self.birthday = birthday
        self.astrology = astrology
        self.foot = foot
        self.height = re.sub("[^0-9]", "", height)
        if wage == None:
            self.wage = None
        else:
            temp_wage = re.sub("[^0-9]", "", wage)
            self.wage = str(float(temp_wage) * 1000)
        self.youth_value = str(float(youth_value) * 1000)
        if game_value == None:
            self.game_value = None
        else:
            temp_game_value = game_value
            if re.match("[^M]", temp_game_value):
                temp_game_value = re.sub("[^0-9]", "", temp_game_value)
                self.game_value = str(float(temp_game_value) * 1000000)
            else:
                temp_game_value = re.sub("[^0-9]", "", temp_game_value)
                self.game_value = str(float(temp_game_value) * 1000)
            if transfermarket_value == None:
                self.transfermarket_value = None
            else:
                temp_transfermarket_value = transfermarket_value
            if re.match("[^m]", temp_transfermarket_value):
                temp_transfermarket_value = re.sub("[^0-9]", "", temp_transfermarket_value)
                self.transfermarket_value = str(float(temp_transfermarket_value) * 1000000)
            else:
                temp_transfermarket_value = re.sub("[^0-9]", "", temp_transfermarket_value)
                self.transfermarket_value = str(float(temp_transfermarket_value) * 1000)
        self.predicted_rate = predicted_rate
        self.game_rating = game_rating
        self.football_critic_rating = fotball_critic_rating
