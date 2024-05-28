from django.db import models
from userprofile.models import User
# Create your models here.
class Poll(models.Model):
    POLL_TYPES= (
        ("normal","normal"),
        ("closed","closed"),
        ("cash","cash")
    )
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.TextField()



class Choice(models.Model):
    poll = models.ForeignKey(Poll,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)


    voters = models.ManyToManyField(User, related_name='voters', blank=True)

    def __str__(self):
        return self.choice

