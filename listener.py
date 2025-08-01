#!/usr/bin/env python

import rospy
from drone_system.msg import DroneTelemetry

def callback(msg):
    if msg.battery_level < 20.0 or msg.is_emergency:
        rospy.logwarn(f"[{msg.drone_id}] Warning! Battery: {msg.battery_level}%, Emergency: {msg.is_emergency}")
    else:
        rospy.loginfo(f"[{msg.drone_id}] Battery OK.")

def listener():
    rospy.init_node('drone_monitor', anonymous=True)
    rospy.Subscriber('telemetry', DroneTelemetry, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
