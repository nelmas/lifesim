import random
from agent import Agent

WORLD_SIZE = 20

def create_grid():
    return [["." for _ in range(WORLD_SIZE)] for _ in range(WORLD_SIZE)]

def spawn_food(grid, count=10):
    for _ in range(count):
        x = random.randint(0, WORLD_SIZE - 1)
        y = random.randint(0, WORLD_SIZE - 1)
        grid[y][x] = "F"

def main():
    grid = create_grid()
    spawn_food(grid, count=10)
    agent = Agent(10, 10)

    for _ in range(20):
        agent.move()
        agent.eat(grid)
        print(f"Agent at ({agent.x}, {agent.y}), energy: {agent.energy}")

if __name__ == "__main__":
    main()