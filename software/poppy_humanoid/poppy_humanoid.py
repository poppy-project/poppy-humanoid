import numpy

from functools import partial

from poppy.creatures import AbstractPoppyCreature

from .primitives.safe import LimitTorque
from .primitives.posture import StandPosition, SitPosition
from .primitives.dance import SimpleBodyBeatMotion


class PoppyHumanoid(AbstractPoppyCreature):
    @classmethod
    def setup(cls, robot):
        robot._primitive_manager._filter = partial(numpy.sum, axis=0)

        if robot.simulated:
            cls.vrep_hack(robot)
        for m in robot.motors:
            m.compliant_behavior = 'safe'
            m.goto_behavior = 'minjerk'

        robot.attach_primitive(StandPosition(robot), 'stand_position')
        robot.attach_primitive(SitPosition(robot), 'sit_position')
        robot.attach_primitive(LimitTorque(robot), 'limit_torque')
        robot.attach_primitive(SimpleBodyBeatMotion(robot, 50), 'dance_beat_motion')

        # robot.limit_torque.start()
    @classmethod
    def vrep_hack(cls, robot):
        # fix vrep orientation bug
        wrong_motor = [robot.r_knee_y, robot.abs_x, robot.bust_x]

        for m in wrong_motor:
            m.direct = not m.direct
            m.offset = -m.offset
