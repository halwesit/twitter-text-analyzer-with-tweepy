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
with open('./inpute/isarcasm_train.csv', 'r') as tweetData:
    tweets = csv.DictReader(tweetData)
# with open('./inpute/isarcasm_test.csv', 'r') as tweetData:
#     tweets = csv.DictReader(tweetData)
    tweets = list(tweets)
    # preparing writing results on a CSV file
    with open('./results/collectedTrainTweets.csv', 'w', newline='') as file:
        writer = csv.writer(file)
    # with open('./results/collectedTestTweets.csv', 'w', newline='') as file:
    #     writer = csv.writer(file)
        writer.writerow(["tweet_id", "tweet_text"])

        # some varabile init
        count = 0
        theTweetIDList = []
        theTweetTextList = []
        tweet_id_list = []
        i = 0
        tweetLen = len(tweets)
        # looping each tweet id
        for tweet in tweets:
            count = count + 1
            # convert string id to int
            theTweetIDList.append(int(tweet['tweet_id']))
            tweet_id_list.append(int(tweet['tweet_id']))

            tweetLen = tweetLen - 1
            # grouping 100 ids each time
            if count == 100 or tweetLen == 0:
                # calling twitter for getting results for 100 given ids
                twt = api.statuses_lookup(theTweetIDList)
                theTweetTextList.insert(i, twt)
                theTweetIDList.clear()
                i = i + 1
                print("A request for " + str(i * count) + " tweet ids are sent")
                count = 0

        # looping result list by response objectes
        results_list = []
        id_list = []
        for ii in range(i):
            for j in range(len(theTweetTextList[ii])):
                results_list.append(theTweetTextList[ii][j])
                id_list.append(theTweetTextList[ii][j].id)

        count_available_tweets = 0
        for t in range(len(tweets)):
            if int(tweets[t]['tweet_id']) in id_list:
                print('The tweet_id:'+tweets[t]['tweet_id']+" available")
                writer.writerow(
                    [str(results_list[count_available_tweets].id), str(results_list[count_available_tweets].text).encode("utf-8")])
                count_available_tweets = count_available_tweets + 1
            else:
                print('The tweet_id:'+tweets[t]['tweet_id']+" NOT available")
                writer.writerow(
                    [str(tweets[t]['tweet_id']), ''])
