import requests
from bs4 import BeautifulSoup
import redis

redis_instance = redis.StrictRedis(host='localhost', port=6379, db=0)

def scrape_and_store_data():
    try:
        url = "https://www.nseindia.com/"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")

        # Assuming the data is in a table with class "nifty-table"
        table = soup.find("table", class_="nifty-table")
        rows = table.find_all("tr")

        # Process the rows and extract the data you need
        scraped_data = []
        for row in rows:
            cells = row.find_all("td")
            if cells:
                # Assuming the first cell contains the name and the second cell contains the value
                name = cells[0].text.strip()
                value = cells[1].text.strip()
                scraped_data.append({"name": name, "value": value})

        # Store the scraped data in Redis
        redis_instance.set("nifty_data", scraped_data)
        print("Data stored in Redis:", scraped_data)

    except Exception as e:
        print("Error while scraping data:", e)
