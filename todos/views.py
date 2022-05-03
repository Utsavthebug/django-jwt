import json
from django.shortcuts import render
from rest_framework.views import APIView
import requests
import json
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class TodoList(APIView):
    permission_classes = [IsAuthenticated]

    def getTodo(self,request):
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        todos = json.loads(response.data)
        return Response(todos)

