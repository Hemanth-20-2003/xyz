#!/usr/bin/env python3
import rospy
from your_package_name.srv import ClassifyObject

def classify_client():
    rospy.init_node('classify_client')
    rospy.wait_for_service('/classify_object')
    try:
        classify = rospy.ServiceProxy('/classify_object', ClassifyObject)
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))
        response = classify(length, width, height)
        print(f"Classification: {response.classification}")
    except rospy.ServiceException as e:
        print(f"Service call failed: {e}")

if __name__ == '__main__':
    classify_client()
