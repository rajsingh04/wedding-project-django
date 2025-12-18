from django.urls import path
from . import views
urlpatterns = [
    path('', views.get_all_teams, name='get_all_teams'),
    path('add/', views.add_teams, name='add_teams'),
    path('public/', views.public_api_view, name='teams_public'),
    path('<int:id>', views.get_team_by_id, name='get_team_by_id'),
]