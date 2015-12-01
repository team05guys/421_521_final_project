# 421_521_final_project
**Team05-Guys&Pis**

_Dan Sazer & Anand Ganapathy_

Rice Bioe 421/521 Final Project

#Abstract

##A Customizable Facial Recognition System to Perform Modularized Tasks


As technology advances, it is becoming increasingly feasible for laymen and hobbyists to develop personalized biometric based control systems for household use. Facial recognition is one of the simplest biometrics that can be achieved with minimal user-input, however facial recognition devices are often expensive and tailored to perform specific tasks with limited modular usage. We plan to develop a highly modular system based around facial recognition technology that allows user customization to perform specific tasks. 
The proposed facial recognition system will incorporate a Raspberry Pi microcontroller, a camera, and a touchscreen. The Raspberry Pi will process the images obtained from the camera, display them on a touchscreen, compare these images to a database of known users, and then perform a certain function specific to that user. This system will then be connected to additional components such as lights, speakers, and other components to allow performance of specific user required tasks. The initial task we propose is the use of this system to recognize and identify a person and then display certain user information such as name. In this use-case, once the system recognizes the individual as a known user, the system will display the user’s name.
After completion of this use case, other implementations of this system will then be developed to expand the functions of this system. Other proposed tasks include playing music from a user’s playlist, switching on lights, or outputting user-specific information (e.g. calendar, agenda, or stock prices).

*Revised 11/05/15*


#Updated Thoughts - 10/29/15
##Modifcations to the Inputs and Outputs of the Facial Recognition without Modifying the Facial Recognition Software
Concept discussion with Jordan and Jacob, we will move away from security aspect of facial recognition and towards personalization aspect. In effect, the system will recognize the user's face and then provide outputs based on that user's preferences. These outputs could include a touchscreen or any hardware (neostix - shows colors, speakers, lights, sounds, smells). For example, after detecting Anand's face, it will turn on a blue light and play a certain song that I like. 

Progress: We were able to get facial identification working using the adafruit tutorial. We had to remove any mention of RPIO.GPIO as this is not a command supported in Raspberry Pi 2. We modified the box2.py file and trained the pi-rec software to Dan's face and were able to positively identify him. However, the system could not recognize anyone else's face (tried 2 people)
