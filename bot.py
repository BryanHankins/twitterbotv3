import tweepy
import random
import os
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Twitter API keys (retrieved from environment variables)
API_KEY = os.getenv("API_KEY")
API_SECRET_KEY = os.getenv("API_SECRET_KEY")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

# Authenticate with Twitter API
def authenticate_twitter():
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    try:
        api.verify_credentials()
        logger.info("Authentication successful")
    except tweepy.TweepError as e:
        logger.error(f"Error during authentication: {e}")
    return api

# Generate promotional tweets
def generate_promotional_tweet():
    promotions = [
        "🌟 Elevate your style with The Celestial Code! Shop luxurious purses & handbags today! 👜✨ #LuxuryFashion #CelestialCode",
        "Handbags that make a statement! Discover your perfect match at The Celestial Code. 🌌👜 #StyleUpgrade",
        "Turn heads with premium handbags from The Celestial Code. Shop now for elegance redefined! 🛍️🌟 #CelestialStyle",
        "Chic. Elegant. Timeless. The Celestial Code handbags are here to transform your wardrobe. 🌠👜 Visit us today!",
        "Indulge in celestial luxury. Handbags crafted for stars like you. 🌟✨ Shop at The Celestial Code now! #LuxuryLifestyle"
    ]
    return random.choice(promotions)

# Post promotional tweets
def post_promotional_tweet():
    api = authenticate_twitter()
    tweet = generate_promotional_tweet()
    try:
        api.update_status(tweet)
        logger.info(f"Tweet posted: {tweet}")
    except tweepy.TweepError as e:
        logger.error(f"Error posting tweet: {e}")

# Entry point for Heroku Scheduler
if __name__ == "__main__":
    post_promotional_tweet()
