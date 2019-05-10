#!/usr/bin/env python

import aiml
import sys
import os

#Changing current directory to the path of aiml files
#This path will change according to your location of aiml files

os.chdir('/home/lentin/Desktop/aiml-files')
mybot = aiml.Kernel()

#If there is a brain file named standard.brn, Kernel() will initialize using bootstrap() method

if os.path.isfile("standard.brn"):
	mybot.bootstrap(brainFile = "standard.brn")

else:
	#If there is not brain file, load all AIML files and save a new brain
	mybot.bootstrap(learnFiles = "startup.xml", commands = "load aiml b")
	mybot.saveBrain("standard.brn")

#This loop ask for response from user and print the output from Kernel() object
while True:
	print mybot.respond(raw_input("Enter input >"))
