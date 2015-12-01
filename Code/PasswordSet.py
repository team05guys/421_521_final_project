#! /usr/bin/python

import picamera
import time
from SimpleCV import Color, Image, np
import numpy as np

#initialize numpy array with dimensions that match the camera's resolution
thickness = 15
a = np.zeros((480, 800, 3), dtype = np.uint8)

#initialize offset from edges, for grid lines
x_offset = 50
y_offset = 200

#create a number of solid white lines equal to the $thickness, within the numpy array
for i in range(thickness):
	a[x_offset + i, :, :] = 0xff
	a[480 - (x_offset + i), :, :] = 0xff
	a[:, y_offset + i, :] = 0xff
	a[:, 800 - (y_offset + i), :] = 0xff

quality = 400
minMatch = 0.3

#Set do you want to add a new face?
#If yes, do below code

with picamera.PiCamera() as camera:
   while True:
	#acquire image
	print "Please align your face with the camera"
	time.sleep(1)
 	camera.start_preview()
	#add overlay
	o = camera.add_overlay(np.getbuffer(a), layer = 3, alpha = 64)
	time.sleep(10)
	camera.capture('pipw.jpg')
	camera.remove_overlay(o)
	
	#process image
	image = Image("pipw.jpg")
	camera.stop_preview()
	faces = image.findHaarFeatures("face.xml")
	faces.draw()
	face = faces[-1]

	#link image to your name and personal greeting
	print "Please Enter Your Name"
	name = raw_input()
	print("Please enter a personalized greeting message:")
	greeting = raw_input()
	print("Please enter the exact name of your favorite subreddit: ")
	myCity = raw_input()
	print("Please enter the zip code of your current location:")
	myzip = raw_input()
	
	#save image as password_yourName.jpg
	face.crop().save("Saved_Passwords/password_" + str(name) + ".jpg")
	
	#save personal greeting
	greeting_file = open("Personal_Stuff/greeting/" + str(name) + "_greeting" +  ".txt", 'w')
	greeting_file.write(greeting)

	#save favorite city
	city_file = open("Personal_Stuff/city/" + str(name) + "_city" + ".txt", 'w')
	city_file.write(myCity)

	#save zip code of current location
	myzip_file = open("Personal_Stuff/ZCode/" + str(name) + "_myzip" + ".txt", 'w')
	myzip_file.write(myzip)
	
	print "Saving an image of your Face and your information!"
	time.sleep(2)
	print "Ending the Program"
	break


	






#If no, then terminate
