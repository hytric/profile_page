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

class Facebook_meta(APIView):
    def get(self, request):
        return render(request, "8o2th7vj1zswq2rfw00oh4syua51s1.html")