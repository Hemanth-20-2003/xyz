#!/usr/bin/env python3
import rospy
from pkg_22brs1150.srv import SetSpeed

def set_speed_client():
    rospy.init_node('speed_client')
    rospy.wait_for_service('/set_speed')
    try:
        set_speed = rospy.ServiceProxy('/set_speed', SetSpeed)
        linear = float(input("Enter linear velocity (m/s): "))
        angular = float(input("Enter angular velocity (rad/s): "))
        response = set_speed(linear, angular)
        print(f"Response: Success={response.success}, Message='{response.message}'")
    except rospy.ServiceException as e:
        print(f"Service call failed: {e}")

if __name__ == '__main__':
    set_speed_client()
