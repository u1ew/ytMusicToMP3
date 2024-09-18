from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import json


# Path to your Chrome profile
profile_path = r'C:\Users\ewanj\AppData\Local\Google\Chrome\User Data'

# Path to your Chromedriver
chromedriver_path = r'C:\Users\ewanj\Documents\CODING\ytMusicPlaylistDownload\chromedriver\chromedriver.exe'

# Set up Chrome options
options = Options()
options.add_argument(f"user-data-dir={profile_path}")

# Set up the Chrome service
service = Service(executable_path=chromedriver_path)

# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=options)

# Open YouTube Playlist with songs
driver.get("https://music.youtube.com/playlist?list=PLCK20UqkVhH5eoEcb5XvA1sSezmTPc2-Y")

# Keep the browser open for a while
print("2 second wait")
time.sleep(2)  # Adjust the sleep time as needed

def goBottom(driver):
    return driver.execute_script("return (window.innerHeight + window.scrollY) >= document.body.scrollHeight")


while True:
    # Scroll down
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Wait for the page to load

    # Check if at the bottom
    if goBottom(driver):
        break

time.sleep(1)

with open(r'C:\Users\ewanj\Documents\CODING\ytMusicPlaylistDownload\linkCollectionScript.js', 'r') as file:
    jsFile = file.read()

result = driver.execute_script(jsFile)

with open(r'C:\Users\ewanj\Documents\CODING\ytMusicPlaylistDownload\linksCollected.json', 'w') as json_file:
    json.dump(result, json_file, indent=4)

# Close the browser
driver.quit()

time.sleep(1)


with open(r'C:\Users\ewanj\Documents\CODING\ytMusicPlaylistDownload\linksCollected.json', 'r') as json_file:
    data = json.load(json_file)

    
links = data

for link in links:

print("Downloading Complete")
