# -*- coding: utf-8 -*-

class LoopIndex:

    def __init__(self, limit, step=1, start=0):
        if step == 0:
            raise ValueError("Incrementing by 0 does not make sense.")

        self._step = step
        self._start = start
        self.set_limit(limit)

        self.reset()
        self._set_lambda_check_bounds()

    def __repr__(self):
        return "LoopIndex(" + str(self._limit) + ", "\
            + str(self._step) + ", " + str(self._start) + ")"

    def check_bounds(self):
        return self._lambda_check_bounds()

    def _check_unreachable_limit_error(self, limit):
        if not self._limit_is_reachable(limit):
            raise ValueError("The limit will never be reached: limit = "
                             + str(limit) + ", step = " + str(self._step)
                             + ", start = " + str(self._start) + ".")

    def get_value(self):
        return self._index

    def increment(self):
        self._index += self._step

    def iterate(self):
        if self._first_iteration:
            self._first_iteration = False
        else:
            self.increment()
        return self.check_bounds()

    def _limit_is_reachable(self, limit):
        return (limit - self._start) * self._step >= 0

    def reset(self):
        self._first_iteration = True
        self._index = self._start

    def _set_lambda_check_bounds(self):
        if self._step > 0:
            self._lambda_check_bounds = lambda: self._index < self._limit
        else:
            self._lambda_check_bounds = lambda: self._index >= self._limit

    def set_limit(self, limit):
        self._check_unreachable_limit_error(limit)
        self._limit = limit
