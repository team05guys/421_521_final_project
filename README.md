# 421_521_final_project
**Team05-Guys&Pis**

_Dan Sazer & Anand Ganapathy_

Rice Bioe 421/521 Final Project

#Summary (A Customizable, Facial Identification-based Personal Assistant Device)
The contents of this repository allow personalized text outputs to be displayed in response to user facial identification. Upon facial registration, the user is prompted to enter his or her name, a personalized greeting message, his or her current zip code (for weather forecasting), and favorite subreddit. Upon facial identification, the personalized data will be output. 

#Technical Requirements
###Hardware
- Raspberry Pi (other microcontroller compatible with Raspbian)
- A camera module (compatible with your microcontroller)
- LCD screen (compatible with your microcontroller)
- STDINPUT device (e.g. keyboard) (compatible with your microcontroller)

###Software
- Raspbian
- Python
- Python modules (download references listed at end of this README.md)
  * Picamera
  * SimpleCV
  * Numpy
  * Pywapi
  * Feedparser
  
###Walkthrough
1. Download this entire repository from GitHub 
2. Verify the microcontroller recognizes your camera, LCD screen, and STDINPUT device
3. Install relevant Python modules as outlined in the "Software" portion of this README.md
4. When ready to register a new user, position face in front of camera
5. Execture PasswordSet.py
6. Align face with grid
7. Input requested information
8. Wait, chill, do whatever, go to sleep and wakeup, wait 10 years, etc
9. When ready to identify a registered user, position face in front of camera
10. Execture PasswordCompare.py
11. Align face with grid
12. Marvel at your requested personal data



#Abstract

##A Customizable, Facial Identification-based Personal Assistant Device


As technology advances, it is becoming increasingly feasible for laymen and hobbyists to develop personalized biometric-based control systems for household use. Facial recognition is one of the simplest biometrics that can be achieved with minimal user-input, however facial recognition devices are often expensive and tailored to perform specific tasks with limited modular usage. We sought to develop a highly modular system based around facial recognition technology that allows user customization to perform specific tasks. The facial recognition system we built incorporates a Raspberry Pi microcontroller, a camera, and a touchscreen. The Raspberry Pi processes the images obtained from the camera, displays them on a touchscreen, compares these images to a database of known users, and then performs a certain function specific to that user. This system can then be connected to additional components such as lights, speakers, and other components to allow performance of specific user-defined tasks. The initial task we proposed and then developed is the use of this system to recognize and identify a person and then display certain user information such as name. In this use-case, once the system recognizes the individual as a known user, the system will display the user’s name. After completion of this use case, we expanded the system to include pertinent weather updates, an rss reddit feed, date/time as well as a personalized message.  Future feature expansion includes playing music from a user’s playlist, switching on lights, or outputting other user-specific information (e.g. calendar, agenda, or stock prices).




#Updated Thoughts - 10/29/15
##Modifcations to the Inputs and Outputs of the Facial Recognition without Modifying the Facial Recognition Software
Concept discussion with Jordan and Jacob, we will move away from security aspect of facial recognition and towards personalization aspect. In effect, the system will recognize the user's face and then provide outputs based on that user's preferences. These outputs could include a touchscreen or any hardware (neostix - shows colors, speakers, lights, sounds, smells). For example, after detecting Anand's face, it will turn on a blue light and play a certain song that I like. 

Progress: We were able to get facial identification working using the adafruit tutorial. We had to remove any mention of RPIO.GPIO as this is not a command supported in Raspberry Pi 2. We modified the box2.py file and trained the pi-rec software to Dan's face and were able to positively identify him. However, the system could not recognize anyone else's face (tried 2 people)

#References 
1. https://learn.adafruit.com/raspberry-pi-face-recognition-treasure-box/overview
2. https://thinkrpi.wordpress.com/2013/05/22/opencv-and-camera-board-csi
3. https://www.youtube.com/watch?v=vRHoQVZLvoM
4. http://www.open-electronics.org/raspberry-pi-and-the-camera-pi-module-face-recognition-tutorial
5. http://thecodeinn.blogspot.com/2013/07/tutorial-weather-forecast-in-python.html
6. https://code.google.com/p/python-weather-api
7. https://www.daniweb.com/programming/software-development/code/490561/postal-code-zips-and-location-python
8. http://www.pythonforbeginners.com/feedparser/using-feedparser-in-python

*Revised 12/2/15*
