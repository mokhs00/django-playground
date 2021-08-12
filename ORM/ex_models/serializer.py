from django.db.models import fields
from rest_framework import serializers
from .models import *



class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = '__all__'



class QuestionSerializer(serializers.ModelSerializer):
    register = PersonSerializer(read_only=True)

    class Meta:
        model = Question
        fields = '__all__'