from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import *
from rest_framework.views import APIView
from django.db.models import Q
from .serializers import *
# Create your views here.


@api_view(['GET'])
def endpoints(request):
    data = ['persones', 'persones/name']
    return Response(data)

@api_view(['GET', 'POST'])
def persons(request):
    if request.method == 'GET':
        query = request.GET.get('query') # забираем данные для фильтрации из url
        if query == None:
            query = ''
        # осуществляем фильтрацию по нахождению данных из url в данных из бд
        persons = Person.objects.filter(Q(name__icontains=query)| Q(bio__icontains=query))
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        person = Person.objects.create(name=request.data['name'], bio=request.data['bio'])
        serializer = PersonSerializer(person, many=False)
        return Response(serializer.data)

class person_details(APIView):
    def get_object(self, name):
        try:
            return Person.objects.get(name=name)
        except Person.DoesNotExist:
            raise JsonResponse('Человек не найден')
    def get(self, request, name):
        person = Person.objects.get(name=name)
        serializer = PersonSerializer(person, many=False)
        return Response(serializer.data)
    def put(self, request, name):
        person = Person.objects.get(name=name)
        person.name = request.data['name']
        person.bio = request.data['bio']
        person.save()
        serializer = PersonSerializer(person, many=False)
        return Response(serializer.data)
    def delete(self, request, name):
        person = Person.objects.get(name=name)
        person.delete()
        return redirect('persons')

@api_view(['GET'])
def sections(request):
    sections = Section.objects.all()
    serializer = SectionSerializer(sections, many=True)
    return Response(serializer.data)