#!/usr/bin/env python

import rospy, os, sys
from sound_play.msg import SoundRequest
from sound_play.libsoundplay import SoundClient

if __name__ == '__main__':
    rospy.init_node('soundplay_test', anonymous = True)
    soundhandle = SoundClient()
    rospy.sleep(1)

    soundhandle.stopAll()

    print 'Starting TTS'
    soundhandle.say('Hello world!')
    rospy.sleep(3)
        
    s = soundhandle.voiceSound("Hello World")
    s.play()
    rospy.sleep(3)
