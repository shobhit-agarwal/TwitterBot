__author__ = 'vipulvaibhaw'

def messageCorrect(user_name,city_name,country,temperature,source):
    return "@"+user_name+ " Temp in "+city_name+" of country "+country+"-" + str(temperature)+" C." +source+ " #WeatherKnow #WeatherBot #India"

def messageIncorrect(user_name):
    return "@"+user_name+ " Sorry! I am new to your language human. Didn't understand your tweet. :/ #WeatherBot #IndianBot."

def twoWordname(user_name):
    return "@"+user_name+ " Please tweet one word.just one whitespace. If city is of two words. concatenate! :) #WeatherBot."
