# scrape_imdb.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Setup Selenium
driver = webdriver.Chrome()

# IMDb 2024 movies page
url = "https://www.imdb.com/search/title/?year=2024&title_type=feature"
driver.get(url)
time.sleep(3)

movies = []
storylines = []

# Each movie block
movie_blocks = driver.find_elements(By.CSS_SELECTOR, "li.ipc-metadata-list-summary-item")

for block in movie_blocks:
    try:
        # Movie name
        name = block.find_element(By.CSS_SELECTOR, "h3.ipc-title__text").text.strip()

        # Storyline
        try:
            storyline = block.find_element(By.CSS_SELECTOR, "div.ipc-html-content-inner-div").text.strip()
        except:
            storyline = "No storyline available"

        movies.append(name)
        storylines.append(storyline)

    except Exception as e:
        print("Skipping due to error:", e)

driver.quit()

# Save to CSV
df = pd.DataFrame({"Movie Name": movies, "Storyline": storylines})
df.to_csv("imdb_movies_2024.csv", index=False, encoding="utf-8-sig")
print(f"✅ Data saved: {len(df)} movies in imdb_movies_2024.csv")
