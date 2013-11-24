from django.db import models

# Create your models here.
class TodoEntry(models.Model):
     task = models.CharField(max_length=120)
     status = models.IntegerField()
     create_date = models.DateTimeField('create date')

     def __unicode__(self):
          return self.task

     def IsOpen(self):
          return (self.status == 1)

