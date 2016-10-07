from ConfMixin import ConfMixin
from DataAccess import DataAccess
import twitter


class TwitterTask(ConfMixin):

    api = None
    ids_list = []
    tweet_list = []

    def __init__(self):
        super(TwitterTask, self).__init__()
        self.connect()
        self.search()

    # DataAccess methods

    def get_since_id_or_none(self):
        return DataAccess.get_since_id_or_none(self.topic)

    def save_since_id(self):
        try:
            value = self.ids_list[-1]
        except IndexError:
            value = None  # empty list!
        DataAccess.save_since_id(self.topic, value)

    # Template (pattern) procedural methods

    def connect(self):
        self.api = twitter.Api(consumer_key=self.consumer_key,
                           consumer_secret=self.consumer_secret,
                           access_token_key=self.access_token_key,
                           access_token_secret=self.access_token_secret)

    def search(self):

        # step 1 - search for tweets
        search = self.api.GetSearch(
            term=self.topic,
            count=10,
            since_id=self.get_since_id_or_none(),
            include_entities=True)

        # step 2 - extract ids
        self.ids_list = [x.id for x in search]
        print self.ids_list

        # step 3 - persist last id in the model
        self.save_since_id()

    def prepareList(self):
        pass


    pass