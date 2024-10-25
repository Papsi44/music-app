from django.urls import path

from music_project.common.views import home

urlpatterns = [
    path('', home, name='home'),
]
