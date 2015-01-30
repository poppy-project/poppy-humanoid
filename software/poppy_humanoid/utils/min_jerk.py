
from __future__ import division
import numpy as np

import collections

import pypot.primitive
import copy
# import kinematics
# import time
# import pypot.utils.pypot_time as time


class MJTraj():

    def __init__(self, initial, final, duration, init_vel=0.0, init_acc=0.0, final_vel=0.0, final_acc=0.0):
        self.a0 = initial
        self.a1 = init_vel
        self.a2 = init_acc / 2.0
        self.d5 = duration ** 5
        self.d4 = duration ** 4
        self.d3 = duration ** 3
        self.d2 = duration ** 2
        self.duration = duration
        self.durations = [0, duration]
        self.initial = initial
        self.final = final
        self.init_vel = init_vel
        self.final_vel = final_vel
        self.init_acc = init_acc
        self.final_acc = final_acc

        self.finals = [final]

        self.A = np.array([[self.d3, self.d4, self.d5], [
                          3 * self.d2, 4 * self.d3, 5 * self.d4], [6 * duration, 12 * self.d2, 20 * self.d3]])
        self.B = np.array([final - self.a0 - (self.a1 * duration) - (self.a2 * self.d2),
                           final_vel - self.a1 - (2 * self.a2 * duration), final_acc - (2 * self.a2)])

        self.X = []
        self.compute()

        self.other_gen = None

        self._mylambda = lambda x: self.a0 + self.a1 * x + self.a2 * x ** 2 + \
            self.X[0] * x ** 3 + self.X[1] * x ** 4 + self.X[2] * x ** 5

        self._generators = [self._mylambda]

    def compute(self):
        self.X = np.linalg.solve(self.A, self.B)

    def getValue(self, t):
        # FIXME: check time range
        # self.a0 + self.a1 * t + self.a2 * t ** 2 + self.X[0] * t ** 3 + self.X[1] * t ** 4 + self.X[2] * t ** 5
        return self._mygenerator[- 1](t)
        # return self._generator[ - 1](t)

    def domain(self, x):

        if not isinstance(x, collections.Iterable):
            x = np.array([x])

        domain = []
        for d in xrange(len(self.durations) - 1):
            d1 = []

            for xi in x:

                d1.append(
                    (xi >= self.durations[d]) & (xi < self.durations[d + 1]))

            domain.append(np.array(d1))
        return np.array(domain)

    def test_domain(self, x):
        return [((np.array(x) >= self.durations[i])) for i in xrange(len(self.durations) - 1)]

    def fix_input(self, x):
        if not isinstance(x, collections.Iterable):
            return np.array([0, x])
        else:
            return x

    def getGen(self):

        return lambda x: np.piecewise(x, self.domain(x), [self._generators[j] for j in xrange(len(self._generators))] + [self.finals[- 1]])

    def __add__(self, othertraj):
        # print "ADD ", self.initial, self.final, othertraj.initial,
        # othertraj.final
        if othertraj.initial == self.final and othertraj.init_vel == self.init_vel and othertraj.init_acc == self.final_acc:
            self.final = othertraj.final
            self.final_vel = othertraj.final_vel
            self.final_acc = othertraj.final_acc
            self.other_gen = othertraj.getGen()

            tmpduration = self.duration
            # self.duration = self.duration + othertraj.duration

            # self._mygenerator(x) if filter(lambda y: y < self.duration, x) else self.other_gen(x)
            # self._mygenerator = lambda x: np.piecewise(np.array(x), [np.array(x) < self.duration, np.array(x) >= self.duration ], [self._mygenerator(x), self.other_gen(x)])
            l = len(self._generators) - 1
            l1 = len(self.durations) - 1
            l2 = len(othertraj.durations) - 1
            # self.durations.append(self.durations[l1] + othertraj.durations[l2])
            # self.durations.append(othertraj.durations[l2])
            # print "DEBUG ", len(self.durations), self.durations[l]

            # tmpgen = lambda x: self.other_gen(x - self.durations[l])
            # self._mygenerator.append(lambda x: np.piecewise(np.array(x), [np.array(x) < self.durations[l], np.array(x) >= self.durations[l]], [self._mygenerator[l], tmpgen]))

            tmpA = copy.deepcopy(self)
            tmpA.durations.append(self.durations[l1] + othertraj.durations[l2])
            tmpA.finals.append(othertraj.finals[- 1])

            tmpA._generators.append(
                lambda x: othertraj._mylambda(x - self.durations[- 1]))

            return tmpA

        else:
            print "Trajectories are not matching"
            return - 1


