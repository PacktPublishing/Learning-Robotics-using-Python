#!/usr/bin/env python
import rospy
import aiml
import os

rospy.init_node('aiml_server')
print "Hello"
print os.getcwd()		
print os.path.dirname(__file__)

data_path = rospy.get_param("aiml_path")

print data_path

