from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

MAX_NAME_LEN = 25
MAX_DATA_LEN = 200


class Droplet(models.Model):
    """
    This is the model for a Droplet instance that represents a row in the DDrop table
    of the database
    """

    drop_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User)
    latitude = models.FloatField()
    longitude = models.FloatField()
    data = models.TextField(max_length=MAX_DATA_LEN)

    def __unicode__(self):
        return self.drop_id

    def __str__(self):
        return self.drop_id
