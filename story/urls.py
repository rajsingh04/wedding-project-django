from django.urls import path
from . import views

app_name = 'story'

urlpatterns = [
    path('', views.story_view, name='story'),
]