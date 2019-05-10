#!/usr/bin/env python



import gobject
import sys

#The following modules need to import before handling gstreamer API's
import pygst
pygst.require('0.10')
gobject.threads_init()
import gst


#Module to handle keyboard interrupt signal
import signal


#Signal handler routine
def signal_handle(signal, frame):
	print "You pressed Ctrl+C"
	sys.exit(0)



#Speech recognition class
class Speech_Recog(object):


	#Initializing gstreamer pipeline and pocketsphinx element
	def __init__(self):
		self.init_gst()

	
	#This function will initialize gstreamer pipeline
	def init_gst(self):
	        """Initialize the speech components"""
		#Install
		#sudo apt-get install gstreamer0.10-gconf for gconf

		#The following line create a gstreamer pipeline and pipeline description.
		#This code need following element to start recognition
        	self.pipeline = gst.parse_launch('gconfaudiosrc ! audioconvert ! audioresample '
                                         + '! vader name=vad auto-threshold=true '
                                         + '! pocketsphinx name=asr ! fakesink')

		#Accessing pocketsphinx element from gstreamer pipeline
        	asr = self.pipeline.get_by_name('asr')
		#Connecting to asr_result function when a conversion is completed
        	asr.connect('result', self.asr_result)

		#We can mention lm and dict for accurate detection
#	        asr.set_property('lm', '/home/user/mylanguagemodel.lm')
#        	asr.set_property('dict', '/home/user/mylanguagemodel.dic')

		#This option will set every option is configured well and can start recognition
        	asr.set_property('configured', True)
        	self.pipeline.set_state(gst.STATE_PAUSED)


    	def asr_result(self, asr, text, uttid):
		#Printing the detected text
		print "Detected Text=>    ",text



	#This function will start/stop Speech recognition operation
	def start_recognition(self):
		

		#VADER - Voice Activity DEtectoR, which helps when the speech start and when its ends
		#Creating VADER object and set the property silent to False, so no speech will detected
	        vader = self.pipeline.get_by_name('vad')
        	vader.set_property('silent', False)
		#Waiting for a key press to start recognition
		raw_input("Press any key to start recognition:>")
		#Start playing the pipeline in a thread
		self.pipeline.set_state(gst.STATE_PLAYING)

		#Waiting for stopping the recognition
		raw_input("Press any key to stop recognition:>")
	        vader = self.pipeline.get_by_name('vad')
		#Setting silent property of VADER to True 
        	vader.set_property('silent', True)
		#Pausing GStreamer pipeline
      		self.pipeline.set_state(gst.STATE_PAUSED)


if __name__ == "__main__":

	#Creating an object of Speech_Recog() class
	app_object = Speech_Recog()


	#Repeat the recognition until keyboard interrupt

	signal.signal(signal.SIGINT, signal_handle)

	while True:

		#Calling Speech recognition routine
		app_object.start_recognition()
