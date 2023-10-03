from django.urls import path

from .views import get_robots_timedelta

app_name = 'api'

urlpatterns = [
    path('robots_excel/', get_robots_timedelta),
]
