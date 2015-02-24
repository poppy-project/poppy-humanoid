from __future__ import division

import pypot.primitive


class LimitTorque(pypot.primitive.LoopPrimitive):
    def __init__(self, robot, freq=20, max_error=10., torque_min=20., torque_max=95.):
        pypot.primitive.LoopPrimitive.__init__(self, robot, freq)

        self._max_error = max_error
        self.torque_min = torque_min
        self.torque_max = torque_max

    def setup(self):
        self.initial_torque_limit = []

        # Using a dictionnary may be a better solution so we can easily retrieve the initial torque value.
        for m in self.robot.motors:
            self.initial_torque_limit.append(m.torque_limit)

        self.active_motors = self.robot.motors

    def update(self):
        for m in self.active_motors:
            self.adjust_torque(m)

    def adjust_torque(self, motor):
        target = motor.goal_position
        pos = motor.present_position
        dist = abs(target - pos)

        if dist > self._max_error:
            motor.torque_limit = self.torque_max
        else:
            motor.torque_limit = self.torque_min + dist / self._max_error * (self.torque_max - self.torque_min)

    def teardown(self):
        for m, i in enumerate(self.robot.motors):
            m.torque_limit = self.initial_torque_limit[i]

    @property
    def change_watched_motors(self):
        return self.active_motors

    @change_watched_motors.setter
    def change_watched_motors(self, watched_motors):
        self.active_motors = map(self.get_mockup_motor, watched_motors)

    @property
    def max_error(self):
        return self._max_error

    @max_error.setter
    def max_error(self, new_error):
        if new_error <= 0:
            raise ValueError('The max_error parameter must be strictly positive!')
        self._max_error = float(new_error)

    # TODO
    @property
    def add_watched_motors(self):
        raise NotImplementedError('TODO :)')

    @add_watched_motors.setter
    def add_watched_motors(self, added_motors):
        raise NotImplementedError('TODO :)')

    @property
    def remove_watched_motors(self):
        raise NotImplementedError('TODO :)')

    @remove_watched_motors.setter
    def remove_watched_motors(self, suppressed_motors):
        raise NotImplementedError('TODO :)')
