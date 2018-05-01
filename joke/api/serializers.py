from joke.models import Category,Language,Joke

from rest_framework.serializers import (
	ModelSerializer, 
	SerializerMethodField,
	)

class JokeListSerializer(ModelSerializer):
	class Meta:
		model = Joke
		fields = [
		'language',
		'title',
		'joke',
		'category',
		'rating',
		]

