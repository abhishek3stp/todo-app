from django.db import models

# Create your models here.

class Task (models.Model):
    note = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.note
