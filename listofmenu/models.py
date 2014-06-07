from django.db import models

# Create your models here.

class Menu( models.Model):
	mealName = models.CharField( max_length = 200)
	date = models.DateTimeField()
	total_point = models.IntegerField( default = 0)
	total_vote = models.IntegerField( default = 0)

	def __unicode__( self):
		return self.date_meal

	def average_point( self):
		return self.total_point * 1.0 / self.total_vote
