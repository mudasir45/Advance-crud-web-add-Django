from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=20)
    department = models.CharField(max_length=20)
    section = models.CharField(max_length=5)
    subject = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return self.name