from music_project.profiles import views
from django.urls import path

from music_project.profiles.views import profile_details, profile_delete

urlpatterns = [
    path('details/', profile_details, name='profile-details'),
    path('delete/', profile_delete, name='profile-delete'),

]
