#!/usr/bin/env python3
import sys
import rospy
import moveit_commander

def get_joint_positions(move_group, target_name):
    # Set the named target
    move_group.set_named_target(target_name)

    # Get the joint values of the named target
    joint_values = move_group.get_named_target_values(target_name)

    return joint_values

if __name__ == '__main__':
    try:
        # Initialize ROS node and MoveIt
        rospy.init_node('get_joint_positions_node')
        moveit_commander.roscpp_initialize(sys.argv)
        robot = moveit_commander.RobotCommander()
        group_name = "arm_group"  # Replace with your MoveIt move group name
        move_group = moveit_commander.MoveGroupCommander(group_name)

        # Get joint positions for a specific named target
        target_name = "place_object_opposite_pose"  # Replace with the name of the predefined pose you want to retrieve
        joint_positions = get_joint_positions(move_group, target_name)

        # Print the joint positions
        print("Joint Positions for Named Target '{}':".format(target_name))
        print(joint_positions)

    except rospy.ROSInterruptException:
        pass
