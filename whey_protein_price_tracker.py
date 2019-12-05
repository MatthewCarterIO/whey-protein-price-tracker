"""
    File name: whey_protein_price_tracker.py
    Author: Matthew Carter
    Date created: 05/12/2019
    Date last modified: 05/12/2019
    Python Version: 3.7.5

    Note: Only used for educational purposes.
"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime

# Create new instance of FireFox Webdriver.
driver = webdriver.Firefox()
# Open URL. Use time to give page chance to fully load.
driver.get("https://www.myprotein.com/sports-nutrition/impact-whey-protein/10530943.html")
time.sleep(4)
# Scroll down page to show whey bag weight buttons.
driver.execute_script('window.scrollTo(0,400)')
time.sleep(2)
# Click on 5kg bag button.
driver.find_element_by_css_selector("button.athenaProductVariations_box:nth-child(7)").click()
time.sleep(2)
# Get the updated price for 5kg bag.
five_kg_price = driver.find_element_by_class_name("productPrice_price").text
# Close browser.
driver.close()
# Get current date.
date_today = datetime.now().strftime("%d/%m/%Y")
# Print time and price.
print("Price for 5kg of whey protein on {} is {}".format(date_today, five_kg_price))
