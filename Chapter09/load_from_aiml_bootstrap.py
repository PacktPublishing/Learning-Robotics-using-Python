#!/usr/bin/env python
import aiml
import sys
import os

os.chdir('/home/lentin/Desktop/aiml-files')
mybot = aiml.Kernel()
mybot.learn('startup.xml')
mybot.respond('load aiml b')
#Saving loaded patterns into a brain file
mybot.saveBrain('standard.brn')


while True:
	print mybot.respond(raw_input("Enter input >"))

