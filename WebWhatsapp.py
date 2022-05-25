from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
import os

from Group import Group


class WebWhatsapp:
    def __init__(self):
        self.driver = self.__initiate_driver()

    def __initiate_driver(self):
        path_current_dir = os.path.dirname(__file__)
        # todo: make it so it selects the driver path based on the operating system
        options = Options()
        options.add_argument("user-data-dir=C:\\Users\\lukke\\AppData\\Local\\Google\\Chrome\\User Data")
        path_driver = "{}\chromedriver.exe".format(path_current_dir)
        driver = webdriver.Chrome(chrome_options=options, executable_path=path_driver)
        driver.get("https://web.whatsapp.com/")
        try:
            WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID, "side")))
        except TimeoutException:
            driver.close()
            time.sleep(5)
            return self.__initiate_driver()
        print("Driver ready to go!")
        return driver

    def get_groups(self):
        result_groups = []
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        side_id = "pane-side"
        sidebar = wait.until(EC.presence_of_element_located((By.ID, side_id)))
        group_class_name = "lhggkp7q ln8gz9je rx9719la"''
        groups = sidebar.find_elements(By.CLASS_NAME, group_class_name.replace(" ", "."))
        for group in groups:
            result_group = self.__process_group_webElement(group)
            result_groups.append(result_group)
            print(result_group)

    def __process_group_webElement(self, group_webElement):
        # get the group name
        group_name_class_name = "ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr i0jNr"
        group_name = group_webElement.find_elements(By.CLASS_NAME, group_name_class_name.replace(" ", "."))[0].text
        # get the unread_messages and muted statuses
        group_amount_unread_messages = 0
        group_is_muted = False
        statuses_class_name = "_1pJ9J"
        statuses = group_webElement.find_elements(By.CLASS_NAME, statuses_class_name)
        for status in statuses:
            status_unread_messages_class_name = "l7jjieqr cfzgl7ar ei5e7seu h0viaqh7 tpmajp1w c0uhu3dl riy2oczp dsh4tgtl sy6s5v3r gz7w46tb lyutrhe2 qfejxiq4 fewfhwl7 ovhn1urg ap18qm3b ikwl5qvt j90th5db aumms1qt"
            status_unread_messages = status.find_elements(By.CLASS_NAME,
                                                          status_unread_messages_class_name.replace(" ", "."))
            if status_unread_messages:
                group_amount_unread_messages = int(status_unread_messages[0].text.split(" ")[0])
            else:
                group_is_muted = True
        # create group object
        return Group(group_name, group_amount_unread_messages, group_is_muted)

    def stop_bot(self):
        self.driver.close()
