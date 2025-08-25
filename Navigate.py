import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


# Setup driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.maximize_window()
driver.get("https://www.powervisionott.com/")

wait = WebDriverWait(driver, 25)   # Increased wait time

# Define menu sections with XPaths
sections = [
    ("Malayalam", "//a[@data-text='Malayalam']"),
    ("English", "//a[@data-text='English']"),
    ("Youth & Kids", "//a[@data-text='Youth & Kids']"),
    ("Prayer request", "//a[@data-text='prayer']"),
]

for name, xpath in sections:
    print(f"➡ Navigating to {name}...")

    # Wait for menu item
    btn = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

    # Scroll into view (handles hidden elements)
    driver.execute_script("arguments[0].scrollIntoView(true);", btn)
    time.sleep(1)

    # Click using JS (more reliable than normal .click())
    driver.execute_script("arguments[0].click();", btn)

    # Wait for section content to load
    try:
        wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//div[contains(@class,'MuiGrid-root')]//img")
            )
        )
        print(f"✅ {name} content loaded")
    except:
        print(f"⚠ {name} content might not have loaded fully")

    time.sleep(3)

print("🎉 Navigation test completed.")
driver.quit()
