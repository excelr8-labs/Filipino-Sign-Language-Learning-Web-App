from django.db import models

class Word(models.Model):
    text = models.CharField(max_length=100)
    definition = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    gif = models.URLField(blank=True, null=True)  # Field to store a URL for a GIF related to the word

    def __str__(self):
        return self.text
