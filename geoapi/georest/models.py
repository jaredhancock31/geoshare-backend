from __future__ import unicode_literals
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from django.db import models
from django.contrib.auth.models import User

MAX_NAME_LEN = 25
MAX_DATA_LEN = 200


class Droplet(models.Model):
    """
    This is the model for a data drop instance that represents a row in the DDrop table
    of the database
    """

    drop_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey('auth.User', related_name='droplets')
    latitude = models.FloatField()
    longitude = models.FloatField()
    data = models.TextField(max_length=MAX_DATA_LEN)
    timestamp = models.TextField()
    # timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return self.drop_id

    def __str__(self):
        return self.drop_id

    # def save(self, *args, **kwargs):
    #     """
    #     Use the `pygments` library to create a highlighted HTML
    #     representation of the code snippet.
    #     """
    #     lexer = get_lexer_by_name(self.drop_id)
    #     linenos = self.linenos and 'table' or False
    #     options = self.title and {'title': self.title} or {}
    #     formatter = HtmlFormatter(style=self.style, linenos=linenos,
    #                               full=True, **options)
    #     self.highlighted = highlight(self.code, lexer, formatter)
    #     super(Droplet, self).save(*args, **kwargs)


# class AppUser(models.Model):
#     """
#     This is the model for a User instance that represents a row in the User table
#     of the database
#     """
#
#     user = models.OneToOneField(User)
#     user_id = models.AutoField(primary_key=True)
#     # name = models.CharField(max_length=MAX_NAME_LEN)
#     # surname = models.CharField(max_length=MAX_NAME_LEN)
#     # email = models.EmailField(unique=True)
#
#     def __unicode__(self):
#         return self.email
#
#     def __str__(self):
#         return self.email
