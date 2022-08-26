from django.db import models

# Create your models here.
class Experience(models.Model):
    company = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=100)
    details = models.CharField(max_length=500)
    

    def __str__(self):
        return f'{self.title} at {self.company} from {self.date}.'

class Education(models.Model):
    school = models.CharField(max_length=200)
    date = models.DateField()
    level = models.CharField(max_length=100)

    def __str__(self):
        return f'Recieved a {self.level} from {self.school} on {self.date}'