import random

class Agent:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.energy = 10

    def move(self):
        dx, dy = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])
        self.x = max(0, min(WORLD_SIZE - 1, self.x + dx))
        self.y = max(0, min(WORLD_SIZE - 1, self.y + dy))
        self.energy -= 1