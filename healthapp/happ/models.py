from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class userModel(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	'''
	alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric')
	bID = models.CharField(
		max_length=8, validators=[alphanumeric], primary_key=True
	)
	'''
	age = models.IntegerField()

	def __str__(self):
		return '%s %s' % (self.user, self.age)
