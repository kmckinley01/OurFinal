import tweepy #library for accessing the Twitter API
import random
from datetime import datetime

tweetNum = random.randint(0, 21)

#Put your Twitter API keys here
consumer_key = "EMb5s2N9YhLb6TUcKx7qmjyO9"
consumer_secret = "a4Z6y9ZSLOMNyvE6QoHLricW0RHsz7uDubnXTBMCd8ymCr7Jgh"
access_token = "1609208303338258432-uRyHxvN9oiEv6W06hSZAqfyIcowDnM"
access_token_secret = "aPhgQLAwCHzBPoqBueJdVUJg6hwC9VkBS6Xrzvi4TM0XH"
client = tweepy.Client(bearer_token=(access_token))

#Authenticate with the Twitter API using your API keys
auth = tweepy.OAuth1UserHandler(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

#Create a Tweepy API client
api = tweepy.API(auth)

# 200 tweets to be extracted
number_of_tweets = 2000
tweets = api.user_timeline(screen_name="SeffSaid")

# Empty Array
tmp = []

# create array of tweet information: username,
# tweet id, date/time, text
tweets_for_csv = [tweet.text for tweet in tweets]  # CSV file created
for j in tweets_for_csv:
    # Appending tweets to the empty array tmp
    tmp.append(j)

    # Printing the tweets
print(tmp)
print(tweets)
while (tmp[tweetNum].find("SeffSaid")>=0):
    tweetNum = random.randint(0, 21)

    # Create a Tweepy API client
api = tweepy.API(auth)
dt = datetime.now()
num = dt.weekday()
if num == 0:
    dayOfWeek = 'Monday'
elif num == 1:
    dayOfWeek = 'Tuesday'
elif num == 2:
    dayOfWeek = 'Wednesday'
elif num == 3:
    dayOfWeek = 'Thursday'
elif num == 4:
    dayOfWeek = 'Friday'
elif num == 5:
    dayOfWeek = 'Saturday'
elif num == 6:
    dayOfWeek = 'Sunday'

Happy = 'Happy ' + str(dayOfWeek) + '!'

api.update_status(Happy + "\n" + tmp[tweetNum] + "\n#DailyQuotes" + "\n#Inspiration")
