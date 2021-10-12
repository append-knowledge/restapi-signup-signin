from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SigninSerializer,UserCreateSerializer
from .models import MyUser
from django.contrib.auth import authenticate,login

# Create your views here.
class SignUpViews(generics.GenericAPIView,mixins.CreateModelMixin):
    model=MyUser
    serializer_class = UserCreateSerializer

    def post(self,request,*args,**kwargs):
        return self.create(request, *args, **kwargs)
        return Response({'msg':'user created'})


class SigninView(APIView):
    serializer_class=SigninSerializer

    def post(self,request,*args,**kwargs):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            email=serializer.validated_data['email']
            password=serializer.validated_data['password']
            user=authenticate(request,username=email,password=password)
            if user:
                login(request,user)
                return Response({'msg':'login success'},status=status.HTTP_201_CREATED)
            else:
                return Response({'msg':'login failed'},status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'msg':'user doesnot exist'},status=status.HTTP_400_BAD_REQUEST)




