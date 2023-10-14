#!/usr/bin/env python3

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg


from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list


class MoveGroupPythonInterfaceTutorial(object):
    """MoveGroupPythonInterfaceTutorial"""
    def __init__(self):
        super(MoveGroupPythonInterfaceTutorial, self).__init__()

        ## First initialize `moveit_commander`_ and a `rospy`_ node:
        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node("move_group_python_interface_tutorial", anonymous=True)

        ## Instantiate a `RobotCommander`_ object. Provides information such as the robot's
        ## kinematic model and the robot's current joint states
        robot = moveit_commander.RobotCommander()

        ## Instantiate a `PlanningSceneInterface`_ object.  This provides a remote interface
        ## for getting, setting, and updating the robot's internal understanding of the
        ## surrounding world:
        scene = moveit_commander.PlanningSceneInterface()

        ## Instantiate a `MoveGroupCommander`_ object.  This object is an interface
        ## to a planning group (group of joints).  In this tutorial the group is the primary
        ## arm joints in the Panda robot, so we set the group's name to "panda_arm".
        ## If you are using a different robot, change this value to the name of your robot
        ## arm planning group.
        ## This interface can be used to plan and execute motions:
        group_name = "arm_group"
        move_group = moveit_commander.MoveGroupCommander(group_name)

        ## Create a `DisplayTrajectory`_ ROS publisher which is used to display
        ## trajectories in Rviz:
        display_trajectory_publisher = rospy.Publisher(
            "/move_group/display_planned_path",
            moveit_msgs.msg.DisplayTrajectory,
            queue_size=20,
        )

        # We can get the name of the reference frame for this robot:
        planning_frame = move_group.get_planning_frame()
        print("============ Planning frame: %s" % planning_frame)

        # We can get a list of all the groups in the robot:
        group_names = robot.get_group_names()
        print("============ Available Planning Groups:", robot.get_group_names())

        # Sometimes for debugging it is useful to print the entire state of the
        # robot:
        print("============ Printing robot state")
        print(robot.get_current_state())
        print("")

         # Misc variables
        self.box_name = ""
        self.robot = robot
        self.scene = scene
        self.move_group = move_group
        self.display_trajectory_publisher = display_trajectory_publisher
        self.planning_frame = planning_frame
        self.group_names = group_names

    def zero_state(self):    
        move_group = self.move_group
        joint_goal = move_group.get_current_joint_values()
        joint_goal[0] = 0
        joint_goal[1] = 0
        joint_goal[2] = 0
        joint_goal[3] = 0
        joint_goal[4] = 0

        # The go command can be called with joint values, poses, or without any
        # parameters if you have already set the pose or joint target for the group
        move_group.go(joint_goal, wait=True)

        # Calling ``stop()`` ensures that there is no residual movement
        move_group.stop()
    
    
    def straight_up_pose(self):
        move_group=self.move_group
        joint_goal=move_group.get_current_joint_values()
        joint_goal[0] = 0
        joint_goal[1] = 0
        joint_goal[2] = -1.47
        joint_goal[3] = 0
        joint_goal[4] = 0
        move_group.go(joint_goal, wait=True)
        move_group.stop() 


    def pick_object_pose(self):
        move_group=self.move_group
        joint_goal=move_group.get_current_joint_values()
        joint_goal[0] = 0
        joint_goal[1] = -1.47
        joint_goal[2] = 0
        joint_goal[3] = 0
        joint_goal[4] = 1.57
        move_group.go(joint_goal, wait=True)
        move_group.stop() 

    def lift_object_pose(self):
        move_group=self.move_group
        joint_goal=move_group.get_current_joint_values()
        joint_goal[0] = 0
        joint_goal[1] = -0.3556
        joint_goal[2] = -0.6296
        joint_goal[3] = 0
        joint_goal[4] = 1.57
        move_group.go(joint_goal, wait=True)
        move_group.stop() 
    
    def opposite_pose(self):
        move_group=self.move_group
        joint_goal=move_group.get_current_joint_values()
        joint_goal[0] = 3.14
        joint_goal[1] = -0.3556
        joint_goal[2] = -0.6296
        joint_goal[3] = 0
        joint_goal[4] = 1.57
        move_group.go(joint_goal, wait=True)
        move_group.stop() 
    
    def place_object_opposite_pose(self):
        move_group=self.move_group
        joint_goal=move_group.get_current_joint_values()
        joint_goal[0] = 3.14
        joint_goal[1] = -1.47
        joint_goal[2] = -0.1605
        joint_goal[3] = 0
        joint_goal[4] = 1.57
        move_group.go(joint_goal, wait=True)
        move_group.stop() 

    
    
    
    def automate_movement_sequence(self):
        self.zero_state()
        self.straight_up_pose()
        self.pick_object_pose()
        self.lift_object_pose()
        self.opposite_pose()
        self.place_object_opposite_pose()
        

def main():
    try:
        print("")
        print("Welcome to the MoveIt MoveGroup Python Interface")
        print("Automating the movement sequence...")
        print("Press Ctrl-C to interrupt at any time")
        print("")
        tutorial = MoveGroupPythonInterfaceTutorial()
        tutorial.automate_movement_sequence()

    except rospy.ROSInterruptException:
        return
    except KeyboardInterrupt:
        return
       
if __name__ == "__main__":
    main()       

