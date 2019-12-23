# -*- coding: utf-8 -*-

class LoopIndex:

    def __init__(self, limit, jump=1, start=0):
        if jump == 0:
            raise ValueError('Incrementing by 0 does not make sense.')

        self.set_limit(limit)
        self._jump = jump
        self._start = start
        
        if not self._limit_is_reachable():
            raise ValueError('The limit will never be reached. limit = '
                             + str(limit) + ', jump = ' + str(jump)
                             + ', start = ' + str(start))

        self.reset()

        if self._jump > 0:
            self._lambda_within_bounds = lambda:\
                self._index + self._jump - 1 < self._limit
        else:
            self._lambda_within_bounds = lambda:\
                self._index + self._jump + 1 >= self._limit

    def __repr__(self):
        return 'LoopIndex(' + str(self._limit) + ', '\
                + str(self._jump) + ', ' + str(self._start) + ')'

    def get_value(self):
        return self._index

    def increment(self):
        self._index += self._jump

    def iterate(self):
        if self._first_iteration:
            self._first_iteration = False
        else:
            self.increment()
        return self.will_stay_within_bounds()

    def _limit_is_reachable(self):
        return (self._limit - self._start) * self._jump > 0

    def reset(self):
        self._first_iteration = True
        self._index = self._start

    def set_limit(self, limit):
        self._limit = limit

    def will_stay_within_bounds(self):
        return self._lambda_within_bounds()
