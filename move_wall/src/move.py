#! /usr/bin/env python
import rospy
import numpy as np
import time as t
from geometry_msgs.msg import Twist
from checker.msg import Coord
from sensor_msgs.msg import LaserScan


tt0 = None
def checkWall(msg):
    if (msg.wall == "Yes"):
        sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)

def callback(msg):  
    right = msg.ranges[0]
    left = msg.ranges[719]
    forward = msg.ranges[360]
    if(right > 1):
        cmd.angular.z = 0
        cmd.linear.x = 0
        pub.publish(cmd)
        t.sleep(1)
        cmd.angular.z = -0.2
        cmd.linear.x = 0
        pub.publish(cmd)
        t.sleep(6.7)
        cmd.angular.z = 0
        cmd.linear.x = 0
        pub.publish(cmd)
        t.sleep(1)
        cmd.angular.z = 0
        cmd.linear.x = 1
        pub.publish(cmd)
        t.sleep(1.5)

        cmd.angular.z = 0
        cmd.linear.x = 0
        pub.publish(cmd)
        t.sleep(1)
        cmd.angular.z = -0.2
        cmd.linear.x = 0
        pub.publish(cmd)
        t.sleep(7.0)
        cmd.angular.z = 0
        cmd.linear.x = 0
        pub.publish(cmd)

        cmd.linear.x = 1
        cmd.angular.z = 0
        t.sleep(counter)

        cmd.angular.z = 0.2
        cmd.linear.x = 0
        pub.publish(cmd)
        t.sleep(7.0)
        cmd.angular.z = 0
        cmd.linear.x = 0
        pub.publish(cmd)

    else:
        counter += 1
        cmd.angular.z = 0
        cmd.linear.x = 1
        t.sleep(1)


    if (forward > 1):

        if (right > 1):
            tw.angular.z = 0
            tw.linear.x = 0
            pub.publish(tw)
            t.sleep(1)
            tw.angular.z = -0.2
            tw.linear.x = 0
            pub.publish(tw)
            t.sleep(6.7)
            cmd.angular.z = 0.1
            pub.publish(cmd)
        elif (left < 1):
            cmd.angular.z = -0.1
            pub.publish(cmd)
        else:
            cmd.linear.x = 0.1
            cmd.angular.z = 0
            pub.publish(cmd)
    else:
        cmd.angular.z = 0.1
        cmd.linear.x = 0.0
        pub.publish(cmd)

            

rospy.init_node('move')
sub = rospy.Subscriber('/coord', Coord, checkWall)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
cmd = Twist()

rospy.spin()