from django.db import models


class Sphere(models.Model):
    sphere_text = models.CharField(max_length=200)


class Cylinder(models.Model):
    master = models.ForeignKey("app1.Master", on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)  # Create your models here.
