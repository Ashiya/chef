from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import  make_password
from django.core.exceptions import ObjectDoesNotExist

from chef.models import Chef, Recipe
from chef.serializers import RecipeSerializer, CreateChefSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.renderers import JSONRenderer


# Create your views here.

class CreateChef(GenericAPIView):

	serializer_class = CreateChefSerializer

	def create_chef(self, data):
		chef_object = Chef(email=data["email"], name=data["name"], password=data["password"], specialized_in=data["specialization"])
		chef_object.save()


	def get_error_response(self):

		return Response(
			self.serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def get_response(self):

		return Response({
			"message":"Chef has been created"
			}, status=status.HTTP_200_OK)

	def post(self, request, *args, **kwargs):

		self.serializer = self.get_serializer(data=self.request.data)

		if not self.serializer.is_valid():

			return self.get_error_response()
		else:
			self.create_chef(self.serializer.data)
			return self.get_response()


class CreateRecipe(GenericAPIView):

	serializer_class = RecipeSerializer
	authentication_classes = (TokenAuthentication,)

	def create_recipe(self, request, data):
		
		receipe_object = Recipe(name=data["name"], chef=self.chef_object, steps_to_make=data["steps_to_make"], meta_data=data["meta_data"])
		receipe_object.save()

	def get_recipe_error(self):

		return Response({"message":"Recipe does not exist"} , status=status.HTTP_400_BAD_REQUEST)

	def get_recipe_query(self, pk):

		try:
	 		return Recipe.objects.get(id=pk)
	 	except ObjectDoesNotExist:
	 		return None
	 	

	def get_chef_query(self, pk):

		try:
	 		self.chef_object = Chef.objects.get(id=pk)
	 	except ObjectDoesNotExist:
	 		self.chef_object = None
	 	return self.chef_object


	def get_response(self):
		return Response(
			{"message":"Receipe has been created"}, status= status.HTTP_200_OK)

	def get_error_response(self):

		return Response(self.serializer.errors , status=status.HTTP_400_BAD_REQUEST)

	def get(self, request, pk, *args, **kwargs):

		recipe_object = self.get_recipe_query(pk)
		print pk
		print recipe_object
		if not recipe_object:
			return self.get_recipe_error()
		else:
			# import pdb; pdb.set_trace()
			self.serializer = self.get_serializer(data=JSONRenderer().render(recipe_object))
			if not self.serializer.is_valid():
				return self.get_error_response()
			else:
				return Response(self.serializer.data, status=status.HTTP_200_OK)



	def post(self, request, *args, **kwargs):

		self.serializer = self.get_serializer(data=self.request.data)
		if not self.serializer.is_valid():
			return self.get_error_response()
		else:
			a = self.get_chef_query(self.serializer.data["chef"])
			if not a:
				return Response({"message":"Chef does not exists"}, status=status.HTTP_400_BAD_REQUEST)
			self.create_recipe(request, self.serializer.data)
			return self.get_response()

	def put(self, request, pk, *args, **kwargs):
	 	obj = self.get_query(pk)
	 	if not obj:
	 		return self.get_recipe_error()
	 	else:
		 	self.serializer = self.get_serializer(data=self.request.data)
		 	if self.serializer.is_valid():

		 		return self.get_error_response()
	 		else:
	 			obj.name = self.serializer.data["name"]
	 			obj.steps_to_make = self.serializer.data["steps_to_make"]
	 			obj.chef =  self

	def delete(self, request, pk, *args, **kwrags):

		self.get_recipe_query(pk)






