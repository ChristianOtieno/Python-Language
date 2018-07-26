import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

class TwitterClient(object):
    """
    Generate TwitterClass for sentiment analysis.
    """
    def __init__(self):
        """
        Generate constructor or initialization method.
        """
        # Keys and tokens from the Twitter Dev Console
        ConsumerKey = ACN59Vzni3WZMqtfDOfw1ojfK
        ConsumerSecret = DEjVRxzzncHVdu4YRZLCWmfBvZMDWu9VKZg7ESi88vsODTqk4X
        AccessToken = 2591453484-wYVZ2YR0PROIEA0PjeqD3h176AqykJGLiEfbiXz
        AccessTokenSecret = EqgHu6GPp9uraucaedR4uxyFPtOwivSJOm0Kx8fH79do8

        # attempt authentication
        try:
            #create OAuthHanandler object
            self.auth = OAuthHandler(ConsumerKey, ConsumerSecret)
            # set access token and secret
            self.auth.set_access_token(AccessToken, AccessTokenSecret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error:Authentication Failed")
    
    def CleanTweet(self, tweet):
        """
        Utility function to clean tweet text by removing links, special characters 
        using simple regex statements.
        """
        return''.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z\t])|(r\w+:r\/r\/r\S+)", " ", tweet).split())
    
    def GetTweetSentiment(self, tweet):
        """
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        """
        # Create TextBlob object of passed tweet text
        analysis = TextBlob(self.CleanTweet(tweet))
        # Set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'
    
    def GetTweets(self, query, count = 10):
        """
        Main function to fetch tweets and parse them.
        """
        # Empty list to store parsed tweets.
        tweets = []

        try:
            # Call twitter api to fetch tweets
            FetchedTweets = self.api.search(q = query, count = count)

            # Parsing tweets one by one
            for tweet in FetchedTweets:
                # Empty dictionary to store required params of a tweet
                ParsedTweet = {}

                # Saving text of tweet
                ParsedTweet['text'] = tweet.text
                # Saving sentiment of tweet
                ParsedTweet['sentiment'] = self.GetTweetSentiment(tweet.text)

                # Appending parsed tweet to tweets list
                if tweet.RetweetCount > 0:
                    # If tweet has retweets, ensure that it is appended only once
                    if ParsedTweet not in tweets:
                        tweets.append(ParsedTweet)
                else:
                    tweets.append(ParsedTweet)
            # return parsed tweets
            return tweets

        except tweepy.TweepError as e:
            # Print error (if any)
            print("Error:"+str(e))
    

    def main():
        # Create object of TwitterClient Class
        api = TwitterClient()
        # Calling function to get tweets 
        tweets = api.GetTweets(query = 'Christian Otieno', count = 200)

        # Picking positive tweets from tweets
        ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
        # Percentage of positive tweets
        print("Positive tweets percentage:{}%".format(100*len(ptweets)/len(tweets)))
        # Picking negative tweets from tweets
        ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
        # Percentage of negative tweets
        print("Negative tweets percentage:{}%".format(100*len(ntweets)/len(tweets)))
        #Percentage of neutral tweets
        print("Neutral tweets percentage:{}%"\
        .format(100*len(tweets - ntweets - ptweets)/len(tweets)))

        # Printing first 5 positive tweets
        print("\n\nPositive tweets:")
        for tweet in ptweets[:10]:
            print(tweet['text'])
        
        # Printing first 5 negative tweets
        print("\n\nnegative tweets:")
        for tweet in ntweets[:10]:
            print(tweet['text'])
        
    if __name__ == "__main__":
        # Calling main function
        main()