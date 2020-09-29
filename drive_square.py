#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PointStamped, Point #get current point
from std_msgs.msg import Header #provides timestamp and frame ID



Class Drive_Square():
    def __init__(self):
    #initializing ros
    rospy.init_node("drive_square")
    rosPub = rospy.Publisher("cmd_vel", PointStamped, queue_size=10)
    #rosSub = rospy.Subscriber("/odom", Odometry) no longer needed

    def square(self, init):
        curr = rospy.get_time()
        time = curr - init
        head = Header(stamp = rospy.Time.time(), frame_id = "base_link")

        if time <= 5:
            x = Point(1,0,1)
        elif 5 > time <= 10:
            x = Point (1,1,1)
        elif 10 > time <= 15
            x = Point (0,1,1)
        elif time > 15
            x = Point(0,0,1)
        return (PointStamped(header=head), point=x)

    #constantly do square
    def doSquare(self):
        while rospy.get_time != 0:
            x = rospy.get_time()

            self.rosPub.publish(self.square)

    #run program
    if __name__ == '__main__'
        Drive_Square.run()