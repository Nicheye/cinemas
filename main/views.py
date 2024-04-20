from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import  status
from .models import *
from .serializers import *
import random
from rest_framework import filters



class Main_View(APIView):
	def get(self,request,*args,**kwargs):
		id = kwargs.get('id',None)
		
		if id is not None:
			cinema_obj = Cinema.objects.get(id=id)
			ser=  Cinema_serializer(cinema_obj)
			return Response({'data':ser.data},status=status.HTTP_200_OK)
		else:
			cinemas = Cinema.objects.all()
			ser = Cinema_serializer(cinemas,many=True)
			return Response({'data':ser.data},status=status.HTTP_200_OK)
	def post(self,request,*args,**kwargs):
		data = request.data
		ser = Cinema_serializer(data=data)
		if ser.is_valid(raise_exception=True):
			map= data['map']
			ser.save(map=map)
			return Response({'data':ser.data},status=status.HTTP_201_CREATED)
	
	def patch(self,request,*args,**kwargs):
		data =request.data
		id = kwargs.get('id',None)
		if id is not None:
			cinema= Cinema.objects.get(id=id)
			if cinema:
				ser = Cinema_serializer(cinema,data=data)
				if ser.is_valid(raise_exception=True):
					map = data['map']
					ser.save(map=map)
					return Response({'data':ser.data},status=status.HTTP_202_ACCEPTED)
			else:
				return Response({'message':"we couldnt find such cinema"},status=status.HTTP_400_BAD_REQUEST)	
		else:
			return Response({'message':"you havent provided id to update it"},status=status.HTTP_400_BAD_REQUEST)
		
	
	def delete(self,request,*args,**kwargs):
		id = kwargs.get('id',None)
		if id is not None:
			cinema_obj = Cinema.objects.get(id=id)
			if cinema_obj:
				ser  = Cinema_serializer(cinema_obj)
				return Response({'data':ser.data},status=status.HTTP_202_ACCEPTED)
			else:
				return Response({'message':"we couldnt find such cinema"},status=status.HTTP_400_BAD_REQUEST)
		else:
			return Response({'message':"you havent provided id to update it"},status=status.HTTP_400_BAD_REQUEST)

	



class Search_View(ListAPIView):
    queryset = Cinema.objects.all()
    serializer_class = Cinema_serializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'location','street','ur_name','website','inn','map']