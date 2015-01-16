from poppy.creatures import AbstractPoppyCreature
from .primitives.safe import LimitTorque


class PoppyHumanoid(AbstractPoppyCreature):
    @classmethod
    def setup(cls, robot):
        robot.attach_primitive(LimitTorque(robot), 'limit_torque')
        robot.limit_torque.start()
