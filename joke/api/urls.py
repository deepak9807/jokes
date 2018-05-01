from django.contrib import admin
from django.conf.urls import url

app_name = 'joke.api'



from .views import (
    JokeListAPIView,
    #,
    LangListAPIView
    )
urlpatterns = [
	url(r'^jokes/$',JokeListAPIView.as_view(), name="list"),
	url(r'^jokes/(?P<language>\d+)/$',LangListAPIView.as_view(), name="language"),
	
     
    # url(r'^(?P<id>\d+)/delete/',comment_delete, name="delete"),

]