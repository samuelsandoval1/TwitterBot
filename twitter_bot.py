import tweepy
import time
CONSUMER_KEY = "A3jFSFfESjiMqz7oe0Rf0pjeK"
CONSUMER_SECRET = "mZFkHizPDgVBo09wCoow4YvAE8Sl6tRYnlTxGvZC9ZGtpRP4Cz"

ACCESS_KEY = "1606351970-BLKU2VISjrqDXQqs2oLWfIDay7GrxliJuGcesgG"
ACCESS_SECRET = "P03UwQJ4bsQvAIMXwRj4ZlJbXU3TyJHoFIRvL54dE2Ddp"


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()
search = '#CSUF'
numTweet = 500

for tweet in tweepy.Cursor(api.search, search).items(numTweet):
    try:
        print('Tweet Liked')
        tweet.favorite()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break 