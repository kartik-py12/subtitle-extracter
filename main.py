from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# URL to the video page
url = "https://www.jiocinema.com/tv-shows/naagin/6/pragati-learns-prathna-s-past/3761450"

# Set up Chrome WebDriver
options = webdriver.ChromeOptions()
options.binary_location = r"C:\Program Files\Opera GX\launcher.exe"  # Change to your Opera GX installation path
driver = webdriver.Chrome(options=options)

# Open the URL in the browser
driver.get(url)

# Wait for the page to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "vjs-menu-button.vjs-control.vjs-button.vjs-subtitles-button")))

# Find and click the subtitle button (if applicable)
try:
    subtitle_button = driver.find_element(By.CLASS_NAME, "vjs-menu-button.vjs-control.vjs-button.vjs-subtitles-button")
    subtitle_button.click()
except Exception as e:
    print("Subtitle button not found or could not be clicked.")

# Wait for the subtitles to load
time.sleep(5)

# Get the subtitle content (if applicable)
try:
    subtitle_element = driver.find_element(By.CLASS_NAME, "vjs-track-label.vjs-subtitles-label")
    subtitle_content = subtitle_element.get_attribute("textContent")

    # Print the subtitles content
    print(subtitle_content)

    # You can save the content to a file here if needed

except Exception as e:
    print("Subtitles not found.")

# Close the browser
driver.quit()