class GotoMJ(pypot.primitive.LoopPrimitive):

    def __init__(self, robot, motors, duration, refresh_freq=50):
        pypot.primitive.LoopPrimitive.__init__(self, robot, refresh_freq)
        self.add(motors, duration)

    def setup(self):
        self.init_traj()

    def update(self):
        if self.elapsed_time <= self.duration:
            for motorname, mj in self.trajs.iteritems():
                getattr(self.robot, motorname).goal_position = mj(
                    self.elapsed_time)
        else:
            del self.trajs
            self.stop(wait=False)

    def add(self, motors, duration):
        self.motors = motors
        self.duration = duration
        self.trajs = {}
        # self.mjstarted = False

    def init_traj(self):
        self.trajs = {m: MJTraj(getattr(self.robot, m).present_position,
                      g, self.duration).getGen()
                      for m, g in self.motors.iteritems()}
        # self.mjstarted = True


class goto_mjtraj(pypot.primitive.LoopPrimitive):

    def __init__(self, robot, motors_traj, refresh_freq=50):
        pypot.primitive.LoopPrimitive.__init__(self, robot, refresh_freq)
        self.add(motors_traj)

    def update(self):
        if not self.mjstarted:
            self.init_traj()
        else:
            if np.array(self.elapsed_time <= np.array(self.durations)).all():
                # if abs(self.pos - self.mjtraj.final) > 0.001:
                for motorname, mj in self.motors_traj.iteritems():
                    getattr(self.robot, motorname).goal_position = mj(
                        self.elapsed_time)
            else:
                # FIXME
                self.stop()

    def add(self, motors):
        self.motors_traj = {m: mj.getGen() for m, mj in motors.iteritems()}
        self.durations = [d.durations[- 1] for d in motors.values()]
        self.mjstarted = False

    def init_traj(self):
        self.mjstarted = True



if __name__ == '__main__':

    ts = np.arange(0, 2.01, .01)

    m1 = MJTraj(0, 10, 0.5)
    m2 = MJTraj(10, 15, 0.5)
    m3 = MJTraj(15, 20, 0.5)
    m4 = m1 + m2 + m3 + MJTraj(20, 25, 0.5)

    # print m4.initial, m4.final, m4.duration,  m4.durations

    m1t = m1.getGen()
    m2t = m2.getGen()
    m3t = m3.getGen()
    m4t = m4.getGen()

    # print m1t(ts)
    # print m2t(ts)
    # print m3t(ts)
    # print len(m4._generators)

    m1 = MJTraj(0, 10, 0.5)
    m2 = MJTraj(10, 15, 0.5)
    m4 = m1 + m2 + m3
    # m4 =  MJTraj(0, 10, 2.0)
    m4t = m4.getGen()

    t = 0.0
    ta = []
    print
    for i in range(20):
        # print m4t(np.ones(10) * t)
        ta.append(t)
        print m4.domain(t)
        # print m4._generators
        # print m4.test_domain(t)
        print t, m4t(t)

        t += 0.10

    ta = np.array(ta)
    # print m4.domain(1.9)
    print

    print ta
    print m4t(ta)
    print m4.domain(ta)
    print m4t(np.asarray([0.4, 0.9, 1.4, 1.9, 2.4]))

    print m4.duration
    # print m4.test_domain(ta)
    # print m4.domain(ta)

    # print m4t(ts)

    # stop

    # plt.plot(ts, m1t(ts))
    # plt.plot(ts, m2t(ts))
    # plt.plot(ts, m4t(ts))

    # plt.plot(ts, mmm(ts))
    # m = simpyMJ(0.0, 10.0, 0.5, final_vel = 5.0)
    # m = npMJ(0.0, 10.0, 0.5, final_vel = 5.0)
    # plt.plot(ts, m(ts))
    # plt.plot(kinematics.deriv(jerk))
    # plt.plot(jerk)
    # plt.plot(test)
    # plt.show()
