from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service  
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

path=r"chromedriver.exe" #chrome driver.exe hangi taracıyla belirler
serv = Service( path )
driver = webdriver.Chrome( service =serv )
driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@id='searchInput']").send_keys("Selenium (software)")
time.sleep(1)
driver.find_element(By.XPATH,"//a[@title='Selenium (software)']").click
driver.find_element(By.XPATH,"//input[@id='searchInput']").send_keys(Keys.ENTER)

check_text ="Selenium"
readed_text = driver.find_element(By.XPATH,"//b[normalize-space()='Selenium']").text
assert readed_text == check_text,"Not succesful testing"
#if no asssert 
print("Test succesful")