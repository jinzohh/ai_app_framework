from django.db import models

# Create your models here.
class Chatbot(models.Model):
    inputMsg = models.TextField(blank=True, null=True)
    outputMsg = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class Inputoutput(models.Model):
    inputMsg1 = models.TextField(blank=True, null=True)
    inputMsg2 = models.TextField(blank=True, null=True)
    inputMsg3 = models.TextField(blank=True, null=True)
    inputMsg4 = models.TextField(blank=True, null=True)
    outputMsg1 = models.TextField(blank=True, null=True)
    outputMsg2 = models.TextField(blank=True, null=True)
    outputMsg3 = models.TextField(blank=True, null=True)
    outputMsg4 = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)