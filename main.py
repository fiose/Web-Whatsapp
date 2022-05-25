from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
import os

from WebWhatsapp import WebWhatsapp


whatsapp_bot = WebWhatsapp()
whatsapp_bot.get_groups()
#whatsapp_bot.stop_bot()
"""

path_current_dir = os.path.dirname(__file__)
# todo: make it so it selects the driver path based on the operating system
options = Options()
options.add_argument("user-data-dir=C:\\Users\\lukke\\AppData\\Local\\Google\\Chrome\\User Data")
path_driver = "{}\chromedriver.exe".format(path_current_dir)
driver = webdriver.Chrome(chrome_options=options, executable_path=path_driver)

driver.get("https://web.whatsapp.com/")

wait = WebDriverWait(driver, 600)

# Replace 'Friend's Name' with the name of your friend
# or the name of a group
target = '"Friend\'s Name"'

# Replace the below string with your own message
string = "Message sent using Python!!!"

x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((
    By.XPATH, x_arg)))
group_title.click()
inp_xpath = '//div[@class="_13NKt copyable-text selectable-text"][@data-tab="9"]'
input_box = wait.until(EC.presence_of_element_located((
    By.XPATH, inp_xpath)))
for i in range(100):
    input_box.send_keys(string + Keys.ENTER)
    time.sleep(1)"""