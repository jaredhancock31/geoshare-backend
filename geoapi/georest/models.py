from __future__ import unicode_literals
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from django.db import models
from django.contrib.auth.models import User

__author__ = 'jared hancock'

MAX_NAME_LEN = 25
MAX_DATA_LEN = 200


# class AppUser(models.Model):
#
#     # user_id = models.AutoField(primary_key=True)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # username = models.CharField(max_length=MAX_NAME_LEN, unique=True)
#     # email = models.EmailField(unique=True)
#
#
#     def __unicode__(self):
#         return self.user_id
#
#     def __str__(self):
#         return self.user_id


class Droplet(models.Model):
    """
    This is the model for a data drop instance that represents a row in the DDrop table
    of the database
    """

    drop_id = models.AutoField(primary_key=True)
    # owner = models.CharField(max_length=MAX_NAME_LEN)
    owner = models.ForeignKey(User)
    latitude = models.FloatField()
    longitude = models.FloatField()
    data = models.TextField(max_length=MAX_DATA_LEN)
    timestamp = models.TextField(max_length=MAX_DATA_LEN)

    def __unicode__(self):
        return self.drop_id

    def __str__(self):
        return self.drop_id
