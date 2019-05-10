#!/usr/bin/env python

import aiml
import sys
import os

#Change the current path to your aiml files path
os.chdir('/home/lentin/Desktop/aiml-files')
mybot = aiml.Kernel()

#Learn startup.xml
mybot.learn('startup.xml')

#Calling load aiml b for loading all AIML files
mybot.respond('load aiml b')

while True:
	print mybot.respond(raw_input("Enter input >"))
