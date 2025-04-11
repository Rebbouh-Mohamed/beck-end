from django.db import models

class LogEntry(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return f"[{self.timestamp}] {self.status} - {self.description[:50]}"
