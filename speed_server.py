#!/usr/bin/env python3
import rospy
from pkg_22brs1150.srv import SetSpeed, SetSpeedResponse

def handle_set_speed(req):
    rospy.loginfo(f"Received speed - Linear: {req.linear}, Angular: {req.angular}")
    message = f"Speed set to Linear: {req.linear} m/s, Angular: {req.angular} rad/s"
    return SetSpeedResponse(success=True, message=message)

def speed_server():
    rospy.init_node('speed_server')
    service = rospy.Service('/set_speed', SetSpeed, handle_set_speed)
    rospy.loginfo("Speed service server ready at /set_speed")
    rospy.spin()

if __name__ == '__main__':
    speed_server()
