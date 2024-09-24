from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")

# Find the search box using its name attribute value
search_box = driver.find_element("name", "q")

# Type the search query and hit Enter
search_box.send_keys("Selenium automation tool")
search_box.send_keys(Keys.RETURN)

# Wait for a few seconds to let the results load
time.sleep(2)

# Get the titles of the search results
titles = driver.find_elements("css selector", "h3")
for title in titles:
    print(title.text)

# Close the browser
driver.quit()