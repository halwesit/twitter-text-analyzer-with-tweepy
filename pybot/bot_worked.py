import tweepy
import csv

#Twitter API 
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""


def get_all_tweets(screen_name):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    alltweets = []  
    
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)
    
    alltweets.extend(new_tweets)
    
    oldest = alltweets[-1].id - 1
    
    while len(new_tweets) > 0:
        print(f"getting tweets before {oldest}")
        
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
    
        alltweets.extend(new_tweets)
        
        oldest = alltweets[-1].id - 1
        
        print(f"...{len(alltweets)} tweets downloaded")

    outtweets = [[tweet.id_str, tweet.created_at, tweet.text] for tweet in alltweets]
    
    #write the csv  
    with open('new_{screen_name}_tweet.csv', 'w', encoding="utf8") as file:
        writer = csv.writer(file)
        writer.writerow(["id","created_at","text"])
        writer.writerows(outtweets)

        # writer.writerows([str(outtweets).encode("utf-8")])
        #s.encode('utf-8').decode('latin-1')

        # writer.writerow([str(theTweetTextList[ii][j-1].text).encode("utf-8")])

    # with open('./data/collectedTestTweets.csv', 'w', newline='', encoding="ISO-8859-1") as file:
    #     writer = csv.writer(file)
    #     writer.writerow(["Tweet_text"])

    
    pass


if __name__ == '__main__':
	get_all_tweets("J_tsar")