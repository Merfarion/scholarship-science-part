
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import psycopg2
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *


from Scientific.models import Scientific_Research_Work, Patent, Grant, Publications

# Create your views here.


@api_view(['GET', 'POST'])
def get_data(request):
    if request.method == 'GET':
        grant_list = []
        publications_list = []
        patent_list = []
        research_work_list = []
        user_id = '1'
        
        for p in Grant.objects.filter(user=user_id):
            grant_list.append({"title": p.title, 'individual_team': p.individual_team, 'RTU_reward': p.RTU_reward, 'date': p.date, 'scores': (p.scores if p.scores > -1 
            else 0)})
        for p in Publications.objects.filter(user=user_id):
            publications_list.append({'title': p.title, 'volume_title': p.volume_title, 'level': p.level, 'authors_quantity': p.authors_quantity, 'date': p.date, 'scores': (p.scores if p.scores > -1 
            else 0)})
        for p in Patent.objects.filter(user=user_id):
            patent_list.append({'title': p.title, 'individual_team': p.individual_team, 'RTU_reward': p.RTU_reward, 'date': p.date, 'scores': (p.scores if p.scores > -1 
            else 0)})
        for p in Scientific_Research_Work.objects.filter(user=user_id):
            research_work_list.append({'title': p.title, 'place': p.title, 'individual_team': p.individual_team, 'RTU_reward': p.RTU_reward, 'date': p.date, 'scores': (p.scores if p.scores > -1 
            else 0)})
        
        return JsonResponse({'Grants': grant_list, 'Publications': publications_list, 'Patents': patent_list, 'Research_works': research_work_list}, safe=False)


@api_view(['GET', 'POST'])
def add_grants(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        grant = Grant()
        grant.title = data['title']
        grant.individual_team = data['individual_team']
        grant.RTU_reward = data['RTU_reward']
        grant.date = data['date']
        grant.user = data['user']
        grant.save()
        return JsonResponse({'Status': 'Confirmed'})
