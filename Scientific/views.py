
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import psycopg2
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from uuid import uuid4
from .models import *
from .serializers import *
from .settings import FILES_DIR

from Scientific.models import Scientific_Research_Work, Patent, Grant, Publications, Files
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from functools import wraps
import jwt
from rest_framework import viewsets
from django.http import JsonResponse


class ScientificViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Scientific.objects.all()
    serializer_class = ScientificSerializer


def get_token_auth_header(request):
    """Obtains the Access Token from the Authorization Header
    """
    auth = request.META.get("HTTP_AUTHORIZATION", None)
    parts = auth.split()
    token = parts[1]

    return token

def requires_scope(required_scope):
    """Determines if the required scope is present in the Access Token
    Args:
        required_scope (str): The scope required to access the resource
    """
    def require_scope(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = get_token_auth_header(args[0])
            decoded = jwt.decode(token, verify=False)
            if decoded.get("scope"):
                token_scopes = decoded["scope"].split()
                for token_scope in token_scopes:
                    if token_scope == required_scope:
                        return f(*args, **kwargs)
            response = JsonResponse({'message': 'You don\'t have access to this resource'})
            response.status_code = 403
            return response
        return decorated
    return require_scope


@api_view(['GET'])
@permission_classes([AllowAny])
def public(request):
    return JsonResponse({'message': 'Hello from a public endpoint! You don\'t need to be authenticated to see this.'})


@api_view(['GET'])
def private(request):
    return JsonResponse({'message': 'Hello from a private endpoint! You need to be authenticated to see this.'})


@api_view(['GET'])
@requires_scope('read:messages')
def private_scoped(request):
    return JsonResponse({'message': 'Hello from a private endpoint! You need to be authenticated and have a scope of read:messages to see this.'})


# Create your views here.


@csrf_exempt
@api_view(['GET', 'POST'])
def get_data(request):
    if request.method == 'GET':

        user_id = '1'

        grantser = GrantSerializer(Grant.objects.filter(user=user_id).all(), many=True)
        publicationser = PublicationSerializer(Publications.objects.filter(user=user_id).all(), many=True)
        patentser = PatentSerializer(Patent.objects.filter(user=user_id).all(), many=True)
        researchser = ResearchWorkSerializer(Scientific_Research_Work.objects.filter(user=user_id).all(), many=True)
        
        return JsonResponse({'Grants': grantser.data, 'Publications': publicationser.data, 'Patents': patentser.data, 'Research_works': researchser.data}, safe=False)


@api_view(['GET', 'POST'])
def add_grants(request):
    if request.method == 'POST':
        try:
            for i in request.data:
                serializer = GrantSerializer(data= i)
                if serializer.is_valid():
                    serializer.save()
                else:
                    raise TypeError
            return JsonResponse(request.data, status=status.HTTP_201_CREATED, safe=False)
        except:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        return JsonResponse({'Method': 'add_grants'})


@api_view(['GET', 'POST'])
def add_researchWorks(request):
    if request.method == 'POST':
        try:
            for i in request.data:
                serializer = ResearchWorkSerializer(data= i)
                if serializer.is_valid():
                    serializer.save()
                else:
                    raise TypeError
            return JsonResponse(request.data, status=status.HTTP_201_CREATED, safe=False)
        except:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        return JsonResponse({'Method': 'add_researchWorks'})


@api_view(['GET', 'POST'])
def add_patents(request):
    if request.method == 'POST':
        try:
            for i in request.data:
                serializer = PatentSerializer(data= i)
                if serializer.is_valid():
                    serializer.save()
                else:
                    raise TypeError
            return JsonResponse(request.data, status=status.HTTP_201_CREATED, safe=False)
        except:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        return JsonResponse({'Method': 'add_patents'})


@api_view(['GET', 'POST'])
def add_publications(request):
    if request.method == 'POST':
        try:
            for i in request.data:
                serializer = PublicationSerializer(data= i)
                if serializer.is_valid():
                    serializer.save()
                else:
                    raise TypeError
            return JsonResponse(request.data, status=status.HTTP_201_CREATED, safe=False)
        except:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        return JsonResponse({'Method': 'add_publications'})


@api_view(['GET', 'POST'])
def add_file(request):
    if request.method == 'POST':
        try:
            for (file_name, f) in request.FILES.items():
                owner = 123 # REPLACE IT
                file_uuid = str(uuid4())
                with open(FILES_DIR + file_uuid, 'wb+') as destination:
                    for chunk in f.chunks():
                        destination.write(chunk)
                
                db_record = Files()
                db_record.owner = owner
                db_record.file_name = file_name
                db_record.file_uuid = file_uuid
                db_record.save()
            return JsonResponse({'UUID': file_uuid}, status=status.HTTP_201_CREATED)
        except:
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        return JsonResponse({'Method': 'add_file'})


@api_view(['GET'])
def showGrants(request):
    '''
    Example for serializer
    '''
    if request.method == 'GET':
        show = Grant.objects.filter(user = 1).all()
        serializer = GrantSerializer(show, many=True)
        return JsonResponse(serializer.data, safe=False)