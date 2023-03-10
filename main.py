import snscrape.modules.twitter as sntwitter
import pandas as pd
import snscrape.modules.twitter as sntwitter

filter_string = '@BankBCA'
since = '2023-01-01'
until = '2023-01-31'

maxTweets = 100
tweets_list = []
j = 1

for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'{filter_string} since:{since} until:{until}').get_items()):
    if (tweet.replyCount > 0 and tweet.inReplyToTweetId == None):
        for x, tweet2 in enumerate(sntwitter.TwitterTweetScraper(tweetId=tweet.id, mode=sntwitter.TwitterTweetScraperMode.SCROLL).get_items()):
            try:
                tweets_list.append([
                    tweet2.url,
                    tweet2.date,
                    tweet2.rawContent,
                    tweet2.renderedContent,
                    tweet2.id,
                    tweet2.user,
                    tweet2.replyCount,
                    tweet2.retweetCount,
                    tweet2.likeCount,
                    tweet2.quoteCount,
                    tweet2.conversationId,
                    tweet2.lang,
                    tweet2.source,
                    tweet2.sourceUrl,
                    tweet2.sourceLabel,
                    tweet2.links,
                    tweet2.media,
                    tweet2.retweetedTweet,
                    tweet2.quotedTweet,
                    tweet2.inReplyToTweetId,
                    tweet2.inReplyToUser,
                    tweet2.mentionedUsers,
                    tweet2.coordinates,
                    tweet2.place,
                    tweet2.hashtags,
                    tweet2.cashtags,
                    tweet2.card,
                    tweet2.viewCount,
                    tweet2.vibe,
                ])
            except AttributeError:
                print('AttributeError', x)

        j = j + 1

    if j > maxTweets:
        break

df = pd.DataFrame(tweets_list, columns=[
    'url',
    'date',
    'rawContent',
    'renderedContent',
    'id',
    'user',
    'replyCount',
    'retweetCount',
    'likeCount',
    'quoteCount',
    'conversationId',
    'lang',
    'source',
    'sourceUrl',
    'sourceLabel',
    'links',
    'media',
    'retweetedTweet',
    'quotedTweet',
    'inReplyToTweetId',
    'inReplyToUser',
    'mentionedUsers',
    'coordinates',
    'place',
    'hashtags',
    'cashtags',
    'card',
    'viewCount',
    'vibe',
])

df.to_csv(f'tweet_{filter_string}_100.csv', index=False)
