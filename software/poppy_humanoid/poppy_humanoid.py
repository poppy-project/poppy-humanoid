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

        for m in robot.motors:
            m.compliant_behavior = 'safe'
            m.default_goto_behavior = 'minjerk'

        robot.attach_primitive(StandPosition(robot), 'stand_position')
        robot.attach_primitive(SitPosition(robot), 'sit_position')
        robot.attach_primitive(LimitTorque(robot), 'limit_torque')
        robot.attach_primitive(SimpleBodyBeatMotion(robot, 50), 'dance_beat_motion')

        # robot.limit_torque.start()
