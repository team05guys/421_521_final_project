#! /usr/bin/python

import picamera
import time
from SimpleCV import Color, Image, np

quality = 400
minMatch = 0.3

#Set do you want to add a new face?
#If yes, do below code

with picamera.PiCamera() as camera:
   while True:
	print "Please align your face with the camera"
	time.sleep(1)
 	camera.start_preview()
	time.sleep(2)
	camera.capture('pipw.jpg')
	image = Image("pipw.jpg")
	camera.stop_preview()
	faces = image.findHaarFeatures("face.xml")
	faces.draw()
	face = faces[-1]
	print "Please Enter Your Name"
	name = raw_input()
	face.crop().save("Saved_Passwords/password_" + str(name) + ".jpg")
	print "Saving your Face and your name!"
	time.sleep(2)
	print "Ending the Program"
	break


	






#If no, then terminate
