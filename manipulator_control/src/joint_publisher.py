#!/usr/bin/env python3

import sys
import rospy
from manipulator_control.msg import JointPositions
from sensor_msgs.msg import JointState

def main():
    if len(sys.argv) != 6:
        print("Usage: joint_publisher.py <joint1_position> <joint2_position> <joint3_position> <joint4_position> <joint5_position>")
        return

    try:
        joint1_pos = float(sys.argv[1])
        joint2_pos = float(sys.argv[2])
        joint3_pos = float(sys.argv[3])
        joint4_pos=float(sys.argv[4])
        joint5_pos=float(sys.argv[5])

    except ValueError:
        print("Error: Joint positions must be valid numbers.")
        return

    rospy.init_node('joint_publisher')
    pub = rospy.Publisher('joint_positions', JointPositions, queue_size=10)
    joint_state_pub = rospy.Publisher('/joint_states', JointState, queue_size=10)
    rate = rospy.Rate(10)  # Publish at 10 Hz

    while not rospy.is_shutdown():
        joint_positions = JointPositions()
        joint_positions.positions = [joint1_pos, joint2_pos, joint3_pos,joint4_pos,joint5_pos]
        pub.publish(joint_positions)

        # Also publish joint state to /joint_states for visualization in RViz
        joint_state_msg = JointState()
        joint_state_msg.header.stamp = rospy.Time.now()
        joint_state_msg.name = ['joint1', 'joint2', 'joint3','joint4','joint5']
        joint_state_msg.position = [joint1_pos, joint2_pos, joint3_pos,joint4_pos,joint5_pos]
        joint_state_pub.publish(joint_state_msg)

        rate.sleep()

if __name__ == '__main__':
    main()
