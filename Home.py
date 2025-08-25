"""
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def run():
    options = Options()
    options.add_argument("--disable-notifications")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://www.powervisionott.com/")
    driver.maximize_window()

    wait = WebDriverWait(driver, 40)

    # ✅ Home
    home_btn = wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Home"))
    )
    driver.execute_script("arguments[0].click();", home_btn)
    print("Home link clicked")
    
    wait.until(EC.presence_of_element_located((By.XPATH,"//span[contains(text(),'Home')]")))
    print("Home content downloaded")

    
    # Malayalam
    malayalam = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Malayalam")))
    driver.execute_script("arguments[0].click();", malayalam)
    print("Malayalam link clicked")

# Wait for Malayalam video grid
    wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class,'MuiGrid-root')]//img")))
    print("Malayalam content loaded")


# English
    english = wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"English")))
    driver.execute_script("arguments[0].click();", english)
    print("English link clicked")

    wait.until(EC.presence_of_all_elements_located((By.XPATH,"//div[contains(@class,'MuiGrid-root')]//img")))
    print("English content loaded")


# Youth & Kids
    youth = wait.until(EC.element_to_be_clickable((By.LINK_TEXT,'Youth & Kids')))
    driver.execute_script("arguments[0].click();", youth)
    print("Youth & Kids clicked")

    wait.until(EC.presence_of_all_elements_located((By.XPATH,"//div[contains(@class,'MuiGrid-root')]//img")))
    print("Youth & Kids content loaded")



    # Screenshot
    driver.save_screenshot("home_page.png")
    print("Screenshot saved as home_page.png")
    

    time.sleep(50)
    driver.quit()


if __name__ == "__main__":
    run()

"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def run():
    options = Options()
    options.add_argument("--disable-notifications")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://www.powervisionott.com/")
    driver.maximize_window()

    wait = WebDriverWait(driver, 30)

    # ✅ Navigate to Home
    home_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/browse/home/001']")))
    driver.execute_script("arguments[0].click();", home_btn)
    print("✅ Home clicked")

    wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/browse/home/001' and contains(@class,'active')]")))
    print("Home content loaded")

    # ✅ Navigate to Malayalam
    malayalam_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/browse/malayalam/237']")))
    driver.execute_script("arguments[0].click();", malayalam_btn)
    print("✅ Malayalam clicked")

    wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/browse/malayalam/237' and contains(@class,'active')]")))
    print("Malayalam content loaded")

    # ✅ Navigate to English
    english_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/browse/english/47']")))
    driver.execute_script("arguments[0].click();", english_btn)
    print("✅ English clicked")

    wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/browse/english/47' and contains(@class,'active')]")))
    print("English content loaded")

    # ✅ Navigate to Youth & Kids (from your second screenshot, href should be /browse/youth-kids/XYZ, update ID if different)
    youth_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'/browse/youth')]")))
    driver.execute_script("arguments[0].click();", youth_btn)
    print("✅ Youth & Kids clicked")

    wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href,'/browse/youth') and contains(@class,'active')]")))
    print("Youth & Kids content loaded")

    # ✅ Take screenshot
    driver.save_screenshot("navigation_flow.png")
    print("Screenshot saved as navigation_flow.png")

    time.sleep(5)
    driver.quit()


if __name__ == "__main__":
    run()

