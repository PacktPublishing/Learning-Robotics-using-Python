#!/usr/bin/env python
import aiml
import sys

mybot = aiml.Kernel()
mybot.learn(sys.argv[1])

while True:
	print mybot.respond(raw_input("Enter input >"))

