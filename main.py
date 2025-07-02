WORLD_SIZE = 20

def create_grid():
    return [["." for _ in range(WORLD_SIZE)] for _ in range(WORLD_SIZE)]

def spawn_food(grid, count=10):
    for _ in range(count):
        x = random.randint(0, WORLD_SIZE - 1)
        y = random.randint(0, WORLD_SIZE - 1)
        grid[y][x] = "F"

