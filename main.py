import pygame
import numpy as np
import random
import pathfinder

s_width = 400
s_height = 500
n = 5
m = 6

def game(maze, sol):
    pygame.font.init()

    screen = pygame.display.set_mode((s_height, s_width))

    pygame.display.set_caption("A* pathfinding")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                continue
        screen.fill((169, 169, 169))
        for i in range(len(maze)):
            for j in range(len(maze[i])):
                draw_rect(screen, maze[i][j], i, j)
        pygame.display.update()


def draw_rect(screen, text, x, y):
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render(str(text), 1, (255,255,255))
    screen.blit(label, (s_width/m*x, s_height/n*y))


def create_maze():
    arr = np.zeros([n, m])

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] = int(random.random() * 10)

    return arr


def main():
    maze = create_maze()
    grid_sol = pathfinder.a_star(maze, (0, 0), (n-1, m-1))
    game(maze, grid_sol)


if __name__ == '__main__':
    main()
