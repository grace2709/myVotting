# from django.db import models
# from userprofile.models import User
# # Create your models here.
# class Poll(models.Model):
#     POLL_TYPES= (
#         ("normal","normal"),
#         ("closed","closed"),
#         ("cash","cash")
#     )
#     owner = models.ForeignKey(User,on_delete=models.CASCADE)
#     name = models.CharField(max_length=30)
#     description = models.TextField()
#
#
#     voters = models.ManyToManyField(User,related_name='voters',blank=True)
#
#
#
# class Choice(models.Model):
#     poll = models.ForeignKey(Poll,on_delete=models.CASCADE)
#     choice = models.CharField(max_length=30)
#     votes = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.choice
#
