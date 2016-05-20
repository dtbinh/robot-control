from django.shortcuts import render
from lazysignup.decorators import allow_lazy_user
from django.http import Http404
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from models import *
from serializers import *

# Create your views here.

@allow_lazy_user
def index(request):
    Sessions.objects.all().last()
    return HttpResponse(request.user.username)

@api_view(['GET','POST'])
@permission_classes((permissions.AllowAny,))
def votes_list(request, session_id=None):
    if request.method == 'GET':
        votes=[]
        if session_id is not None:
            votes = Votes.objects.filter(session=session_id)
        else:
            votes = Votes.objects.all()
        serializer = VotesSerializer(votes, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = VotesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SessionList(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, format=None):
        sessions = Session.objects.all()
        serializer = SessionSerializer(sessions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SessionDetail(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self, pk):
        try:
            return Session.objects.get(pk=pk)
        except Session.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        session=self.get_object(1)
        if pk=='0':
            session = Session.objects.all().last()
        else:
            session = self.get_object(pk)
        serializer = SessionSerializer(session)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        session=self.get_object(1)
        if pk=='0':
            session = Session.objects.all().last()
        else:
            session = self.get_object(pk)
        serializer = SessionSerializer(session, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RobotList(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, format=None):
        robots = Robot.objects.all()
        serializer = RobotSerializer(robots, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RobotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VotesViewSet(viewsets.ModelViewSet):
    queryset = Votes.objects.all()
    serializer_class = VotesSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
