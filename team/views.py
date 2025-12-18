from django.shortcuts import render
from .models import TeamMember

def team_view(request):
    team_members = TeamMember.objects.filter(is_active=True)
    bridesmaids = team_members.filter(role__in=['bridesmaid', 'maid_of_honor'])
    groomsmen = team_members.filter(role__in=['groomsman', 'best_man'])
    return render(request, 'team/team.html', {
        'bridesmaids': bridesmaids,
        'groomsmen': groomsmen
    })
