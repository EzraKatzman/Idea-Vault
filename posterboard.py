from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, os, sys, traceback
from dotenv import load_dotenv

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
load_dotenv()

args = sys.argv
args.pop(0)
content = ' '.join(args)

driver.get("https://www.notion.so/8aeb1067f7244d708066f03e2a1df719?v=3b1c8594783a436a8db269c933159fe8")

try:
    userinput = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="notion-app"]/div/div[1]/div/main/div/div[3]/div[3]/div[3]/input'))
    )
    userinput.send_keys(os.getenv('NOTIONUSER'))
    userinput.send_keys(Keys.RETURN)
    passinput = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="notion-app"]/div/div[1]/div/main/div/div[3]/div[3]/div[5]/input'))
    )
    passinput.send_keys(os.getenv('NOTIONPASS'))
    passinput.send_keys(Keys.RETURN)
    buttonpress = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="notion-app"]/div/div[1]/div[2]/div[2]/div[3]/div/div/div[1]/div[1]/div[1]/div[5]'))
    )
    buttonpress.click()
    title = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="notion-app"]/div/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div[1]/div[3]/a/div/div[2]/div'))
    )
    title.send_keys(content)
    time.sleep(5)
    driver.quit()
    print("Successfully added to Notion")
except:
    driver.quit()
    print("An error occurred")
    traceback.print_exc()
    