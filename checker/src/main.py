#! /usr/bin/env python
import rospy
import numpy as np
from checker.msg import Coord



rospy.init_node('Checker')
pub = rospy.Publisher('/coord', Coord, queue_size=1)
val = Coord()
while(True):

    val.data = raw_input("Move: ")
    val.wall = raw_input("Is there a wall? (Yes, no) : ")
    pub.publish(val)

rospy.spin()