#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import JointState

def callback(data):
    # Update the manipulator arm's joint positions based on received message
    # The updated joint positions can be extracted from 'data.position'
    joint1_pos = data.position[0]
    joint2_pos = data.position[1]
    joint3_pos = data.position[2]
    joint4_pos = data.position[3]
    joint5_pos=data.position[4]


    # Perform any processing or control logic based on the received joint positions

def main():
    rospy.init_node('joint_subscriber')
    rospy.Subscriber('/joint_states', JointState, callback)
    rospy.spin()

if __name__ == '__main__':
    main()