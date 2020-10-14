import pygame
from grid import *
from snake import *

global running 
               
def main():
    width = 300
    height = 300
    rows = 20
    columns = 20
    grid = Grid(rows, columns, (255, 255, 255))
    snake = Snake([(10, 10)], (10, 10), (0, 0, 255))
    snake.SetDirection(1)
    grid.Register("Snake", snake)
    grid.Register("Food", Food((3, 3), (255, 0, 0)))
    window = pygame.display.set_mode((width, height))
    window.fill((255, 255, 255))

    running = True
    while running:
        pygame.time.wait(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.SetDirection(0)
                elif event.key == pygame.K_RIGHT:
                    snake.SetDirection(1)
                elif event.key == pygame.K_UP:
                    snake.SetDirection(2)
                elif event.key == pygame.K_DOWN:
                    snake.SetDirection(3)
        running = snake.Move()
        grid.Draw(window)
        pygame.display.update()
    print("Game over!")
    print("You scored: {0}".format(snake.GetLen()))

if __name__ == "__main__": main()
