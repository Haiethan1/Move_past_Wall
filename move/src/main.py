#! /usr/bin/env python
import rospy
import numpy as np
import time as t
from geometry_msgs.msg import Twist
from checker.msg import Coord


tt0 = None
def callback(msg):  
    d = msg.data 
    w = msg.wall
    tw = Twist()
    if(msg.wall != "Yes"):
        if (d == "w"):
            tw.linear.x = 0.5
            
        elif (d == "s"):
            tw.linear.x = -0.5
        elif ( d == "d"):
            tw.angular.z = -0.5
        elif (d == "a"):
            tw.angular.z = 0.5
        else:
            pass
        pub.publish(tw)
        t.sleep(2)
        tw.angular.z = 0
        tw.linear.x = 0
        pub.publish(tw)



        
    
    

rospy.init_node('move')
sub = rospy.Subscriber('/coord', Coord, callback)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

rospy.spin()