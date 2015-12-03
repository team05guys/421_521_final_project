#! /usr/bin/python

#import relevant modules
import picamera
import time
from SimpleCV import Color, Image, np
import os
import glob
import rss_reddit
from weather import *


#Set up grid overlay
#initialize numpy array with dimensions that match the camera's resolution
import numpy as np
a = np.zeros((480, 800, 3), dtype = np.uint8)

#initialize offset from edges, for grid lines
x_offset = 50
y_offset = 200
 
#create a number of solid white lines equal to the $thickness, within the numpy array
a[x_offset, :, :] = 0xff
a[480 - x_offset, :, :] = 0xff
a[:, y_offset, :] = 0xff
a[:, 800 - y_offset, :] = 0xff


#Set camera settings
quality = 400
minMatch = 0.3
minDist = 0.25

with picamera.PiCamera() as camera:
#Infinite loop of image acquistion that breaks when a face is recognized
	while True:
		camera.start_preview()
		#overlay grid 		
		o = camera.add_overlay(np.getbuffer(a), layer = 3, alpha = 64)
		time.sleep(10)	
		camera.capture('pifacepw.jpg')
		#remove grid
		camera.remove_overlay(o)

		image = Image("pifacepw.jpg")
		camera.stop_preview()
		#finds Haar features within the acquired image, using face.xml protocol 
		faces = image.findHaarFeatures("face.xml")
		if faces:
			
			#load the file names of each pre-exisiting password image into an array
			password_array = []
			os.chdir("/home/pi/421_521_final_project/Code/Saved_Passwords")
			for file in glob.glob("password_*"):
				password_array.append(file)

			#img processing
			faces.draw()
			face = faces[-1]
			template = face.crop()
			template.save("passwordmatch.jpg")
			
			#check acquired image against each saved password image 
			for e in password_array:
				password = Image(e)
				keypoints = password.findKeypointMatch(template,quality,minDist,minMatch)
				#keypoints is the function that performs the comparison of the current face image against the known user database
				if keypoints:
					#print your name
					myName = str(e[9:(len(e)-4)])
					print("---------------------------------------------------------\n")
					print("Welcome back, " + myName + "!" + "\n")

					#print greeting file
                                        greeting_file = open("/home/pi/421_521_final_project/Code/Personal_Stuff/greeting/" + myName + "_greeting.txt", 'r')
	                                print(greeting_file.read())
					print
					print("---------------------------------------------------------\n")

					#Print current time and date
					print("The Current Time is " + time.strftime("%I:%M:%S %p %Z "))
					print("Today is " + time.strftime("%A, %b. %d, %Y") + "\n")

					#Print Weather for Current City
					lookup_weather(myName)
					print
					print("---------------------------------------------------------\n")
					
					#open file containing name of favorite city
					city_file = open ("/home/pi/421_521_final_project/Code/Personal_Stuff/city/" + myName + "_city.txt", 'r')
					city_file_contents = city_file.read()

					#print top 10 reddit posts from favorite city subreddit 
					print("Displaying top 10 reddit posts from the " + city_file_contents + " subreddit: \n")
					rss_reddit.subreddit(city_file_contents)


					break
			
			if not keypoints:
				#If the current face image is not recognized against the known user database, the line below is printed and the program terminates
				print("I DO NOT RECOGNIZE")
		
			break


			
