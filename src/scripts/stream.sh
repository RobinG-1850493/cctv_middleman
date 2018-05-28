#!/bin/bash

rosrun dlink_camera connect.py 192.168.3.114/video2.mjpg --topic /stream_1 &
rosrun dlink_camera connect.py 192.168.3.116/video2.mjpg --topic /stream_2 &
rosrun dlink_camera connect.py 192.168.3.117/video2.mjpg --topic /stream_3 &
rosrun dlink_camera connect.py 192.168.3.118/video2.mjpg --topic /stream_4 &
rosrun dlink_camera connect.py 192.168.3.119/video2.mjpg --topic /stream_5 &
rosrun dlink_camera connect.py 192.168.3.120/video2.mjpg --topic /stream_6 &
