import json
import urllib

import pymongo
from django.conf import settings


class WeatherManager(object):
    def __init__(self):
        client = pymongo.MongoClient(settings.MONGO_URI)
        db = client['weather']
        self.coll = db['coll']

    def get_weather(self, lat, lang):
        if self.coll.find({"latitude": lat, "longitude": lang}).count() == 0:
            with urllib.request.urlopen("https://api.darksky.net/forecast/caf0208379875df865f2185f5246bf48/"+str(lat)+","+str(lang)+"?units=auto") as url:
                resp = url.read()
            resp_jsonified = json.loads(resp)
            weather = resp_jsonified.get('currently')
            self.coll.save(resp_jsonified)
        else:
            weather = self.coll.find_one({"latitude": lat, "longitude": lang})['currently']
        return weather
