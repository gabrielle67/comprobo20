#!/usr/bin/env python3

import tty
import select
import sys
import termios
import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3

#initialize node first
rospy.init_node('teleop')
#rospy publisher
rosPub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

#twist needs vector3 variables
w = Twist(Vector3(1,0,0), Vector3(0,0,0))
a = Twist(Vector3(0,0,0), Vector3(0,0,1))
s = Twist(Vector3(-1,0,0), Vector3(0,0,0))
d = Twist(Vector3(0,0,0), Vector3(0,0,-1))
wait = Twist(Vector3(0,0,0), Vector3(0,0,0))

def getKey():
    #get key info provided by class
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

settings = termios.tcgetattr(sys.stdin)
key=getKey()

while key != '\x03':
    key = getKey()
    if key == 'w':
        print("w")
        rosPub.publish(w)
    elif key == 'a':
        rosPub.publish(a)
    elif key == 's':
        rosPub.publish(s)
    elif key == 'd':
        rosPub.publish(d)
    else:
        rosPub.publish(wait)
    print("waiting...")


