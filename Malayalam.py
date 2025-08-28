import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_malayalam_sections():
    options = Options()
    options.add_argument("--disable-notifications")

    # Setup driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get("https://www.powervisionott.com/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 15)

        # Click on Malayalam menu
        malayalam_menu = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Malayalam"))
        )
        malayalam_menu.click()
        print(" Clicked on Malayalam menu")

        # Wait for sections in Malayalam page
        sections = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "section.thumb_slider_section"))
        )
        print(f"Found {len(sections)} Malayalam content sections")

        # Loop through each section
        for index, section in enumerate(sections):
            print(f"\n===== Checking Malayalam Section {index+1} =====")

            # Section heading
            try:
                heading = section.find_element(By.TAG_NAME, "h4").text
                print(f" Section heading: {heading}")
            except:
                print("No heading found")

            # Thumbnails
            thumbnails = section.find_elements(By.TAG_NAME, "img")
            print(f"   Found {len(thumbnails)} thumbnails")

            for i, thumb in enumerate(thumbnails):
                src = thumb.get_attribute("src")
                if src and "http" in src:
                    print(f"Thumbnail {i+1} loaded: {src[:60]}...")
                else:
                    print(f"Thumbnail {i+1} missing src!")

            # Click first thumbnail to check video
            if thumbnails:
                try:
                    thumbnails[0].click()
                    print(" Clicked first video thumbnail")

                    # Wait for video or iframe
                    try:
                        video_player = wait.until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, "video, iframe"))
                        )
                        if video_player.is_displayed():
                            print("Hogaya Open Video player opened successfully")
                        else:
                            print("Ye Nahi Hua Video player not visible")
                    except:
                        print("No video player detected")

                    # Go back
                    driver.back()
                    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "section.thumb_slider_section")))
                except Exception as e:
                    print(f" Could not click video: {e}")

    finally:
        time.sleep(3)
        driver.quit()


# Run test
if __name__ == "__main__":
    test_malayalam_sections()
