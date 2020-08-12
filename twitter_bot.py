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
search = '#SwiftLang'
numTweet = 100


for tweet in tweepy.Cursor(api.search, search).items(numTweet):
    try:
        tweet.favorite()
        print('Tweet Liked')
    except tweepy.TweepError as e:
        if e.response.status_code == 420 or e.response.status_code == 429 :
            time.sleep(15 * 60)
            continue
        else:
            print("Break due to exception: ", tweepy.TweepError)
            break
        print(e.reason)

    except StopIteration:
        break
