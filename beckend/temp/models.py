from django.db import models

class SystemStat(models.Model):
   
   
    timestamp = models.DateTimeField(auto_now_add=True)  # track when data is logged
    indoor_temp = models.FloatField()
    humidity = models.FloatField()
    server_load = models.FloatField()
    external_temp = models.FloatField()
    ac_level = models.FloatField()
    fans_active = models.FloatField()
    hour = models.FloatField()  # or use DateTimeField and extract hour later

    def __str__(self):
        return f"Stat at {self.timestamp}"
