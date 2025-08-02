#!/usr/bin/env python3

import rospy
from your_package_name.msg import DroneTelemetry  # Replace with your actual package name

def telemetry_callback(msg):
    if msg.battery_level < 20.0 or msg.is_emergency:
        rospy.logwarn(f"[{msg.drone_id}] Warning - Battery: {msg.battery_level}%, Emergency: {msg.is_emergency}")
    else:
        rospy.loginfo(f"[{msg.drone_id}] OK - Battery: {msg.battery_level}%, Position: {msg.position}")

def main():
    rospy.init_node('drone_monitor')
    topic_name = rospy.get_param('~telemetry_topic', '/drone1/telemetry')
    rospy.Subscriber(topic_name, DroneTelemetry, telemetry_callback)
    rospy.loginfo(f"Subscribed to topic: {topic_name}")
    rospy.spin()

if __name__ == '__main__':
    main()
