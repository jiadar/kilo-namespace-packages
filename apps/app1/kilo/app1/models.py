from django.db import models


class Master(models.Model):
    master_text = models.CharField(max_length=200)


class Slave(models.Model):
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)  # Create your models here.
