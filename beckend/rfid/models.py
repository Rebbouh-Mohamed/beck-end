from django.db import models

class RFID(models.Model):
    id_rfid = models.CharField(max_length=100)  # RFID ID
    name = models.CharField(max_length=255)  # Name of the person or entity
    last_access = models.DateTimeField(auto_now=True)  # Timestamp for the last access
    is_active = models.BooleanField(default=True)  # Whether the RFID is active or not

    def __str__(self):
        return f"RFID {self.id_rfid} - {self.name} (Active: {self.is_active})"
