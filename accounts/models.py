from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# class Children(models.Model):
#
#
#

class Counsellor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=128)
    secret_key = models.CharField(max_length=128)
    lists = models.TextField()
    timetable = models.TextField()
    def __str__(self):
        return self.name

    # @staticmethod
    # def create(secret_key, user_id=None, user_firstname=None):
    #     if user_id:
    #         user = User.objects.get by pk
    #     elif user_firstname and user_lastname:
    #         user = User.objects.create(user_firstname)
    #
    #     counsellor = Counsellor.objects.create(user, )
