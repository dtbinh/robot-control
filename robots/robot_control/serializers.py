from models import *
from rest_framework import serializers

class SessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Session
        fields = ('start', 'end', 'num_votes')

class VotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Votes
        fields = ('robot', 'vote_date', 'session', 'vote', 'username')

class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'joined', 'is_active', 'is_staff', 'control_robot')

class SessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Session
        fields = ('start', 'end', 'num_votes')

class RobotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Robot
        fields = ('name',)
