from django.db import models

# Create your models here.
class Skills(models.Model):
    skill = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.type}: {self.skill}'