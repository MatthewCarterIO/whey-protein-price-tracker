"""
    File name: whey_protein_price_tracker.py
    Author: Matthew Carter
    Date created: 05/12/2019
    Date last modified: 30/06/2020
    Python Version: 3.8.3

    Note: Used only for educational purposes.
"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime

# Create new instance of FireFox Webdriver.
driver = webdriver.Firefox()

# Open URL.
driver.get("https://www.myprotein.com/sports-nutrition/impact-whey-protein/10530943.html")
# Close pop-up window.
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "emailReengagement_close_button"))).click()

# Scroll down page to show whey bag weight buttons.
driver.execute_script('window.scrollTo(0,400)')
time.sleep(2)
# Click on 5kg bag button.
driver.find_element_by_css_selector("li.athenaProductVariations_listItem:nth-child(3) > button:nth-child(2)").click()
time.sleep(2)
# Get the updated price for 5kg bag.
five_kg_price = driver.find_element_by_class_name("productPrice_price").text

# Close browser.
driver.close()

# Get current date.
date_today = datetime.now().strftime("%d/%m/%Y")
# Print price on current date.
print("Price for 5kg of whey protein on {} is {}".format(date_today, five_kg_price))
