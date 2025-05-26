from django.urls import path

from .views import *

app_name = 'leaderboard'

urlpatterns = [
    path('results/get-competition-result/', ResultsView.as_view(), name='get_competition_result')
]