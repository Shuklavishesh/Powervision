from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

def prayer_test():
    # Setup Chrome driver
    options = Options()
    options.add_argument("--disable-notifications")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get("https://www.powervisionott.com")
        wait = WebDriverWait(driver, 10)

        # Open menu and click on Prayer request
        menu_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Prayer request")))
        menu_button.click()

        prayer_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Prayer request")))
        prayer_link.click()
        print("click on prayer link")

        # Wait for form to load
        wait.until(EC.presence_of_element_located((By.NAME, "name")))

        # Fill form fields
        fields = {
            "name": "Test User",
            "email": "testuser@example.com",
            "phoneno": "1234567890",
            "address": "43 Noida",
            "message": "Please pray for my family"
        }

        driver.find_element(By.NAME, "name").send_keys(fields["name"])
        driver.find_element(By.NAME, "email").send_keys(fields["email"])
        driver.find_element(By.NAME, "phoneno").send_keys(fields["phoneno"])
        driver.find_element(By.NAME, "address").send_keys(fields["address"])
        driver.find_element(By.NAME, "message").send_keys(fields["message"])

        # Select country (your logic)
        country_dropdown = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//div[@role="combobox" and @aria-haspopup="listbox"]')
        ))
        driver.execute_script("arguments[0].click();", country_dropdown)
        print("click select country options")

        # Select country option by CSS selector
        country_option = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//li[normalize-space(text())="India"]')
        ))
        driver.execute_script("arguments[0].click();", country_option)
        print("select country option India")
       

        # Click Submit button
        submit_btn = wait.until(EC.element_to_be_clickable(
           (By.XPATH, '//button[contains(text(), "Submit")]')
        ))
        driver.execute_script("arguments[0].click();", submit_btn)
        print("form submitted")

        # Wait for submission
        time.sleep(5)

    finally:
        driver.quit()

# Run the test
if __name__ == "__main__":
    prayer_test()
