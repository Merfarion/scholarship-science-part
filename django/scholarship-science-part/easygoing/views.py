
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
# from easygoing.simple.models import MyProject
import json
import psycopg2
from rest_framework import status

from simple.models import MyProject
from simple.serializers import MyProjectSerializer

# Create your views here.
@csrf_exempt
def get_first(request):
    if request.method == "GET":
        # data = [
        # { "id": 0, "nameProject": "f1", "status": "value 2", "place": 0 },
        # { "id": 0, "nameProject": "f1", "status": "field2", "place": 0 }
        # ]
        # data = {'projects': MyProject}
        projects = MyProject.objects.all()
        serializer = MyProjectSerializer(projects,many=True)
        return JsonResponse(serializer.data, safe=False)

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




