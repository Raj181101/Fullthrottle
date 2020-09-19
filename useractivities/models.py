from django.db import models

# Create your models here.
class User(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    real_name = models.CharField(max_length = 70)
    tz = models.CharField(max_length = 80)

    def __str__(self):
        return self.real_name

class ActivityPeriods(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.user.real_name