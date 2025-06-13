#open google.com
# search campusx
# learnwith.campusx.in
#dsmp course page

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
driver.get("https://www.google.com")
time.sleep(2)

# Step 2: Find input box (Google Search box)
try:
    search_box = driver.find_element(By.NAME, "q")
except:
    search_box = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')

# Step 3: Type search term like human
human_typing(search_box, "CampusX")

# Step 4: Press Enter
time.sleep(1)
search_box.send_keys(Keys.ENTER)

link = driver.find_element(by= By.XPATH, value='//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a')
link.click()
time.sleep(1)

enroll = driver.find_element(by= By.XPATH, value='//*[@id="1698390585510d"]/div/div[1]/div/div/div/div[1]/div/div/div[2]/a[2]')
enroll.click()
time.sleep(5)

# Wait up to 10 seconds for the button to be present
try:
    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="public-page"]/div[1]/div/div/div/div/button')))
    button.click()
except Exception as e:
    print("⚠️ Button not found or clickable:", e)


# Step 5: Keep browser alive
input("🔍 Press Enter to exit and close browser...")
driver.quit()

