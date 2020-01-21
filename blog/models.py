from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=255)
	body = models.TextField()

	def __str__(self):
		return self.title

class Article(models.Model):
	marque = models.CharField(max_length=255)
	typeVetement = models.CharField(max_length=255)
	prix = models.CharField(max_length=255)
	titre = models.TextField()

	def __str__(self):
		return self.titre

class Customer(models.Model):
	login = models.CharField(max_length=255)
	mdp = models.CharField(max_length=255)
	nom = models.CharField(max_length=255)
	prenom = models.CharField(max_length=255)
	adresse = models.CharField(max_length=255)
	dateNaissance = models.DateTimeField()

	