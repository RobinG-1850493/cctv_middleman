#!/usr/bin/env python
import rospy
import os
import time
import sys
from std_msgs.msg import String


def callback(data):
    msg = str(data.data)
    if msg.__contains__("openpose"):
        splitmsg = str(msg).split(' ')
        os.system("~/Robin/catkin_ws/src/cctv_middleman/src/scripts/openpose.sh stream_" + splitmsg[1] + " openpose_" + splitmsg[1])
    elif msg.__contains__("tracking"):
        #os.system("rosnode kill `rosnode list | grep rostopic_`")
        splitmsg = str(msg).split(' ')
        os.system("~/Robin/catkin_ws/src/cctv_middleman/src/scripts/tracking.sh stream_" + splitmsg[1] + " tracking_" + splitmsg[1])
    elif msg.__contains__("personcounter"):
        splitmsg = str(msg).split(' ')
        os.system("python ~/Robin/PersonCounter/PersonCounter_ROS.py --input stream_" + splitmsg[1] + " --output personcounter_"+ splitmsg[1])

def quit_al(data):
    msg = str(data.data)
    if msg.__contains__("op_quit"):
        os.system("killall openpose_ros_node")

    elif msg.__contains__("tr_quit"):
        os.system("rosnode kill /image_converter_node")

    elif msg.__contains__("pc_quit"):
        os.system("rosnode kill `rosnode list | grep person_counter`")

def listener():
    rospy.init_node('middleman_node', anonymous=True)
    rospy.Subscriber("middleman", String, callback)
    rospy.Subscriber("middleman_quit", String, quit_al)
    rospy.spin()


if __name__ == '__main__':
    listener()