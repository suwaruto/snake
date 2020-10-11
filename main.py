import pygame
import astar
from collections import deque

class Grid(object):
    def __init__(self, rows, columns, arr = None):
        self._rows = rows
        self._columns = columns
        if not (arr is None):
            self._grid = arr[:][:]
        else: 
            self._grid = []
            for y in range(self._rows):
                row = []
                for x in range(self._columns):
                    row += [(0, 0, 0)]
                self._grid += [row]

    def _Put(self, coordinate_seq, color):
        for item in coordinate_seq:
           self._grid[item[1]][item[0]] = color 

    def Draw(self, surface):
        width = surface.get_width()  
        height = surface.get_height()
        step_x = width // self._columns
        step_y = height // self._rows
        for y in range(self._rows):
            for x in range(self._columns):
                pygame.draw.rect(surface, self._grid[y][x],
                    pygame.Rect(x * step_x, y * step_y, step_x, step_y))

class Snake(object):
    def __init__(self, coordinate_seq, head, grid):
        self._deque = deque(coordinate_seq)
        self._head = head
        self._grid = grid
        self._grid._Put(self._deque, (0, 0, 255))

    def MoveLeft(self):
        new_head = (self._head[0] - 1, self._head[1])
        self._deque.append(new_head)
        self._head = new_head
        self._grid._Put([self._deque.popleft()], (0, 0, 0))
        self._grid._Put(self._deque, (0, 0, 255))

    def MoveRight(self):
        new_head = (self._head[0] + 1, self._head[1])
        self._deque.append(new_head)
        self._head = new_head
        self._grid._Put([self._deque.popleft()], (0, 0, 0))
        self._grid._Put(self._deque, (0, 0, 255))

    def MoveUp(self):
        new_head = (self._head[0], self._head[1] - 1)
        self._deque.append(new_head)
        self._head = new_head
        self._grid._Put([self._deque.popleft()], (0, 0, 0))
        self._grid._Put(self._deque, (0, 0, 255))


    def MoveDown(self):
        new_head = (self._head[0], self._head[1] + 1)
        self._deque.append(new_head)
        self._head = new_head
        self._grid._Put([self._deque.popleft()], (0, 0, 0))
        self._grid._Put(self._deque, (0, 0, 255))


class Food(object):
    def __init__(self, grid):
        pass

def main():
    width = 300
    height = 300
    rows = 20
    columns = 20
    grid = Grid(rows, columns)
    snake = Snake([(10, 10), (10, 11), (10, 12)], (10, 12), grid)
    window = pygame.display.set_mode((width, height))
    window.fill((255, 255, 255))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.MoveLeft()
                elif event.key == pygame.K_RIGHT:
                    snake.MoveRight()
                elif event.key == pygame.K_UP:
                    snake.MoveUp()
                elif event.key == pygame.K_DOWN:
                    snake.MoveDown()
        grid.Draw(window)
        pygame.display.update()

if __name__ == "__main__": main()
