#!/usr/bin/env python3
import sys
import rospy
import argparse
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg


def move_to_position(positions):
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node("move_group_python_interface_tutorial", anonymous=True)
    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()
    group_name = "arm_group"
    move_group = moveit_commander.MoveGroupCommander(group_name)
    joint_goal = move_group.get_current_joint_values()

    if len(positions) != len(joint_goal):
        rospy.logerr("Number of target positions does not match the number of joints.")
        return
    
    for i in range(len(positions)):
        joint_goal[i] = positions[i]
    move_group.go(joint_goal, wait=True)
    move_group.stop()    


if __name__ == '__main__':
    try:
        # Move the arm to the target position
        parser = argparse.ArgumentParser(description='Move a robotic arm to target joint positions.')
        parser.add_argument('target_positions', type=float, nargs='+', help='Target joint positions')
        args = parser.parse_args()

        move_to_position(args.target_positions)

    except Exception as e:
        rospy.logerr(e)

    finally:
        # Shutdown MoveIt
        moveit_commander.roscpp_shutdown()
