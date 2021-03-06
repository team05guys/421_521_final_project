
#! /usr/bin/python
# encoding: utf-8

import pywapi
import pprint

city = raw_input("Enter city name: ")
#this will give you a dictionary of all cities in the world with this city's name - be specific
print('Your city is '+ city)

lookup = pywapi.get_location_ids(city)

#workaround to access last item of dictionary
for i in lookup:
   location_id = i
 
#location_id now contains the city's code
weather_com_result = pywapi.get_weather_from_weather_com(location_id)

print ("The current weather is " +  weather_com_result['current_conditions']['text'].lower() + " and  " + weather_com_result['current_conditions']['temperature'] + "C in " + city + ".")
