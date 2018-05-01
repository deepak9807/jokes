from __future__ import unicode_literals
from joke.models import Category,Language,Joke
from rest_framework.views import APIView
from .serializers import JokeListSerializer
from rest_framework.decorators import api_view
from rest_framework import status

from rest_framework.filters import (
	SearchFilter,
	OrderingFilter,
	)

from django.db.models import Q
from rest_framework.generics import (
	DestroyAPIView,
	ListAPIView, 
	UpdateAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView,
	CreateAPIView,

	)
class JokeListAPIView(ListAPIView):
	queryset = Joke.objects.all()
	serializer_class  = JokeListSerializer

class LangListAPIView(ListAPIView):
	serializer_class  = JokeListSerializer
	
	def get_queryset(self):
		#language = 2
		queryset_list = Joke.objects.all()
		language = self.kwargs['language']
		print(language)
		if language is not None:
			queryset = queryset_list.filter(language=language)
		return queryset