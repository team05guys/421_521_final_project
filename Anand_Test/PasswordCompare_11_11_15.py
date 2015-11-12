#! /usr/bin/python

import picamera
import time
from SimpleCV import Color, Image, np
import os
import glob 

quality = 400
minMatch = 0.3
minDist = 0.25
with picamera.PiCamera() as camera:
	while True:
		camera.start_preview()
		time.sleep(2)
		camera.capture('pifacepw.jpg')
		image = Image("pifacepw.jpg")
		camera.stop_preview()
		#finds Haar features within the acquired image, using face.xml protocol 
		faces = image.findHaarFeatures("face.xml")
		if faces:
			
			#load the file names of each pre-exisiting password image into an array
			password_array = []
			os.chdir("/home/pi/Anand_Test/Saved_Passwords")
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
					print("Welcome back " + str(e[9:(len(e)-4)]))
					break
			
			if not keypoints:
				print("I DO NOT RECOGNIZE")
		
			break


			
