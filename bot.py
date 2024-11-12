import tweepy
import random
import time

# Twitter API keys (replace with your actual keys)
API_KEY = "4VqwHcsMFfURfPGzYyGdPmCmD"
API_SECRET_KEY = "18tre0LwCiNksaPgmeGMtOmZcKodsCI5EfboMtUk0CijNGUSaX"
ACCESS_TOKEN = "AAAAAAAAAAAAAAAAAAAAAKm2wwEAAAAAbrkU8fWaNy2OHYbOpeJX0umQK38%3DsaZa1lNA4rfu2kKqM8zvTBXmPyvftrowrQwjZ38v6rX1lWwtAj"
ACCESS_TOKEN_SECRET = "foO5QmWT653vo1kZK4dw808ME49Y8sHATmzQakoybzTUg"

# Authenticate with Twitter API
def authenticate_twitter():
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    try:
        api.verify_credentials()
        print("Authentication successful")
    except tweepy.TweepError as e:
        print(f"Error during authentication: {e}")
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
def post_promotional_tweet(api):
    tweet = generate_promotional_tweet()
    try:
        api.update_status(tweet)
        print(f"Tweet posted: {tweet}")
    except tweepy.TweepError as e:
        print(f"Error posting tweet: {e}")

# Main function
def main():
    api = authenticate_twitter()
    # Tweet every 6 hours
    while True:
        post_promotional_tweet(api)
        time.sleep(6 * 60 * 60)  # 6 hours in seconds

if __name__ == "__main__":
    main()