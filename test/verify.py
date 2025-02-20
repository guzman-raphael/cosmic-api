from selenium import webdriver 
from selenium.webdriver.firefox.options import Options 
from selenium.webdriver.common.by import By
import json
 
url = "https://guzman-raphael.github.io/cosmic-api/" 
 
options = Options() 
options.add_argument("-headless")
 
with webdriver.Firefox(options=options) as driver: 
    driver.get(url) 
    print(json.loads(driver.find_element(By.ID, "json").text)["shipments"][0])