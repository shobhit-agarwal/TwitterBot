__author__ = 'vipulvaibhaw'

import urllib2
from bs4 import BeautifulSoup

class Weather:
    def __init__(self,city):
        self.city = city
        self.url1 = "http://api.openweathermap.org/data/2.5/weather?q="
        self.url2 = "&appid=e79deb978550ee67b4e25ad9a7fe44ff&mode=xml"
        self.finalurl = self.url1+self.city+self.url2
        page = urllib2.urlopen(self.finalurl)
        soup = BeautifulSoup(page)
        self.weather_report = {"city_name":soup.city["name"],
        "country":str(soup.country.text),
        "humidity":soup.humidity["value"],
        "clouds":soup.clouds["name"],
        "wind":soup.wind.speed["name"],
        "temperature":float(soup.temperature["value"])-273.15,
        "weather":soup.weather["number"],
        "weather_value":soup.weather["value"],
        "lastupdate":soup.lastupdate["value"],
        "source":"source: OpenWeatherMap.",
        #"signoff":"If information is not correct, please spare your toddler bot! :/"
                }

    def Know(self):
        return self.weather_report

    def AnalyseWeather(self):
        #with reference to
        #http://openweathermap.org/weather-conditions
        drizzle_and_rain = [300,301,302,310,311,312,313,314,321,500,501,502,503,504,511,520,521,522,531]
        temperature = int(self.weather_report["weather"])
        if temperature in drizzle_and_rain:
            return "rain"
        else:
            return "clouds"

"""m = "@WeatherBot NewDelhi ".split(" ")
print m[1]
k= Weather("Nashik")
print k.Know()"""