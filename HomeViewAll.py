import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_home_sections():
    # Setup driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        driver.get("https://www.powervisionott.com/")   # Open website
        driver.maximize_window()

        wait = WebDriverWait(driver, 10)

        # Find all home sections
        sections = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "section.thumb_slider_section"))
        )

        print(f"Found {len(sections)} home sections")

        for index, section in enumerate(sections):
            try:
                # Extract heading if available
                heading = section.find_element(By.TAG_NAME, "h4").text
                print(f"✅ Section {index}: {heading}")

                # Check if 'View All' exists
                try:
                    view_all = section.find_element(By.LINK_TEXT, "View All")
                    print(f"   🔗 View All link found -> {view_all.get_attribute('href')}")
                except:
                    print("   ❌ No View All link in this section")

            except Exception as e:
                print(f"⚠️ Section {index} has no heading: {e}")

    finally:
        time.sleep(3)
        driver.quit()

# Run test
if __name__ == "__main__":
    test_home_sections()
    

