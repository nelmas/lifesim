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

def print_grid(grid, agent):
    for y in range(len(grid)):
        row = ""
        for x in range(len(grid[y])):
            if agent.x == x and agent.y == y:
                row += "A "  # Agenten
            else:
                row += grid[y][x] + " "
        print(row)
    print()  # Tom rad för tydlighet

def main():
    grid = create_grid()
    spawn_food(grid, count=10)
    agent = Agent(10, 10, WORLD_SIZE)

    for _ in range(20):
        if agent.energy <= 0:
            print("Agent has run out of energy and cannot move.")
            break
        agent.move(grid)
        agent.eat(grid)
        print_grid(grid, agent)
        print(f"Agent at ({agent.x}, {agent.y}), energy: {agent.energy}")

if __name__ == "__main__":
    main()