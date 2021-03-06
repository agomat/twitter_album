from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# If this file grows up, consider to split these classes into multiple files
# I left the model classes in a single file for exercise purpose


class Owner(models.Model):
    name = models.CharField(max_length=128)
    screen_name = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name_plural = 'owners'

    def __unicode__(self):  # python 2.*
        return '%s, %s' % (self.name, self.screen_name)


class Album(models.Model):
    topic_name = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name_plural = 'album'

    def __unicode__(self):  # python 2.*
        return self.topic_name


class Photo(models.Model):
    tw_id = models.IntegerField(unique=True) # btw not mandatory to be unique; every time we need Min(tw_id)
    media_url = models.URLField(max_length=100, unique=True)
    favorite_count = models.IntegerField(null=True, default=0)
    first_seen = models.DateTimeField(default=timezone.now, blank=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'photos'

    def as_dict(self):
        return {
            "id": self.tw_id,
            "media_url": self.media_url,
            "favorite_count": self.favorite_count,
            "first_seen": self.first_seen.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

    def __unicode__(self):  # python 2.*
        return '%s, %s %s' % (self.media_url, self.favorite_count, self.first_seen)

