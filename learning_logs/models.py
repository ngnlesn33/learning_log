from django.contrib.auth.models import User
from django.db import models


class Topic(models.Model):
    """The topic the user is learning about."""

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Entry(models.Model):
    """Some specific learned about a topic"""

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, blank=False)
    text = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        """Return a simple string representing the entry."""

        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        return self.text
