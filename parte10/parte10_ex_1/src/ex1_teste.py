#!/usr/bin/env python
from math import sin ,cos
import rospy
from sensor_msgs import point_cloud2
from sensor_msgs.msg import LaserScan
from sensor_msgs.msg import PointCloud2, PointField
from std_msgs.msg import Header

# global variables
pub= None

def callback(msg):
    nmeasurements= len(msg.ranges)
    rospy.loginfo("I receveid " + str(nmeasurements) + "measurement")

    # create point list
    points = []
    i= 0
    for range in msg.ranges:
        theta = msg.angle_min + i * msg.angle_increment
        x= range * cos(theta)
        y= range * sin(theta)
        z= 0
        pt = [x, y, z]
        points.append(pt)
        i= i+1

    fields = [PointField('x', 0, PointField.FLOAT32, 1),
              PointField('y', 4, PointField.FLOAT32, 1),
              PointField('z', 8, PointField.FLOAT32, 1)
              ]
    header = Header()
    header.frame_id = msg.header.frame_id
    pc2 = point_cloud2.create_cloud(header, fields, points)
    global pub
    pub.publish(pc2)

def listener():

    rospy.init_node('listener', anonymous=False)

    rospy.Subscriber("/left_laser/laserscan", LaserScan, callback)
    global pub
    pub = rospy.Publisher('~point_cloud', PointCloud2, queue_size=10)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    listener()
