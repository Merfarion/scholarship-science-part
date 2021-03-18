from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def get_first(request):
    if request.method == "GET":
        data = [
        { "id": 0, "field1": "f1", "field2": "value 2" },
        { "id": 0, "field1": "f1", "field": "field2" }
        ]

        return JsonResponse(data, safe=False)

    elif request.method == "POST":
        data = {
        "id": 4,
        "field1": json.loads(request.body)["field1"],
        "field2": json.loads(request.body)["field2"]
        }

        return JsonResponse(data, safe=False)

def get_index(request, id):
    data = {
    "id": id,
    "field1": "value",
    "field2": "value 2"
    }
    return JsonResponse(data, safe=False)