from numpy import mean
from collections import deque

from pypot.primitive import LoopPrimitive


class ArmsTurnCompliant(LoopPrimitive):
    """ Automatically turns the arms compliant when a force is applied. """
    def setup(self):
        for m in self.robot.arms:
            m.compliant = False
            m.torque_limit = 20

        freq = 1. / self.period
        self.l_arm_torque = deque([0], 0.2 * freq)
        self.r_arm_torque = deque([0], 0.2 * freq)

    def update(self):
        for side in ('l', 'r'):
            recent_arm_torques = getattr(self, '{}_arm_torque'.format(side))
            motors = getattr(self.robot, '{}_arm'.format(side))

            recent_arm_torques.append(max([abs(m.present_load) for m in motors]))

            mt = mean(recent_arm_torques)

            if mt > 20:
                for m in motors:
                    m.compliant = True
            elif mt < 7:
                for m in motors:
                    m.compliant = False


class PuppetMaster(LoopPrimitive):
    """ Apply the motion made on the left arm to the right arm. """
    def setup(self):
        for m in self.robot.arms:
            m.moving_speed = 0.
            m.torque_limit = 50.

        for m in self.robot.l_arm:
            m.compliant = True

        for m in self.robot.r_arm:
            m.compliant = False

    def update(self):
        for lm, rm in zip(self.robot.l_arm, self.robot.r_arm):
            rm.goal_position = lm.present_position * (1 if lm.direct else -1)

    def teardown(self):
        for m in self.robot.arms:
            m.compliant = False

        self.robot.goto_position({m.name: 0. for m in self.robot.arms},
                                 2., wait=True)

        for m in self.robot.arms:
            m.moving_speed = 0.
