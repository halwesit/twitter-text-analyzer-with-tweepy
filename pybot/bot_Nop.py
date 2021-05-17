import tweepy
import csv

#  Api key for twitter auth.
API_KEY = ""
API_SECRET_KEY = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

# creating object for Tweepy lib.
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Reading IDs from CSV file
with open('./data/isarcasm_test.csv', 'r') as tweetData:
    tweets = csv.DictReader(tweetData)

    # preparing writing results on a CSV file
    with open('./data/collectedTestTweets.csv', 'w', newline='', encoding="ISO-8859-1") as file:
        writer = csv.writer(file)
        writer.writerow(["Tweet_text"])
        

        # some varabile init
        count = 0
        theTweetIDList = []
        theTweetTextList = []
        i = 0

        # looping each tweet id
        for tweet in tweets:
            count = count + 1
            # convert string id to int
            theTweetIDList.append(int(tweet['tweet_id']))

            # grouping for 100 ids each time
            if count == 100:
                # calling twitter for getting results for 100 given ids
                twt = api.statuses_lookup(theTweetIDList)
                theTweetTextList.insert(i, twt)
                count = 0
                theTweetIDList.clear()
                i = i + 1
                print(i)

        # looping result list by response objectes
        for ii in range(i):
            for j in range(100):
                # checking if index existe
                if theTweetTextList[ii][j-1]:
                    print(theTweetTextList[ii][j-1].text)
                    # getting text of tweets from each object and write on the CSV file
                    writer.writerow([str(theTweetTextList[ii][j-1].text).encode("utf-8")])
        
