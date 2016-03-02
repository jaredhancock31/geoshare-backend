from __future__ import unicode_literals

from django.db import models

MAX_NAME_LEN = 25
MAX_DATA_LEN = 200


class User(models.Model):
    """
    This is the model for a User instance that represents a row in the User table
    of the database
    """

    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=MAX_NAME_LEN)
    surname = models.CharField(max_length=MAX_NAME_LEN)
    email = models.EmailField(unique=True)

    def __unicode__(self):
        return self.email

    def __str__(self):
        return self.email


class Droplet(models.Model):
    """
    This is the model for a data drop instance that represents a row in the DDrop table
    of the database
    """

    drop_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User)
    latitude = models.FloatField()
    longitude = models.FloatField()
    data = models.TextField(max_length=MAX_DATA_LEN)
    timestamp = models.TextField()
    # timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return self.drop_id

    def __str__(self):
        return self.drop_id


