from celery import Celery
from django.shortcuts import render
import redis
from .tasks import scrape_and_store_data

app = Celery('web_scraper_project')
app.conf.broker_url = 'memory://'
# Connect to your Redis instance
redis_instance = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

def card_layout(request):
    nifty_data = redis_instance.get("nifty_data")

    if not nifty_data:
        # If data is not available, fetch the data synchronously using the task function
        scrape_and_store_data()

        # Retrieve the data again from Redis after scraping and storing
        nifty_data = redis_instance.get("nifty_data")

    # Pass the relevant data to the template
    context = {
        'nifty_data': nifty_data,
    }

    return render(request, "card_layout.html", context)

def homepage(request):
    # Your homepage view logic here...
    return render(request, 'homepage.html')
