from .serializer import *
from .models import Person, Question
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import datetime
# Create your views here.

@api_view(['GET','POST'])
def person(request): 
    if request.method == 'GET':
        person = Person.objects.all()

        response = PersonSerializer(person, many=True).data
        print(response)

        return Response(response)

    elif request.method == 'POST':
        print(request.data)
        serializer = PersonSerializer (data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def question(request):

    if request.method == 'GET':
        question = Question.objects.all()

        response = QuestionSerializer(question, many=True).data
        print(response)

        return Response(response)

    elif request.method == 'POST':
        print(request.data)

        print(request.data['register_id'])

        q = Question(register_id=request.data['register_id'], \
                 question_text=request.data['question_text'])
        
        q.save()

        # serializer = QuestionSerializer(data=request.data)
        # print(serializer.data)
        
        # if serializer.is_valid():
            # serializer.save()
        serializer = QuestionSerializer(q)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
