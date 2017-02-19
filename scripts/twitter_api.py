    # # Tweet here.
    # auth = tweepy.OAuthHandler(config.CONSUMER_TOKEN, config.CONSUMER_SECRET)
    # auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
    # api = tweepy.API(auth)
    #
    # emergency_text = u'%s: %s' % (new_emer.participant.org_name, new_emer.detail)
    # emergency_text = smart_truncate_chars(emergency_text, 108)
    # tweet_text = u'%s #RGnews http://rgne.ws/closings-delays' % emergency_text
    # api.update_status(status = tweet_text)

import config
import pprint
import tweepy
auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

# print(api.me().name)
# user = api.get_user('jpheasly')
# print dir(user)
saved_search_obj = api.get_saved_search(833019869687738368)
# print saved_search_obj

# https://dev.twitter.com/rest/public/search
# http://docs.tweepy.org/en/v3.5.0/api.html#help-methods
search_results = api.search(
    q=u'stop "I voted" tweet OR tweeting to:realdonaldtrump OR to:potus',
    count=100,
)

# print dir(search_result)
# print search_result.index()

search_results = tweepy.Cursor(
    api.search,q=u'stop "I voted" tweet OR tweeting to:realdonaldtrump OR to:potus',
).items(100)

for search_result in search_results:
    '''
    'author',
    'contributors',
    'coordinates',
    'created_at',
    'destroy',
    'entities',
    'favorite',
    'favorite_count',
    'favorited',
    'geo',
    'id',
    'id_str',
    'in_reply_to_screen_name',
    'in_reply_to_status_id',
    'in_reply_to_status_id_str',
    'in_reply_to_user_id',
    'in_reply_to_user_id_str',
    'is_quote_status',
    'lang',
    'metadata',
    'parse',
    'parse_list',
    'place',
    'retweet',
    'retweet_count',
    'retweeted',
    'retweets',
    'source',
    'source_url',
    'text',
    'truncated',
    'user'
    '''

    pprint.pprint(search_result.text)
    pprint.pprint(search_result.created_at)
