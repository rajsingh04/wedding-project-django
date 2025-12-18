from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Teams
from .serializers import TeamsSerializer
import urllib.request
import json

@api_view(['GET'])
def home_page(req):
    return Response({"message":"Welcome to Teams API !"})

@api_view(['GET'])
def get_all_teams(req):
    teams = Teams.objects.all()
    serializer = TeamsSerializer(teams,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_teams(req):
    serializer=TeamsSerializer(data=req.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {'message':'Teams added!', 'data':serializer.data},
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_team_by_id(req,id):
    teams = get_object_or_404(Teams, id=id)
    serializer = TeamsSerializer(teams)
    return Response(serializer.data)


def public_api_view(request):
    """Fetch public API data and render it in a simple template.

    Uses https://jsonplaceholder.typicode.com/users as a sample public API
    and passes the returned JSON to the `teams_public.html` template as
    the `users` context variable.
    """
    url = 'https://jsonplaceholder.typicode.com/users'
    try:
        with urllib.request.urlopen(url, timeout=5) as resp:
            data = json.load(resp)
    except Exception:
        data = []
    return render(request, 'teams_public.html', {'users': data})