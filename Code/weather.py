#! /usr/bin/python
# encoding: utf-8

def lookup_weather(name):
	import pywapi
	import pprint
	
	myzip_file = open ("/home/pi/421_521_final_project/Anand_Test/Personal_Stuff/ZCode/" + name + "_myzip" + ".txt", 'r')		
	myzip = myzip_file.read()
	#this will give you a dictionary of all cities in the world with this city's name - be specific
	#myzip = str(input("Please enter your zipcode "))
	
	fname = "/home/pi/421_521_final_project/Anand_Test/US/US.txt"
	with open(fname) as fin:
		data_str = fin.read()
	
	#create a list of lists
	data_list = []
	for line in data_str.split('\n'):
		mylist = line.split('\t')
		if len(mylist) > 11:
			data_list.append(mylist)
	
	for sublist in data_list:
		zip_code = sublist[1]
		if zip_code == myzip:
			location = "{}, {} {}".format(sublist[2], sublist[3], myzip)
		 
	#location_id now contains the city's code
	weather_com_result = pywapi.get_weather_from_weather_com(myzip, units = 'imperial')
	
	#Prints the current weather and the three day forecast
	print ("Current weather: " +  weather_com_result['current_conditions']['text'].lower() + " and " + weather_com_result['current_conditions']['temperature'] + " F in " + location + " with a " + weather_com_result['forecasts'][0]['day']['chance_precip'] + "% chance of precipitation.")
	print ("Tomorrow's forecast: (" + weather_com_result['forecasts'][1]['date'] + ") is a high/low of " + weather_com_result['forecasts'][1]['high'] + '/' + weather_com_result['forecasts'][1]['low'] + " F with a " + weather_com_result['forecasts'][1]['day']['chance_precip'] + "% chance of precipitation.") 
	print ("2 days from now: (" + weather_com_result['forecasts'][2]['date'] + ") is a high/low of " + weather_com_result['forecasts'][2]['high'] + '/' + weather_com_result['forecasts'][2]['low'] + " F with a " + weather_com_result['forecasts'][2]['day']['chance_precip'] + "% chance of precipitation.")
	print ("3 days from now: (" + weather_com_result['forecasts'][3]['date'] + ") is a high/low of " + weather_com_result['forecasts'][3]['high'] + '/' + weather_com_result['forecasts'][3]['low'] + " F with a " + weather_com_result['forecasts'][3]['day']['chance_precip'] + "% chance of precipitation." )


