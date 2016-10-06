from django.test import TestCase

from django.test import TestCase
from app.models import Owner, Album, Photo

from faker import Factory


class ModelCase(TestCase):
    def setUp(self):
        fake = Factory.create()

        ow1, owc1 = Owner.objects.get_or_create(
            name=fake.name(),
            screen_name='foo_user',
        )
        ow2, owc2 = Owner.objects.get_or_create(
            name=fake.name(),
            screen_name='bar_user',
        )
        a1, ac1 = Album.objects.get_or_create(
            topic_name='#carnival',
        )
        a2, ac2 = Album.objects.get_or_create(
            topic_name='#other',
        )

        # insert 8 Proto objects

        Photo.objects.get_or_create(
            media_url='http://1.com',
            favorite_count=2,
            album=a1,
            owner=ow1
        )

        Photo.objects.get_or_create(
            media_url='http://2.com',
            album=a1,
            owner=ow2
        )

        Photo.objects.get_or_create(
            media_url='http://3.com',
            favorite_count=7,
            album=a1,
            owner=ow2
        )

        Photo.objects.get_or_create(
            media_url='http://4.com',
            favorite_count=2,
            album=a1,
            owner=ow2
        )

        Photo.objects.get_or_create(
            media_url='http://5.com',
            favorite_count=70,
            album=a1,
            owner=ow1
        )

        Photo.objects.get_or_create(
            media_url='http://6.com',
            favorite_count=1,
            album=a1,
            owner=ow1
        )

        Photo.objects.get_or_create(
            media_url='http://7.com',
            favorite_count=1,
            album=a1,
            owner=ow2
        )

        Photo.objects.get_or_create(
            media_url='http://8.com',
            favorite_count=10,
            album=a1,
            owner=ow1
        )

        Photo.objects.get_or_create(
            media_url='http://other_album.com',
            favorite_count=1,
            album=a2,
            owner=ow1
        )

    def test_high_rate(self):
        """First 3 photos most popular in #carnival Album"""
        album = Album.objects.get(
            topic_name='#carnival',
        )

        photos = Photo.objects.filter(album=album).order_by('-favorite_count')[:3]

        # for testing purpose we use subscripting to access the QuerySet, without iterate it
        self.assertEqual(photos[0].media_url, 'http://5.com')
        self.assertEqual(photos[1].media_url, 'http://8.com')
        self.assertEqual(photos[2].media_url, 'http://3.com')

    def test_child_count(self):
        """Photo's number for #carnival album"""
        album = Album.objects.get(
            topic_name='#carnival',
        )

        total = Photo.objects.filter(album=album).count()

        self.assertEqual(total, 8)