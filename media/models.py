from django.db import models


class Conversation(models.Model)
    datestart = DateField()
    datelast = Datefield()
    ForeignKey(Friend, on_delete=models.CASCADE)


class Message(models.Model)
    order = models.IntegerField()
    datetime = models.DateField()
    content = models.TextField()






# Create your models here.
