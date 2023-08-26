from django.db import models

# Create your models here.
class Message(models.Model):
    username = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)
    room = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.username
    class Meta:
        ordering = ['-date']
