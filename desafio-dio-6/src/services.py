import tweepy
from src.secrets import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
from src.constants import BRAZIL_WOE_ID
from src.connection import trends_collection


def _get_trends(woe_id: int, api: tweepy.API):
    """Get Trending Topic
    Args:
        :param woe_id:
    :return: List[Dict[str, Any]]: [description] Trends List
    """
    trends = api.trends_place(woe_id)

    return trends[0]['trends']


def get_trends_from_mongo():
    trends = trends_collection.find({})
    return list(trends)


def save_trends():
    auth = tweepy.Client(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    trends = _get_trends(BRAZIL_WOE_ID, api=api)
    trends_collection.insert_many(trends)
