import twitter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
#Pratim Patel


twitter_consumer_key = 'dhRcqO7NaZf8wk3hTVCVAoOzA'
twitter_consumer_secret = 'ns8oQfE2Pg8cVFAd70jbei2E3hJzpgWIO3gHlVPtO4WwwvWlau'
twitter_access_token = '1009938991540469761-BX6um21ZjdyEHqMCDyqwvJido1kbCT'
twitter_access_secret = 'e8qjvjZhJTjm7mtV7VxZwB7ra6YF2f2X3OSdj1GsG87fY'

twitter_api = twitter.Api(consumer_key = twitter_consumer_key, consumer_secret = twitter_consumer_secret, access_token_key = twitter_access_token, access_token_secret = twitter_access_secret)

handle = input("Please enter the twitter username in the format @realDonaldTrump")

#use the twitter method in order to get the users timeline up to 1000 previous tweets, and disallow retweets.

statuses = twitter_api.GetUserTimeline(screen_name=handle, count=1000, include_rts=False, exclude_replies=True)

text = ""
"""loops through all of the statuses and concatenates only true text to the string, after changing the encoding of the text to utf-8"""
for status in statuses:
  if (status.lang == 'en'):
      text+= str(status.text.encode('utf-8'))
"""Removes urls and tags from the string text"""
removeurl = " ".join([word for word in text.split()
                            if 'http' not in word
                                and not word.startswith('@')
                                and word != 'RT'
                            ])




#utilizing the wordcloud API in order to generate a wordcloud with the text that we gained from the twitter user
wordcloud = WordCloud(width = 800, height = 800, background_color = 'black', min_font_size = 10).generate(removeurl)

plt.figure(figsize = (8, 8), facecolor = None)

plt.imshow(wordcloud)

plt.axis("off")

plt.tight_layout(pad = 0)
 
plt.show()




