from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
# Create your views here.


@api_view(['GET'])
def endpoints(request):
    data = ['/advocates', 'advocates/:username']
    return Response(data)

@api_view(['GET'])
def advocates(request):
    data = ['Dennis', 'Ann']
    return JsonResponse(data, safe=False)

@api_view(['GET'])
def advocate_details(request, username):
    data = username
    return JsonResponse(data, safe=False)