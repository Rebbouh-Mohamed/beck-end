from django.db import models
from datetime import timedelta

class Material(models.Model):
    STATUS_CHOICES = [
        ('active', 'active'),
        ('inactive', 'inactive'),
        ('maintenance', 'maintenance'),
        ('expired', 'expired'),
    ]
    
    name = models.CharField(max_length=255)
    last_maintenance = models.DateField()
    next_maintenance = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    time_left = models.DurationField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Automatically calculate the time left before the next maintenance
        if self.next_maintenance:
            self.time_left = self.next_maintenance - self.last_maintenance
        super().save(*args, **kwargs)
