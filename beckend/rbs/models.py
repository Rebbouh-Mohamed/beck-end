from django.db import models

class SignalData(models.Model):
    user_count = models.IntegerField()
    time_of_day = models.IntegerField()
    signal_strength = models.FloatField()
    traffic_type = models.IntegerField()
    rbs = models.IntegerField(default=0)

    def __str__(self):
        return f"User Count: {self.user_count}, Time: {self.time_of_day}, Signal: {self.signal_strength}, Traffic Type: {self.traffic_type}, RBS: {self.rbs}"
