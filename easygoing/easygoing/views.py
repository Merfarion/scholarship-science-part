import select
import sqlite3
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import models
from easygoing.simple.models import *
import json
import psycopg2
# Create your views here.
@csrf_exempt
def get_first(request):
    if request.method == "GET":
        # data = [
        # { "id": 0, "nameProject": "f1", "status": "value 2", "place": 0 },
        # { "id": 0, "nameProject": "f1", "status": "field2", "place": 0 }
        # ]
        data = {'projects': MyProject}

        return JsonResponse(data, safe=False)

    elif request.method == "POST":
        data = {
        "id": 4,
        "status": json.loads(request.body)["field2"],
        "place": 5
        }


        return JsonResponse(data, safe=False)

def get_index(request, id):
    data = {
    "id": id,
    "status": "value 2",
    "place": 5
    }
    return JsonResponse(data, safe=False)