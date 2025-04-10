from django.db import models

class SignalData(models.Model):
    time = models.IntegerField()
    users = models.IntegerField()
    signal = models.FloatField()
    freq_used = models.IntegerField(default=0)

    def __str__(self):
        return f"Time: {self.time}, Users: {self.users}, Signal: {self.signal}, Frequency Used: {self.freq_used}"
