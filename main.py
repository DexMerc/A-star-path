import pygame
import pathfinder

s_width = 400
s_height = 500
n = 10
m = 10


def game(maze, sol):
    pygame.font.init()

    screen = pygame.display.set_mode((s_height, s_width))
    pygame.display.set_caption("A* pathfinding")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill((169, 169, 169))
        for i in range(len(maze)):
            for j in range(len(maze[i])):
                if (i, j) in sol:
                    draw_rect(screen, maze[i][j], i, j, (0, 255, 0))
                else:
                    draw_rect(screen, maze[i][j], i, j, (0, 0, 0))
        pygame.display.update()


def draw_rect(screen, text, x, y, color):
    pygame.draw.rect(screen, (255, 255, 255), [s_height / n * y + 10, s_width / m * x + 10, 20, 20])
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render(str(text), 1, color)
    screen.blit(label, (s_height / n * y + 15, s_width / m * x + 10))


def main():
    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    grid_sol = pathfinder.a_star(maze, (0, 2), (len(maze) - 1, len(maze[0]) - 1))
    print(grid_sol)
    game(maze, grid_sol)


if __name__ == '__main__':
    main()
