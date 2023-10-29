from django.contrib import admin
from django.contrib.auth.models import Group

from . import models

admin.site.register(models.Profile)
admin.site.register(models.Project)
admin.site.register(models.Skill)
admin.site.register(models.Comment)
admin.site.register(models.Tag)
admin.site.unregister(Group)


'''
import time
import datetime
import os

from django.db import models
from django.urls import path

from . import utils
'''
