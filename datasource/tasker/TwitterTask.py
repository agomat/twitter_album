from ConfMixin import ConfMixin
from DataAccess import DataAccess
import twitter
import urllib
from pprint import pprint


class TwitterTask(ConfMixin):

    api = None
    tweet_list = []

    def __init__(self):
        super(TwitterTask, self).__init__()
        self.connect()
        self.search()
        self.process_list()

    # DataAccess methods

    def get_min_id_or_none(self):
        return DataAccess.get_min_id_or_none(self.topic)

    def save_photo(self, tw_id, owner_name, owner_screen_name, media_url, favorite_count):
        DataAccess.save_photo(self.topic, tw_id, owner_name, owner_screen_name, media_url, favorite_count)

    # Template (pattern) procedural methods

    def connect(self):
        self.api = twitter.Api(consumer_key=self.consumer_key,
                           consumer_secret=self.consumer_secret,
                           access_token_key=self.access_token_key,
                           access_token_secret=self.access_token_secret)

    def search(self):

        # STEP 1 - building raw_query
        raw_query = {
                        'q': self.topic,
                        'count': 10,
                        'filter': 'twimg',
                        'exclude': 'retweets',
                        'include_entities': 'true'
                    }

        # Please find my local min_id if I have one
        min_id = self.get_min_id_or_none()

        # If id the first time for this album or I have no id, I prefer to have an (most) recent id
        if not min_id:
            raw_query['result_type'] = 'recent'
            raw_query['count'] = 1
        else:
            raw_query['result_type'] = 'mixed'
            raw_query['count'] = 30
            raw_query['max_id'] = min_id    # you can also use since_id option to fetch freshes photos:
                                            # change the aggregate funcion in DataAccess from Min to Max
                                            # For exercise purpose I choose to use max_id in order to
                                            # populate my album as quick as possibile

        # STEP 2 - search for tweets
        self.tweet_list = self.api.GetSearch(
            raw_query=urllib.urlencode(raw_query),
        )

    def process_list(self):
        # STEP 3 - save data into model using DataAccess
        for tweet in self.tweet_list:
            tweet = tweet.AsDict()

            print "*****************"
            pprint(tweet.get('id'))

            # a) Grabbing favs count

            favorite_count = tweet.get('favorite_count')  # Returns Int or None

            # b) Grabbing media url

            media_url = None
            try:
                media_url = tweet['media'][0]['media_url']
            except KeyError:
                print "No media url found"
                print tweet
                pass

            # c) Grabbing Long Name

            owner_name = None
            try:
                owner_name = tweet['user']['name']
            except KeyError:
                print "No full name found"
                pass

            # d) Grabbing UserName

            owner_screen_name = None
            try:
                owner_screen_name = tweet['user']['screen_name']
            except KeyError:
                print "No username found"
                pass

            if owner_name and owner_screen_name and media_url:
                self.save_photo( tweet.get('id'), owner_name, owner_screen_name, media_url, favorite_count )



