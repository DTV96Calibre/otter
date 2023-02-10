import datetime

from django.db import models
from django.utils import timezone

class User(models.Model):
    handle = models.SlugField(max_length=15, blank=False, unique=True)
    username = models.CharField(max_length=50, blank=False)
    join_date = models.DateTimeField(editable=False)
    followed_users = models.ManyToManyField("self", related_name="followers", symmetrical=False)
    active = models.BooleanField(default=True)
    def __str__(self):
        if not active:
            return "*deactivated user*"
        return self.handle
    def joined_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.join_date <= now

class Post(models.Model):
    created_by = models.ForeignKey(
            User,
            on_delete=models.CASCADE,
            )
    response_to = models.ForeignKey(
            self,
            on_delete=models.CASCADE,
            null=True,
            default=None,
            )
    text = CharField(
            max_length=280,
            blank=True
            )
    poll = models.ForeignKey(Poll,
            on_delete=models.CASCADE,
            null=True,
            default=None,
            )
