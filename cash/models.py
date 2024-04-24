from django.db import models

class Cost(models.Model):
    def __str__(self):
        return self.title
    
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)

class Income(models.Model):
    def __str__(self):
        return self.title
    
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    source = models.ForeignKey('Source', on_delete=models.PROTECT)

class Category(models.Model):
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

class Source(models.Model):
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)