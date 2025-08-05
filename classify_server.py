#!/usr/bin/env python3
import rospy
from your_package_name.srv import ClassifyObject, ClassifyObjectResponse

def handle_classify(req):
    volume = req.length * req.width * req.height
    if volume < 1000:
        classification = "Small"
    elif volume < 5000:
        classification = "Medium"
    else:
        classification = "Large"
    rospy.loginfo(f"Object volume: {volume}, Classified as: {classification}")
    return ClassifyObjectResponse(classification=classification)

def classify_server():
    rospy.init_node('classify_server')
    service = rospy.Service('/classify_object', ClassifyObject, handle_classify)
    rospy.loginfo("Object classification server ready at /classify_object")
    rospy.spin()

if __name__ == '__main__':
    classify_server()
