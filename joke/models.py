from django.db import models

# Create your models here.

class Category(models.Model):
	category = models.CharField("Category of Joke", max_length=50,default="joke")
	def __str__(self):
		return str(self.category)

class Language(models.Model):
	language = models.CharField("Language",default="Hindi",max_length=20)
	def __str__(self):
		return str(self.language)

class Joke(models.Model):
	language 	= models.ForeignKey(Language,on_delete=models.CASCADE,default=1)
	title 		= models.CharField("Title of joke",max_length=50,null= True)
	joke 		= models.CharField("Joke story", max_length=1000)
	category 	= models.ForeignKey(Category, on_delete=models.CASCADE,default="joke")
	keywords    = models.CharField("Keywords of joke",max_length=50)
	rating 		= models.IntegerField()
	create_date = models.DateField(auto_now_add=True)

	def __str__(self):
		return str(self.joke)
