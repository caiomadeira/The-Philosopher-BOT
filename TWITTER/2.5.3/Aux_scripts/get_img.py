from Credentials.credentials_verify_test import api_test
import requests

timeline = api_test.user_timeline(count=10, screen_name = "sudomadeira")
for tweet in timeline:
   for media in tweet.entities.get("media",[{}]):
      print(media)
      #checks if there is any media-entity
      if media.get("type",None) == "photo":
          # checks if the entity is of the type "photo"
          image_content=requests.get(media["media_url"])
          print(image_content)
          img.save()