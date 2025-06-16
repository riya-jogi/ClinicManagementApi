from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from django.contrib.auth.hashers import make_password

class RegisterView(APIView):
    def post(self, request):
        data = request.data
        data['password'] = make_password(data['password'])
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"})
        return Response(serializer.errors)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data)
        return Response(serializer.errors)

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        print(request.user)
        return Response({"message": f"Welcome, {request.user.name}!"})
    
    # def get(self, request):
    #     print("Inside get() of protected class")
    #     reg_data = User.objects.all()
    #     serializer = RegisterSerializer(reg_data,many=True)
    #     print(serializer.data)
    #     return Response(serializer.data)