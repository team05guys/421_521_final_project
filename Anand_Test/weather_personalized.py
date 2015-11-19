
#! /usr/bin/python
# encoding: utf-8

def lookup_weather():
	import pywapi
	import pprint

	city_file = open ("/home/pi/421_521_final_project/Anand_Test/Personal_Stuff/city/Dan_city.txt", 'r')		
	city = city_file.read()
	#this will give you a dictionary of all cities in the world with this city's name - be specific
	print('Your city is '+ city)
	
	lookup = pywapi.get_location_ids(city)
	
	#workaround to access last item of dictionary
	for i in lookup:
	   location_id = i
	 
	#location_id now contains the city's code
	weather_com_result = pywapi.get_weather_from_weather_com(location_id)
	
	print ("The current weather is " +  weather_com_result['current_conditions']['text'].lower() + " and  " + weather_com_result['current_conditions']['temperature'] + "C in " + city + ".")
