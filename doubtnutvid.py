from time import sleep
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json

#get link to doubtnut site from user
link = input("Enter link: " )


#selenium setup
cap = DesiredCapabilities().CHROME
cap["pageLoadStrategy"]  = "eager"

options = Options()
options.add_argument('--headless=new')
options.add_argument("--log-level=3")

driver = webdriver.Chrome(options=options)
driver.get(link)

#locating element and extracting required values
ele = driver.find_element(By.XPATH, "/html/body/script")
raw_data = ele.get_attribute("innerHTML")

compiledData = json.loads(raw_data)
videoName = compiledData["props"]["pageProps"]["videoData"]["video_name"]


#output video link
driver.close()
print("https://videos.doubtnut.com/"+videoName)
