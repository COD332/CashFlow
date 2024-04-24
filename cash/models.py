from django.db import models

class Cost(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    amount = models.IntegerField()
    date = models.DateField(defult = auto_now_add)
    category = models.ForeignKey('Category')

class Income(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    amount = models.IntegerField()
    date = models.DateField(defult = auto_now_add)
    source = models.ForeignKey('Source')

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

class Source(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()