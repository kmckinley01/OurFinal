import tweepy #library for accessing the Twitter API

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

tweet = 'this is an automated test tweet'

api.update_status(tweet)