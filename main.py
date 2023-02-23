#!pip install snscrape
#!pip install git+https://github.com/JustAnotherArchivist/snscrape.git
#!pip install pandas

import snscrape.modules.twitter as sntwitter
import pandas as pd
import snscrape.modules.twitter as sntwitter

username = 'BANKBRI_ID'
since = '2023-01-01'
until = '2023-01-31'

maxTweets = 1000
tweets_list2 = []
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'@{username} since:{since} until:{until}').get_items()):
  if i > maxTweets:
    break
  tweets_list2.append([tweet.date, tweet.url, tweet.id, tweet.username, tweet.rawContent, tweet.content, tweet.replyCount, tweet.retweetCount, tweet.likeCount, tweet.quoteCount, tweet.links])

tweets_df2 = pd.DataFrame(tweets_list2, columns=['Datetime', 'URL', 'Tweet Id', 'Username', 'Raw Text', 'Text', 'Reply Count', 'Retweet Count', 'Like Count', 'Quote Count', 'Links'])

tweets_df2.to_csv(f'tweet_{username}.csv', index=False)