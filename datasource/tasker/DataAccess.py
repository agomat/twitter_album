# This class should be the only of this package to use app/Model

from django.db import IntegrityError
from django.db.models import Min, Count
from app.models import Owner, Album, Photo
from django.core.mail import get_connection, EmailMultiAlternatives


class DataAccess(object):

    @staticmethod
    def get_min_id_or_none(topic_name):
        album, created = Album.objects.get_or_create(topic_name=topic_name)
        if created:
            album.save()
            return None
        else:
            aggregation = Photo.objects.filter(album=album).aggregate(Min('tw_id'))
            return aggregation.get('tw_id__min')

    @staticmethod
    def save_photo(topic_name, tw_id, owner_name, owner_screen_name, media_url, favorite_count):

        # step 1 - Get or create Owner entity

        owner, o_created = Owner.objects.get_or_create(
            name=owner_name,
            screen_name=owner_screen_name,
        )
        if o_created:
            owner.save()

        # step 2 - Get or create Album entity

        album, a_created = Album.objects.get_or_create(
            topic_name=topic_name,
        )
        if a_created:
            album.save()

        # step 3 - Associate owner and album to photo entity

        try:
            photo = Photo.objects.create(
                tw_id=tw_id,
                media_url=media_url,
                favorite_count=favorite_count,
                album=album,
                owner=owner
            )
            photo.save()
        except IntegrityError as e:
            print '%s Photo exists already' % media_url

        # step 4 - Send mail when the counter reach precise values (Api fetching will no stop)

        aggregation = Photo.objects.filter(album=album).aggregate(Count('tw_id')) # TODO test it
        counter = aggregation.get('tw_id___count')
        if counter in [100,200,300,400,501]:
            DataAccess.send_mail( topic_name, counter )

    @staticmethod
    def send_mail(topic_name, counter): # fake
        print "SEND MAIL"
        print "%s has %d photos" % (topic_name, counter)
        print "SEND MAIL END"
        return True # do not disturb

        msg = EmailMultiAlternatives(

            "%s has %d photos" % ( topic_name, counter ),
            "I'm awesome",
            "E*ap Hashtag <Has*ag@E*er*pp.com>",
            ["<ag***t@gmail.com>"],
            "<da*de@E*er*pp.com>",
            connection=get_connection()
        )

        msg.send()
