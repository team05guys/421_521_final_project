#!/usr/bin/python 

import picamera
import time
from SimpleCV import Color, Image, np 

quality = 400
minMatch = 0.3

try:
    password = Image("password.jpg")
except:
    password = None

mode = "unsaved"
saved = False
minDist = 0.25

with picamera.PiCamera() as camera:
   while True:
	camera.start_preview()
	time.sleep(5)
	camera.capture('pifacepw.jpg')
	image = Image("pifacepw.jpg")
	camera.stop_preview()
	faces = image.findHaarFeatures("face.xml")
	if faces:
		if not password:
			faces.draw()
			face = faces[-1]
			password = face.crop().save("password.jpg")
			print "Saving Face, RUN!"
			print "Terminating the Program"
		else:
			faces.draw()
			face = faces[-1]
			template = face.crop()
			template.save("passwordmatch.jpg")
			keypoints = password.findKeypointMatch(template,quality,minDist,minMatch)
			if keypoints:
				print "Welcome back - Your Face Matches!"
				prompt = raw_input("Would you like to use the last picture as a password? Y/N")
 				if prompt == "Y":
				  image = cam.getImage().scale(320, 240)
 				  faces = image.findHaarFeatures("face.xml")
				  tryit = 1
				  while not tryit == 10 or not faces:
				    image = cam.getImage().scale(320,240)
				    faces = image.findHaarFeatures("face.xml")
				    tryit += 1
 				  if not faces:
				    print "I found no face"
				    break
				  else:
				    faces.draw()
  				    face = faces[-1]
				    password = face.crop().save("password.jpg")
				    face.crop().show()
				    print "Saving Run"
				    print "Closing the Program"
				    time.sleep(1)
				    break
				else:
				  print "OK..."
				  break
			else:
				print "I do not Recognize"
				print "Activating alarm"
				break
	else:
		break
