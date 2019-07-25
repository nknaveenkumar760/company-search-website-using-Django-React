from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LoginPageSerializer
from login.models import LoginPage

class LoginAPIView(APIView):
    def post(self, request, format=None):
        serializer = LoginPageSerializer(data=request.data)

        if serializer.is_valid():
           serializer.save()
           return Response("data is saved successfully")
        else:
            return Response("Some thing is wrong please")