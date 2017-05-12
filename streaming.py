from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="brqoDeFg6zJDv50HbVPlEZ2tI"
consumer_secret="Fx6D7jK2Q2X4RS39yMxQD3E08I8EcWRK2hk5njox9xRZPI4nxz"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="282304285-fyw4JKgyw2zCYM4PC2a8vNVdydytfJov3WgJrPhI"
access_token_secret="wDiPPXmRtcF41JPQQW9bAj8ENVL8m1Hl1V3aUxWQi07FF"

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(languages=["en"], track=['ahok', 'Basuki Tjahaja Purnama', 'Basuki', 'Basuki Tjahaja'])
