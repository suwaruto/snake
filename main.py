import pygame
from collections import deque
import random

global running 

class Grid(object):
    def __init__(self, rows, columns, color, grid = None):
        self._rows = rows
        self._columns = columns
        self._color = color
        if not (grid is None):
            self._grid = grid[:][:]
        else: 
            self._grid = []
            for y in range(self._rows):
                row = []
                for x in range(self._columns):
                    row += [self._color]
                self._grid += [row]
        self._objects = dict()

    def _Put(self, coordinate_seq, color):
        for item in coordinate_seq:
           self._grid[item[1]][item[0]] = color 

    def Register(self, key, obj):
        self._objects[key] = obj
        obj._grid = self
        self._Put(obj._coordinate_seq, obj._color)

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
    def __init__(self, coordinate_seq, head, color):
        self._coordinate_seq = deque(coordinate_seq)
        self._head = head
        self._grid = None
        self._color = color

    def Eat(self):
        self._coordinate_seq.appendleft(self._coordinate_seq[0])
        self._grid._objects["Food"].NewFood()

    def Bump(self):
        global running 
        running = False

    def GetLen(self):
        return len(self._coordinate_seq)

    def MoveLeft(self):
        new_head = ((self._head[0] - 1) % self._grid._columns, self._head[1])
        self._coordinate_seq.append(new_head)
        self._head = new_head
        if self._grid._grid[self._head[1]][self._head[0]] == self._color:
            self.Bump()
        self._grid._Put([self._coordinate_seq.popleft()], self._grid._color)
        self._grid._Put(self._coordinate_seq, self._color)
        if self._grid._objects["Food"].IsEaten():
            self.Eat()

    def MoveRight(self):
        new_head = ((self._head[0] + 1) % self._grid._columns, self._head[1])
        self._coordinate_seq.append(new_head)
        self._head = new_head
        if self._grid._grid[self._head[1]][self._head[0]] == self._color:
            self.Bump()
        self._grid._Put([self._coordinate_seq.popleft()], self._grid._color)
        self._grid._Put(self._coordinate_seq, self._color)
        if self._grid._objects["Food"].IsEaten():
            self.Eat()

    def MoveUp(self):
        new_head = (self._head[0], (self._head[1] - 1) % self._grid._rows)
        self._coordinate_seq.append(new_head)
        self._head = new_head
        if self._grid._grid[self._head[1]][self._head[0]] == self._color:
            self.Bump()
        self._grid._Put([self._coordinate_seq.popleft()], self._grid._color)
        self._grid._Put(self._coordinate_seq, self._color)
        if self._grid._objects["Food"].IsEaten():
            self.Eat()

    def MoveDown(self):
        new_head = (self._head[0], (self._head[1] + 1) % self._grid._rows)
        self._coordinate_seq.append(new_head)
        self._head = new_head
        if self._grid._grid[self._head[1]][self._head[0]] == self._color:
            self.Bump()
        self._grid._Put([self._coordinate_seq.popleft()], self._grid._color)
        self._grid._Put(self._coordinate_seq, self._color)
        if self._grid._objects["Food"].IsEaten():
            self.Eat()

class Food(object):
    def __init__(self, coordinate, color):
        self._grid = None
        self._color = color
        self._coordinate_seq = [coordinate]

    def IsEaten(self):
        if self._grid._grid[self._coordinate_seq[0][1]] \
            [self._coordinate_seq[0][0]] != self._color:
            return True
        else:
            return False

    def NewFood(self):
        x = random.randint(0, self._grid._columns - 1)
        y = random.randint(0, self._grid._rows - 1)
        while self._grid._grid[y][x] != self._grid._color:
            x = random.randint(0, self._grid._columns - 1)
            y = random.randint(0, self._grid._rows - 1)
        self._coordinate_seq = [(x, y)]
        self._grid._Put(self._coordinate_seq, self._color)
                
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

    global running
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
    print("Game over!")
    print("You scored: {0}".format(snake.GetLen()))

if __name__ == "__main__": main()
