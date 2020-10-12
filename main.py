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
    grid.Register("Snake", snake)
    grid.Register("Food", Food((3, 3), (255, 0, 0)))
    window = pygame.display.set_mode((width, height))
    window.fill((255, 255, 255))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    running = snake.MoveLeft()
                elif event.key == pygame.K_RIGHT:
                    running = snake.MoveRight()
                elif event.key == pygame.K_UP:
                    running = snake.MoveUp()
                elif event.key == pygame.K_DOWN:
                    running = snake.MoveDown()
        grid.Draw(window)
        pygame.display.update()
    print("Game over!")
    print("You scored: {0}".format(snake.GetLen()))

if __name__ == "__main__": main()
