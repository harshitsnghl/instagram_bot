from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os
import time


class InstagramBot:
    def __init__(self, username, password):
        self.option = webdriver.ChromeOptions()
        self.chrome_prefs = {}
        self.option.experimental_options["prefs"] = self.chrome_prefs
        self.chrome_prefs["profile.default_content_settings"] = {"images": 2}
        self.chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}
        self.username = username
        self.password = password
        self.base_url = "https://www.instagram.com"
        self.driver = webdriver.Chrome(options=self.option)
        self.login()
        

    def login(self):
        self.driver.get("https://www.instagram.com")
        time.sleep(4)
        self.driver.find_element_by_name("username").send_keys(self.username)
        self.driver.find_element_by_name("password").send_keys(self.password)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button").click()
        self.driver.set_window_size

    def nav_user(self, user):
        time.sleep(4)
        self.driver.get("{}/{}/".format(self.base_url, user))
        time.sleep(3)
        self.driver.find_element_by_class_name("_9AhH0").click()
        time.sleep(1)


    def nav_tag(self, tag):
        time.sleep(4)
        self.driver.get("{}/explore/tags/{}/".format(self.base_url, tag))
        time.sleep(3)
        self.driver.find_element_by_class_name("_9AhH0").click()
        time.sleep(3)


    def like(self, post_count):
        count = 0
        liked_pictures = 0
        unliked_pictures = 0


        while count < post_count:


            try:
                self.driver.find_element_by_css_selector("[aria-label='Unlike']")


            except NoSuchElementException:
                try:
                    self.driver.find_element_by_css_selector("[aria-label='Like']").click()
                    unliked_pictures = unliked_pictures + 1
                    print(unliked_pictures)
                except NoSuchElementException:
                    self.driver.find_element_by_class_name("coreSpriteRightPaginationArrow").click()
                    time.sleep(3.5)
                    print("skipped")
            
            try:
                self.driver.find_element_by_class_name("coreSpriteRightPaginationArrow").click()
                time.sleep(3.5)
                count = count + 1


            except NoSuchElementException:
                print(" Liked pictures successfully ")


if __name__ == "__main__":
    # username = input("Enter the username: ")
    # password = input("Enter the password: ")
    ig_bot = InstagramBot("harshitsinghal__", "cosmos")
    # ig_bot.nav_user("dusky_bong")
    ig_bot.nav_tag("l4l")     
    ig_bot.like(post_count=5000)


#538
#follow: 306 million+ posts

#like4like: 296 million+ posts

#tagsforlikes: 209 million+ posts

#instalike: 207+ million posts

#likeforlike: 193 million+ posts

#follow4follow: 178 million+ posts

#followforfollow: 133 million+ posts

#l4l: 123 million+ posts

#f4f: 121 million+ posts

#followback: 76 million+ posts

#instafollow: 75 million+ posts

#likeforfollow: 42 million+ posts//20 per day

#likeforlikes: 41 million+ posts

#20likes: 41 million+ posts

#likeback: 37 million+ posts

#likes4likes: 29 million+ posts

#followher:  29 million+ posts

#followhim: 24 million+ posts

#lfl: 23 million+ posts

#pleasefollow: 23 million+ posts

#like4follow: 23 million+ posts

#teamfollowback: 22 million+ posts

