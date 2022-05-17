# ~/webpage/views.py

from django.shortcuts import render
from rest_framework.views import APIView


class Main(APIView):
    def get(self, request):
        return render(request, "index.html")

class Programing(APIView):
    def get(self, request):
        return render(request, "webpage/Programing.html")

class SeTA(APIView):
    def get(self, request):
        return render(request, "webpage/SeTA.html")