from django.db import models

# Create your models here.


class Note(models.Model):
    title = models.CharField(blank=False, max_length=50)
    description = models.TextField(blank=False)
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'notes'
