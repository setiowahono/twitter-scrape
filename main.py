#!pip install snscrape
#!pip install git+https://github.com/JustAnotherArchivist/snscrape.git
#!pip install pandas

import snscrape.modules.twitter as sntwitter
import pandas as pd
import snscrape.modules.twitter as sntwitter

username = '@BANKBRI_ID'
since = '2023-01-01'
until = '2023-02-28'

maxTweets = 1000
tweets_list = []
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'{username} since:{since} until:{until}').get_items()):
    if (tweet.replyCount > 0 and tweet.inReplyToTweetId != None):
        tweets_list.append([tweet.date, tweet.url, tweet.id, tweet.username, tweet.rawContent, tweet.content,
                            tweet.replyCount, tweet.retweetCount, tweet.likeCount, tweet.quoteCount, tweet.links, tweet.inReplyToTweetId, False])
        
        for y, parentTweet in enumerate(sntwitter.TwitterTweetScraper(tweet.inReplyToTweetId).get_items()):
            tweets_list.append([parentTweet.date, parentTweet.url, parentTweet.id, parentTweet.username, parentTweet.rawContent, parentTweet.content,
                                parentTweet.replyCount, parentTweet.retweetCount, parentTweet.likeCount, parentTweet.quoteCount, parentTweet.links, tweet.inReplyToTweetId, True])
            
        if i > maxTweets:
            break

df = pd.DataFrame(tweets_list, columns=['Datetime', 'URL', 'Tweet Id', 'Username', 'Raw Text',
                  'Text', 'Reply Count', 'Retweet Count', 'Like Count', 'Quote Count', 'Links', 'Reply to ID', 'Is Parent'])

df.to_csv(f'tweet_{username}_2.csv', index=False)
