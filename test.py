import snscrape.modules.twitter as sntwitter

tweets_list = []

for i, tweet in enumerate(sntwitter.TwitterTweetScraper(tweetId=1629095687953715202, mode=sntwitter.TwitterTweetScraperMode.SCROLL).get_items()):
    tweets_list.append([tweet.date, tweet.url, tweet.id, tweet.username, tweet.rawContent, tweet.content,
                        tweet.replyCount, tweet.retweetCount, tweet.likeCount, tweet.quoteCount, tweet.links, tweet.inReplyToTweetId, True])
    
print(tweets_list)
