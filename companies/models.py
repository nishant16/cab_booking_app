from __future__ import unicode_literals

from django.db import models


class Cab(models.Model):
    name = models.CharField(max_length=25, null=True)
    helpline_no = models.CharField(max_length=25, null=True)
    support = models.CharField(max_length=250, null=True)
    refer_and_earn = models.CharField(max_length=100, null=True)

    def __unicode__(self):
        return self.name


class Driver(models.Model):
    name = models.CharField(max_length=50, null=True)
    cab = models.ForeignKey(Cab)
    mobile_no = models.CharField(max_length=10, null=True)

    def __unicode__(self):
        return self.name

#
# class Trip(models.Model):
#     user = models.ForeignKey('auth.User')
#     driver = models.ForeignKey(Driver)
#     booking_id = models.CharField(max_length=50)
#     travelling_from = models.CharField(max_length=50)
#     travelling_to = models.CharField(max_length=50)
#     distance_travelled = models.CharField(max_length=10)