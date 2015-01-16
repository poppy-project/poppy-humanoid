import pypot.primitive


class LimitTorque(pypot.primitive.LoopPrimitive):
    def __init__(self, poppy_humanoid, freq=20, max_error=10, torque_min=20, torque_max=95):
        pypot.primitive.LoopPrimitive.__init__(self, poppy_humanoid, freq)

        self.poppy_humanoid = poppy_humanoid
        self._max_error = max_error
        self.torque_min = torque_min
        self.torque_max = torque_max

    def update(self):
        for m in self.poppy_humanoid.motors:
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
        for m in self.poppy_humanoid.motors:
            m.torque_limit = self.torque_max

    @property
    def max_error(self):
        return self._max_error

    @max_error.setter
    def max_error(self, new_error):
        if new_error <= 0:
            raise ValueError('The max_error parameter must be strictly positive!')
        self._max_error = new_error
