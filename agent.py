import random

class Agent:
    def __init__(self, x, y, world_size):
        self.x = x
        self.y = y
        self.world_size = world_size
        self.energy = 10

    def move(self, grid):
        # Kolla grannrutor för mat
        directions = {
            (0, 1): (self.x, self.y + 1),
            (1, 0): (self.x + 1, self.y),
            (0, -1): (self.x, self.y - 1),
            (-1, 0): (self.x - 1, self.y),
        }

        for (dx, dy), (nx, ny) in directions.items():
            if 0 <= nx < self.world_size and 0 <= ny < self.world_size:
                if grid[ny][nx] == "F":
                    self.x = nx
                    self.y = ny
                    self.energy -= 1
                    return  # Flytta mot mat och sluta

        # Om ingen mat i närheten, slumpmässig rörelse
        dx, dy = random.choice(list(directions.keys()))
        new_x = max(0, min(self.world_size - 1, self.x + dx))
        new_y = max(0, min(self.world_size - 1, self.y + dy))
        self.x = new_x
        self.y = new_y
        self.energy -= 1

    def eat(self, grid):
        if grid[self.y][self.x] == "F":
            self.energy += 5
            grid[self.y][self.x] = "."
