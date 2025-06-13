import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# Simulate typing like a human
def human_typing(element, text):
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.1, 0.3))  # Random typing speed

# Launch undetected Chrome
options = uc.ChromeOptions()
options.add_argument("--start-maximized")

driver = uc.Chrome(options=options)

# Step 1: Open Google
driver.get("https://www.smartprix.com/mobiles")
time.sleep(2)

#Exculde out of stock
driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input').click()
time.sleep(1)

# #Exculde the upcoming
# driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input').click()
# time.sleep(2)

#only Smartphones
driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[6]/div[2]/label[1]/input').click()
time.sleep(2)

old_height = driver.execute_script("return document.body.scrollHeight;")

while True:
    driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
    time.sleep(1)

    new_height = driver.execute_script("return document.body.scrollHeight;")

    print(old_height)
    print(new_height)
    if new_height == old_height:
        break

    old_height = new_height

html = driver.page_source

with open("smartprix-smartphones.html", "w", encoding="utf-8") as f:
    f.write(html)


# Step 5: Keep browser alive
input("🔍 Press Enter to exit and close browser...")
driver.quit()