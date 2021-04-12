
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import psycopg2
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Scientific.models import MyProject
from Scientific.serializers import MyProjectSerializer
from Scientific.models import MyProject

# Create your views here.
@csrf_exempt
def get_first(request):
    if request.method == "GET":
        message_list = []
        for p in MyProject.objects.raw('SELECT id, place, status FROM simple_myproject'):
            message_list.append({'id': p.id, 'place': p.place, 'status': p.status})
        return JsonResponse(test_list, safe=False)

    elif request.method == "POST":
        # data = {
        # "id": 4,
        # "status": json.loads(request.body)["field2"],
        # "place": 5
        # }
        serializer = MyProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_index(request, id):
    # data = {
    # "id": id,
    # "status": "value 2",
    # "place": 5
    # }
    projects = MyProject.objects.get(id)
    serializer = MyProjectSerializer(projects, many=True)
    return JsonResponse(serializer.data, safe=False)




# @api_view(['GET', 'POST'])
# def project_list(request):
#     if request.method == 'GET':
#         projects = MyProject.objects.all()
#         se