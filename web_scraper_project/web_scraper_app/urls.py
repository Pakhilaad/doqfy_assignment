from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),  # Add this URL pattern for the homepage
    path('card-layout/', views.card_layout, name='card_layout'),
    # Add any other URL patterns as needed
]
