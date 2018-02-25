from django.db import models

# Create your models here.
class User(models.Model):
    serverList = (
        ('bakal', 'bakal'),
        ('cain','cain'),
        ('casillas', 'casillas'),
        ('diregie','diregie'),
        ('hilder', 'hiler'),
        ('prey', 'prey'),
        ('siroco', 'siroco'),
    )
    characterName = models.CharField(max_length=30)
    serverName = models.CharField(max_length = 10,choices = serverList, default="cain")
    def __str__(self):
        return "name:"+self.characterName + "server:" + self.serverName
