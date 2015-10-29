# 421_521_final_project
**Team05-Guys&Pis**

_Dan Sazer & Anand Ganapathy_

Rice Bioe 421/521 Final Project

#Brainstorm

##Facial Recognition Software to Unlock a Door


We are proposing to build a security system that recognizes individual faces and mechanically unlocks a door. The system would incorporate a Raspberry Pi microcontroller, an Arduino microcontroller, a camera, and a servo motor. The Raspberry Pi would process images from the camera, compare the images to a database of known users with access to the door, and then send a digital signal to the servo motor, via Arduino, if the given user has clearance. 
This project will necessitate the use of several external resources, including servo motors, customized housing and actuation components, and open-source facial recognition software.

#Abstract

##A Customizable Facial Recognition System to Perform Modularized Tasks


As technology advances, it is becoming increasingly feasible for laymen and hobbyists to develop biometric security systems for household use. Facial recognition is one of the simplest biometrics that can be achieved with minimal user-input, however facial recognition devices are often expensive and tailored to perform specific tasks with limited modular usage. We plan to develop a highly modular system based around facial recognition technology that allows user customization to perform specific tasks. 
The proposed facial recognition system will incorporate a Raspberry Pi microcontroller, an Arduino microcontroller, and a camera. The Raspberry Pi will process the images obtained from the camera, compare these images to a database of known users with access, and then perform a certain function based on the level of access. This system will then be connected to additional components such as servo motors, solenoid valves, or other actuators to allow performance of specific user required tasks. The initial task we propose is the use of this system to mechanically unlock a door through the use of a connected servo. In this use-case, once the system recognizes the individual as a known user with access, the system would send a digital signal to the servo motor to unlock the door.
After completion of this use case, other implementations of this system will then be developed to expand the functions of this system. Other proposed tasks include opening an unlocked door, switching on lights, or outputting user information.


#Updated Thoughts - 10/29/15
##Modifcations to the Inputs and Outputs of the Facial Recognition without Modifying the Facial Recognition Software
Concept discussion with Jordan and Jacob, we will move away from security aspect of facial recognition and towards personalization aspect. In effect, the system will recognize the user's face and then provide outputs based on that user's preferences. These outputs could include a touchscreen or any hardware (neostix - shows colors, speakers, lights, sounds, smells). For example, after detecting Anand's face, it will turn on a blue light and play a certain song that I like. 

Progress: We were able to get facial identification working using the adafruit tutorial. We had to remove any mention of RPIO.GPIO as this is not a command supported in Raspberry Pi 2. We modified the box2.py file and trained the pi-rec software to Dan's face and were able to positively identify him. However, the system could not recognize anyone else's face (tried 2 people)
