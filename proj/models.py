from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class MyModelName(models.Model):
    name = models.CharField(max_length=20, help_text='Enter your name')
    CHOICES = (
        ('rock', 'ROCK'),
        ('paper', 'PAPER'),
        ('scissors', 'SCISSORs'),
    
    )
    user_choice = models.CharField(max_length=10, choices=CHOICES)
    comp_choice=models.CharField(max_length=10, choices=CHOICES)
    user_score=models.IntegerField(blank=True,null=True)
    comp_score=models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.name