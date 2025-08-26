import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options  

def test_home_sections():
    
    options = Options()
    options.add_argument("--disable-notifications")
    
    # Setup driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service,options=options)

    try:
        driver.get("https://www.powervisionott.com/")   # Open website
        driver.maximize_window()

        wait = WebDriverWait(driver, 15)

        # Find all home sections
        sections = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "section.thumb_slider_section"))
        )

        print(f"Found {len(sections)} home sections")

        for index, section in enumerate(sections):
            print(f"\n===== Checking Section {index} =====")

            # Get section heading (if available)
            try:
                heading = section.find_element(By.TAG_NAME, "h4").text
                print(f" Section heading: {heading}")
            except:
                print(" No heading found for this section")

            # Find all thumbnails inside section
            thumbnails = section.find_elements(By.TAG_NAME, "img")
            print(f"   Found {len(thumbnails)} thumbnails")

            for i, thumb in enumerate(thumbnails):
                src = thumb.get_attribute("src")
                if src and "http" in src:
                    print(f"Thumbnail {i} loaded: {src[:60]}...")
                else:
                    print(f"Thumbnail {i} missing src!")

            # Try clicking the first thumbnail to test video playback
            if thumbnails:
                try:
                    thumbnails[0].click()
                    print("Hogaya Bhaiya Clicked first video thumbnail")

                    # Wait for video player or iframe
                    try:
                        video_player = wait.until(
                            EC.presence_of_element_located(
                                (By.CSS_SELECTOR, "video, iframe")
                            )
                        )
                        if video_player.is_displayed():
                            print("Video player opened successfully")
                        else:
                            print("Video player not visible")
                    except:
                        print("No video player detected")

                    # Go back to homepage
                    driver.back()
                    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "section.thumb_slider_section")))
                except Exception as e:
                    print(f"    Could not click video: {e}")

    finally:
        time.sleep(3)
        driver.quit()

# Run test
if __name__ == "__main__":
    test_home_sections()
