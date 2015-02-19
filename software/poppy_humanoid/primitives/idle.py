from __future__ import division

import pypot.primitive
from pypot.primitive.utils import Sinus


class UpperBodyIdleMotion(pypot.primitive.LoopPrimitive):
    def __init__(self, robot, freq):
        pypot.primitive.LoopPrimitive.__init__(self, robot, freq)

        sinus_args = [{'motor_list': [self.robot.abs_z, ], 'amp': 3, 'freq': 0.2},
                      {'motor_list': [self.robot.abs_z, ], 'amp': 0.8, 'freq': 0.5},
                      {'motor_list': [self.robot.l_shoulder_x, ], 'amp': 2, 'freq': 0.2, 'offset': 5},
                      {'motor_list': [self.robot.l_shoulder_x, ], 'amp': 0.8, 'freq': 0.5, 'offset': 0},
                      {'motor_list': [self.robot.r_shoulder_x, ], 'amp': 2, 'freq': 0.2, 'offset': -5, 'phase': 66},
                      {'motor_list': [self.robot.r_shoulder_x, ], 'amp': 0.8, 'freq': 0.5, 'offset': 0, 'phase': 66},
                      {'motor_list': [self.robot.l_shoulder_y, ], 'amp': 3, 'freq': 0.2, 'offset': 15},
                      {'motor_list': [self.robot.l_shoulder_y, ], 'amp': 0.8, 'freq': 0.5, 'offset': 0},
                      {'motor_list': [self.robot.l_elbow_y, ], 'amp': 2, 'freq': 0.5, 'offset': -25},
                      {'motor_list': [self.robot.l_elbow_y, ], 'amp': 0.3, 'freq': 0.2},
                      {'motor_list': [self.robot.r_elbow_y, ], 'amp': 2, 'freq': 0.5, 'offset': -25, 'phase': 75},
                      {'motor_list': [self.robot.r_elbow_y, ], 'amp': 0.3, 'freq': 0.2, 'phase': 75},
                      {'motor_list': [self.robot.l_arm_z, ], 'amp': 3, 'freq': 0.2},
                      {'motor_list': [self.robot.r_arm_z, ], 'amp': 3, 'freq': 0.2, 'phase':78}]

        self.all_sinus = [Sinus(self.robot, 50, **s) for s in sinus_args]

    def setup(self):
        for m in self.robot.torso + self.robot.arms:
            m.compliant = False

        [all_sinus.start() for all_sinus in self.all_sinus]

    def teardown(self):
        [all_sinus.stop() for all_sinus in self.all_sinus]

    def update(self):
        pass


class HeadIdleMotion(pypot.primitive.LoopPrimitive):
    def __init__(self, robot, freq):
        pypot.primitive.LoopPrimitive.__init__(self, robot, freq)

        sinus_args = [{'motor_list': [self.robot.head_z, ], 'amp': 20, 'freq': 0.05},
                      {'motor_list': [self.robot.head_z, ], 'amp': 15, 'freq': 0.1},
                      {'motor_list': [self.robot.head_y, ], 'amp': 20, 'freq': 0.04},
                      {'motor_list': [self.robot.head_y, ], 'amp': 5, 'freq': 0.09}]

        self.head_sinus = [Sinus(self.robot, 50, **s) for s in sinus_args]

    def start(self):
        pypot.primitive.LoopPrimitive.start(self)

        for m in self.robot.head:
            m.compliant = False

        [hs.start() for hs in self.head_sinus]

    def pause(self):
        [hs.pause() for hs in self.head_sinus]

    def resume(self):
        [hs.resume() for hs in self.head_sinus]

    def stop(self):
        [hs.stop() for hs in self.head_sinus]
        pypot.primitive.LoopPrimitive.stop(self)

    def update(self):
        pass
