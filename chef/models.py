from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Create your models here.

class CreationInfo(models.Model):

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	

	class Meta:

		abstract = True



class Chef(CreationInfo):

	email = models.EmailField()
	password = models.CharField(max_length=100)
	name = models.CharField(max_length=100)

	CHINEASE = "Chinease"
	ITALIAN = "Italian",
	SOUTH_INDIAN = "South_Indian",
	MAXICAN = "Maxican"

	specialization = (
		(CHINEASE, "Chinease"),
		(ITALIAN, "Italian"),
		(SOUTH_INDIAN, "South_Indian"),
		(MAXICAN, "Maxican"))

	specialized_in = models.CharField(max_length=15, choices=specialization)

	def __unicode__(self):
		return self.name
	
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Recipe(CreationInfo):

	name = models.CharField(max_length=200)
	steps_to_make = models.TextField()
	chef = models.ForeignKey(Chef)
	meta_data = models.TextField(null=True, blank=True)


