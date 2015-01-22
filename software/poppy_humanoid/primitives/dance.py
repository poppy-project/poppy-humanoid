from __future__ import division

import numpy

import pypot.primitive


def sinus(ampl, t, freq=0.5, phase=0, offset=0):
    pi = numpy.pi
    return ampl * numpy.sin(freq * 2.0 * pi * t + phase * pi / 180.0) + offset


class SimpleBodyBeatMotion(pypot.primitive.LoopPrimitive):
    '''
    Simple primitive to make Poppy shake its booty following a given beat rate in bpm.

    '''
    def __init__(self, robot, bpm, motion_amplitude=10):
        pypot.primitive.LoopPrimitive.__init__(self, robot, 50)

        self._bpm = bpm
        self.amplitude = motion_amplitude
        self.frequency = bpm / 60.0
        self.pi = numpy.pi

    def setup(self):
        for m in self.robot.motors:
            m.moving_speed = 50.0

    def update(self):
        t = self.elapsed_time
        amp = self._amplitude
        freq = self.frequency

        self.robot.head_y.goal_position = sinus(amp / 2.0, t, freq)
        self.robot.head_z.goal_position = sinus(amp / 2.0, t, freq / 2.0)

        self.robot.bust_x.goal_position = sinus(amp / 6.0, t, freq / 2.0) + sinus(amp / 6.0, t, freq / 4.0)
        self.robot.abs_x.goal_position = - sinus(amp / 8.0, t, freq / 4.0) + sinus(amp / 6.0, t, freq / 4.0)

        self.robot.l_shoulder_y.goal_position = sinus(amp / 3.0, t, freq / 2.0)
        self.robot.r_shoulder_y.goal_position = - sinus(amp / 3.0, t, freq / 2.0)

        self.robot.r_elbow_y.goal_position = sinus(amp / 2.0, t, freq, offset=-20)
        self.robot.l_elbow_y.goal_position = sinus(amp / 2.0, t, freq / 2.0, offset=-20)

    def teardown(self):
        self.robot.power_up()

    @property
    def bpm(self):
        return self._bpm

    @bpm.setter
    def bpm(self, new_bpm):
        '''
        Permits to change the beat rate while the motion is performing
        '''
        self._bpm = new_bpm
        self.frequency = self._bpm / 60.0

    @property
    def amplitude(self):
        return self._amplitude

    @amplitude.setter
    def amplitude(self, new_amp):
        self._amplitude = new_amp
