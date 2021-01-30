import random


class MonteCarlo:
    def __init__(self, h, k, r):
        self.h = h
        self.k = k
        self.r = r

    def next_drop_x(self):
        return random.uniform(self.h - self.r, self.h + self.r)

    def next_drop_y(self):
        return random.uniform(self.k - self.r, self.k + self.r)

    def inside_circle(self, x, y):
        inside_circle = None
        position = (x - self.h)**2 + (y - self.k)**2
        if position <= self.r**2:
            inside_circle = True
        else:
            inside_circle = False

        return inside_circle
