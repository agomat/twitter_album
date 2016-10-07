# This class should be the only of this package to use app/Model

from django.core.exceptions import *

from app.models import Owner, Album, Photo


class DataAccess(object):

    @staticmethod
    def get_since_id_or_none(topic_name):
        album, created = Album.objects.get_or_create(topic_name=topic_name)
        return album.since_id

    @staticmethod
    def save_since_id(topic_name, since_id):
        album = Album.objects.get(topic_name=topic_name)
        album.since_id = since_id
        album.save()