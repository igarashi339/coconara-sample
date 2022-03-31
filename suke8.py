import tweepy
import os
import time
from dotenv import load_dotenv

FETCH_TWEET_NUM = 100  # 1回の実行で取得するツイートの数
LIKE_TWEET_NUM = 3  # 1回の実行でLIKEするツイートの数
LIKE_TIMESPAN = 10  # いいねする感覚。[秒]

load_dotenv()
api_key = os.getenv("TWITTER_API_KEY")
api_secret = os.getenv("TWITTER_API_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
bearer_token = os.getenv("BEARER_TOKEN")


def get_client():
    return tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)


def fetch_tweets(client):
    """ツイートを取得する。
    """
    tweet_list = []
    try:
        query = "在籍ほしい OR 在籍欲しい OR 出稼ぎ行きたい OR お茶引いた OR 体入行きたい OR 在籍探す"
        tweet_list = client.search_recent_tweets(query, max_results=FETCH_TWEET_NUM).data
    except Exception as e:
        print(e)
    return tweet_list


def exec_like(client, tweet_list):
    """いいねを実行する。
    """
    liked_count = 0
    for tweet in tweet_list:
        if liked_count >= LIKE_TWEET_NUM:
            break
        liked_count += 1
        id = tweet["id"]
        client.like(tweet_id=id)
        print(f"like tweet: {id}")
        time.sleep(LIKE_TIMESPAN)


def main():
    client = get_client()
    tweet_list = fetch_tweets(client)
    exec_like(client, tweet_list)


if __name__ == "__main__":
    main()
