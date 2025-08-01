#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Point
from drone_system.msg import DroneTelemetry

def publisher():
    pub = rospy.Publisher('telemetry', DroneTelemetry, queue_size=10)
    rospy.init_node('drone_publisher', anonymous=True)
    rate = rospy.Rate(1)  # 1 Hz

    while not rospy.is_shutdown():
        msg = DroneTelemetry()
        msg.drone_id = rospy.get_param("~drone_id", "drone1")
        msg.position = Point(1.0, 2.0, 3.0)
        msg.battery_level = 18.0  # simulate low battery
        msg.is_emergency = False

        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
