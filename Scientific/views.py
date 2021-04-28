
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


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)
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