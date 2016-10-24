__author__ = 'vipulvaibhaw'
import weatherparser
import BookReviewParser

class Messages:

    def __init__(self,user_name):
        self.user_name = user_name

    def WeatherMessage(self,city_name,country,temperature,clouds,source):
        z = weatherparser.Weather(city_name)
        k = z.AnalyseWeather()
        if z == "rain":
            return "@"+self.user_name+" Temp in "+city_name+" of country "+country+"-"+str(temperature)+" C. Carry an Umbrella. Source: " +source
        else:
            return "@"+self.user_name+" Temp in #"+city_name+" of country "+country+"-"+str(temperature)+ "C. "+clouds+ ". Source: " +source

    def ThankYouMessage(self):
        return "@"+self.user_name+ " I hope you liked me. You are Welcome!"

    def TimelyGreeterMesage(self,timeword):#Ignoring this function, don't want to greet people by good morning or good noon!
        return "Good " + timeword + " People!"

    def RandomQuoteTweeterMessage(self,quote,name):
        return str(quote) + " - #" + name+ ". #RandomQuote."

    def BookRaterMessage(self,book_title_clean,book_title):
        book = BookReviewParser.Book(book_title)
        rate = book.KnowRating()
        author = str(book.Author())
        if rate>=4:
            return "@"+self.user_name+" "+ book_title_clean+ " - Must Read! average rating on #goodreads- "+str(rate)+". #"+author
        if rate>=3 and rate<4:
            return "@"+self.user_name+" "+ book_title_clean+ " - Good Read! average rating on #goodreads- "+str(rate)+". #"+author
        if rate<3:
            return "@"+self.user_name+" "+ book_title_clean+ " - can't say! average rating on #goodreads- "+str(rate)+". #"+author
        else:
            return "@"+self.user_name+" "+ " sorry unable to fetch info."