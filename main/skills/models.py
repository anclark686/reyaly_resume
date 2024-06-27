from django.db import models

# Create your models here.
class Skills(models.Model):
    skill = models.CharField(max_length=100)
    type = models.CharField(max_length=100)


    def __str__(self):
        return f'{self.type}: {self.skill}'
    

class Certification(models.Model):
    program = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    date = models.DateField()
    link = models.CharField(max_length=500)
    

    def __str__(self):
        return f'Recieved a {self.title} certification from {self.program} on {self.date}'