import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def run_test():
    # Disable notifications
    options = Options()
    options.add_argument("--disable-notifications")

    # Connect driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    # Open web
    driver.get("https://www.powervisionott.com/")
    driver.maximize_window()

    wait = WebDriverWait(driver, 40)

    # Login button
    login_btn = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[normalize-space()='Login']")))
    driver.execute_script("arguments[0].click();", login_btn)
    print("Login Button Clicked")

    # Phone input
    phone_input = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//input[@type='tel' and @placeholder='Enter your whatsapp no']")))
    phone_input.clear()
    phone_input.send_keys("8299445947")
    print("Entered WhatsApp number")

    # Recaptcha (manual)
    print("Please solve the recaptcha manually...")
    WebDriverWait(driver, 120).until(
        lambda d: d.find_element(By.XPATH, "//button[normalize-space()='Continue']").is_enabled()
    )

    # Continue button
    continue_btn = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[normalize-space()='Continue']")))
    driver.execute_script("arguments[0].click();", continue_btn)
    print("OTP Sent")

    time.sleep(50)
    driver.quit()


if __name__ == "__main__":
    run_test()
