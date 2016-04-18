import os
import numpy
import ctypes

from functools import partial

from poppy.creatures import AbstractPoppyCreature

from .primitives.safe import LimitTorque, TemperatureMonitor
from .primitives.dance import SimpleBodyBeatMotion
from .primitives.posture import StandPosition, SitPosition
from .primitives.idle import UpperBodyIdleMotion, HeadIdleMotion
from .primitives.interaction import ArmsTurnCompliant, PuppetMaster


class PoppyHumanoid(AbstractPoppyCreature):

    @classmethod
    def setup(cls, robot):
        robot._primitive_manager._filter = partial(numpy.sum, axis=0)

        if robot.simulated:
            cls.vrep_hack(robot)
            cls.add_vrep_methods(robot)

        for m in robot.motors:
            m.goto_behavior = 'dummy'

        for m in robot.torso:
            m.compliant_behavior = 'safe'

        # Attach default primitives:
        if not robot.simulated:
            sound_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                      'media', 'sounds', 'error.wav')
            robot.attach_primitive(TemperatureMonitor(robot, sound=sound_file), 'temperature_monitoring')
            robot.temperature_monitoring.start()

        # basic primitives:
        robot.attach_primitive(StandPosition(robot), 'stand_position')
        robot.attach_primitive(SitPosition(robot), 'sit_position')

        # Safe primitives:
        robot.attach_primitive(LimitTorque(robot), 'limit_torque')
        # robot.limit_torque.start()

        # Dance primitive:
        robot.attach_primitive(SimpleBodyBeatMotion(robot, 50), 'dance_beat_motion')

        # Idle primitives
        robot.attach_primitive(UpperBodyIdleMotion(robot, 50), 'upper_body_idle_motion')
        robot.attach_primitive(HeadIdleMotion(robot, 50), 'head_idle_motion')

        # Interaction primitives
        robot.attach_primitive(ArmsTurnCompliant(robot, 50), 'arms_turn_compliant')
        robot.attach_primitive(PuppetMaster(robot, 50), 'arms_copy_motion')

    @classmethod
    def vrep_hack(cls, robot):
        # fix vrep orientation bug
        wrong_motor = [robot.r_knee_y, robot.abs_x, robot.bust_x]

        for m in wrong_motor:
            m.direct = not m.direct
            m.offset = -m.offset

    @classmethod
    def add_vrep_methods(cls, robot):
        from pypot.vrep.controller import VrepController
        from pypot.vrep.io import remote_api

        def set_vrep_force(robot, vector_force, shape_name):
            """ Set a force to apply on Poppy Humanoid. """
            vrep_io = next(c for c in robot._controllers
                           if isinstance(c, VrepController)).io

            raw_bytes = (ctypes.c_ubyte * len(shape_name)).from_buffer_copy(shape_name)
            vrep_io.call_remote_api('simxSetStringSignal', 'shape',
                                    raw_bytes, sending=True)

            packedData = remote_api.simxPackFloats(vector_force)
            raw_bytes = (ctypes.c_ubyte * len(packedData)).from_buffer_copy(packedData)
            vrep_io.call_remote_api('simxSetStringSignal', 'force',
                                    raw_bytes, sending=True)

        robot.set_vrep_force = partial(set_vrep_force, robot)
