from django.db import models


class StudentModal(models.Model):
    stuname= models.CharField(max_length=50)
    email= models.CharField(max_length=50)

    def __str__(self):
        return self.stuname
    
