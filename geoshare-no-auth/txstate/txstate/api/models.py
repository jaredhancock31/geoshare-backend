from __future__ import unicode_literals

from django.db import models


MAX_NAME_LEN = 25
MAX_DATA_LEN = 200


class Droplet(models.Model):
    """
    This is the model for a data drop instance that represents a row in the DDrop table
    of the database
    """

    drop_id = models.AutoField(primary_key=True)
    owner = models.CharField(max_length=MAX_NAME_LEN)
    latitude = models.FloatField()
    longitude = models.FloatField()
    data = models.TextField(max_length=MAX_DATA_LEN)
    # timestamp = models.TextField(max_length=MAX_DATA_LEN)

    def __unicode__(self):
        return self.drop_id

    def __str__(self):
        return self.drop_id
