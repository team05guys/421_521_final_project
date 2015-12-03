#! /usr/bin/python
# encoding: utf-8

#Defines the below code as a function called lookup_weather that takes in the input variable (name), which corresponds to the identified user
def lookup_weather(name):
	#Imports the relevant modules
	import pywapi
	import pprint
	
	#Opens the folder ZCode and imports the text file containing the user specified zipcode
	myzip_file = open ("/home/pi/421_521_final_project/Code/Personal_Stuff/ZCode/" + name + "_myzip" + ".txt", 'r')		
	myzip = myzip_file.read()
	
	#Opens the US.txt file, which contains a list of the US zip codes with corresponding city, state identifers
	fname = "/home/pi/421_521_final_project/Code/US/US.txt"
	with open(fname) as fin:
		data_str = fin.read()
	
	#Create a list of lists
	data_list = []
	for line in data_str.split('\n'):
		mylist = line.split('\t')
		if len(mylist) > 11:
			data_list.append(mylist)
	
	#Searches the lists to find the city and state location corresponding to the input zip code
	for sublist in data_list:
		zip_code = sublist[1]
		if zip_code == myzip:
			location = "{}, {} {}".format(sublist[2], sublist[3], myzip)
		 
	#From the pywapi python module pulls the weather information for the input zip code and converts the units to imperial (fahrenheit)
	weather_com_result = pywapi.get_weather_from_weather_com(myzip, units = 'imperial')
	
	#Prints the current weather and the three day forecast as well the current city, state
	print ("Current weather: " +  weather_com_result['current_conditions']['text'].lower() + " and " + weather_com_result['current_conditions']['temperature'] + " F in " + location + " with a " + weather_com_result['forecasts'][0]['day']['chance_precip'] + "% chance of precipitation.")
	print ("Tomorrow's forecast: (" + weather_com_result['forecasts'][1]['date'] + ") is a high/low of " + weather_com_result['forecasts'][1]['high'] + '/' + weather_com_result['forecasts'][1]['low'] + " F with a " + weather_com_result['forecasts'][1]['day']['chance_precip'] + "% chance of precipitation.") 
	print ("2 days from now: (" + weather_com_result['forecasts'][2]['date'] + ") is a high/low of " + weather_com_result['forecasts'][2]['high'] + '/' + weather_com_result['forecasts'][2]['low'] + " F with a " + weather_com_result['forecasts'][2]['day']['chance_precip'] + "% chance of precipitation.")
	print ("3 days from now: (" + weather_com_result['forecasts'][3]['date'] + ") is a high/low of " + weather_com_result['forecasts'][3]['high'] + '/' + weather_com_result['forecasts'][3]['low'] + " F with a " + weather_com_result['forecasts'][3]['day']['chance_precip'] + "% chance of precipitation." )


