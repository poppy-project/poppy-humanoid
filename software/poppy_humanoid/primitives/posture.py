from __future__ import division

import time
import itertools

import pypot.primitive


class InitRobot(pypot.primitive.Primitive):

    def setup(self):
        self.robot.compliant = False
        self.robot.power_up()

        # Change PID of Dynamixel MX motors
        for m in filter(lambda m: hasattr(m, 'pid'), self.robot.motors):
            m.pid = (4, 2, 0)
        for m in self.robot.torso:
            m.pid = (6, 2, 0)

        # Reduce max torque to keep motor temperature low
        for m in self.robot.motors:
            m.torque_limit = 70

        time.sleep(0.5)

    def run(self):
        pass


class StandPosition(InitRobot):
    def run(self):
        # Goto to position 0 on all motors
        self.robot.goto_position(dict(zip((m.name for m in self.robot.motors), itertools.repeat(0))), 2, wait=True)

        # Specified some motor positions to keep the robot balanced
        self.robot.goto_position({'r_hip_z': -2,
                                  'l_hip_z': 2,
                                  'r_hip_x': -2,
                                  'l_hip_x': 2,
                                  'l_shoulder_x': 20,
                                  'r_shoulder_x': -20,
                                  'l_shoulder_y': 10,
                                  'r_shoulder_y': 10,
                                  'l_elbow_y': -20,
                                  'r_elbow_y': -20,
                                  'l_ankle_y': -3,
                                  'r_ankle_y': -2,
                                  'abs_y': -2,
                                  'head_y': 1,
                                  'head_z': 0},
                                 3,
                                 wait=True)

        # Restore the motor speed
        self.robot.power_up()

        # Reduce max torque to keep motor temperature low
        for m in self.robot.motors:
            m.torque_limit = 70

        time.sleep(1)


class SitPosition(pypot.primitive.Primitive):
    def run(self):
        self.robot.goto_position({'l_hip_y': -39,
                                  'r_hip_y': -39,
                                  'l_knee_y': 134,
                                  'r_knee_y': 134,
                                  'abs_x': 0,
                                  'abs_y': 3,
                                  'abs_z': 0,
                                  'bust_x': 0,
                                  'bust_y': 0,
                                  },
                                 2,
                                 wait=True)

        motor_list = [self.robot.l_knee_y, self.robot.l_ankle_y, self.robot.r_knee_y, self.robot.r_ankle_y]

        for m in motor_list:
            m.compliant = True

        for m in self.robot.legs:
            m.torque_limit = 20

        time.sleep(2)
