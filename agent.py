import random

class Agent:
    def __init__(self, x, y, world_size):
        self.x = x
        self.y = y
        self.world_size = world_size
        self.energy = 10

    def move(self):
        dx, dy = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])
        self.x = max(0, min(self.world_size - 1, self.x + dx))
        self.y = max(0, min(self.world_size - 1, self.y + dy))
        self.energy -= 1

    def eat(self, grid):
        if grid[self.y][self.x] == "F":
            self.energy += 5
            grid[self.y][self.x] = "."
