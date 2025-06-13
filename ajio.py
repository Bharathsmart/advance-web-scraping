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
driver.get("https://www.ajio.com/men-backpacks/c/830201001")
time.sleep(2)

old_height = driver.execute_script("return document.body.scrollHeight;")
# print(f"Full Page Height: {height}px")
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# we need stop the scroll at end of page
counter = 1
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    new_height = driver.execute_script("return document.body.scrollHeight;")
    print(counter)
    counter += 1
    print(old_height)
    print(new_height)
    if new_height == old_height:
        break

    old_height = new_height

html = driver.page_source

with open("ajio.html", "w", encoding="utf-8") as f:
    f.write(html)


# Step 5: Keep browser alive
input("🔍 Press Enter to exit and close browser...")
driver.quit()
