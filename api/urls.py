from django.urls import path

from .views import new_robots

app_name = 'api'

urlpatterns = [
    path('robots/', new_robots)
]
