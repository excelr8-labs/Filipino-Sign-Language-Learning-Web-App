from django.db import models

class Word(models.Model):
    name = models.CharField(max_length=100)
    definition = models.TextField()
    gif = models.URLField(blank=True, null=True)  # Field to store GIF URL
    

    def __str__(self):
        return self.name
