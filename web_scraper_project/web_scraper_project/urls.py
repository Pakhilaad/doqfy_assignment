# web_scraper_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web_scraper_app.urls')),  # Add this line to include the app's URLs
]

