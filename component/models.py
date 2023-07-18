from django.db import models


# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Component(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    tech = models.CharField(max_length=200, null=True)
    Tags = models.ManyToManyField(Tag, related_name='+')
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    # tag_id = models.ForeignKey(Tag, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.name


     # component = models.ForeignKey(Component, null=True, on_delete=models.SET_NULL)
    #Tags = models.ForeignKey(Tag, null=True, on_delete=models.SET_NULL)
