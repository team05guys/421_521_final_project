#! /usr/bin/python

import picamera
import time
from SimpleCV import Color, Image, np
import os
import glob

#Set up grid overlay
import numpy as np
a = np.zeros((480, 800, 3), dtype = np.uint8)

x_offset = 50
y_offset = 200
 
a[x_offset, :, :] = 0xff
a[480 - x_offset, :, :] = 0xff
a[:, y_offset, :] = 0xff
a[:, 800 - y_offset, :] = 0xff

quality = 400
minMatch = 0.3
minDist = 0.25
with picamera.PiCamera() as camera:
	while True:
		camera.start_preview()
		#overlay grid 		
		o = camera.add_overlay(np.getbuffer(a), layer = 3, alpha = 64)
		time.sleep(3)	
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
			os.chdir("/home/pi/421_521_final_project/Anand_Test/Saved_Passwords")
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
				if keypoints:
					myName = str(e[9:(len(e)-4)])
					f = open("/home/pi/421_521_final_project/Anand_Test/Personal_Stuff/" + myName + ".txt", 'r')
					print(f.read())

					print("Welcome back " + myName)
					print("The Current Time is " + time.strftime("%I:%M:%S %p "))
					print("The Current Date is " + time.strftime("%m/%d/%Y"))
					break
			
			if not keypoints:
				print("I DO NOT RECOGNIZE")
		
			break


			
