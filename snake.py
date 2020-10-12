from collections import deque
import random

class Snake(object):
    def __init__(self, coordinate_seq, head, color):
        self._coordinate_seq = deque(coordinate_seq)
        self._head = head
        self._grid = None
        self._color = color

    def Eat(self):
        self._coordinate_seq.appendleft(self._coordinate_seq[0])
        self._grid._objects["Food"].NewFood()

    def GetLen(self):
        return len(self._coordinate_seq)

    def MoveLeft(self):
        res = True
        new_head = ((self._head[0] - 1) % self._grid._columns, self._head[1])
        self._coordinate_seq.append(new_head)
        self._head = new_head
        if self._grid._grid[self._head[1]][self._head[0]] == self._color:
            res = False
        self._grid._Put([self._coordinate_seq.popleft()], self._grid._color)
        self._grid._Put(self._coordinate_seq, self._color)
        if self._grid._objects["Food"].IsEaten():
            self.Eat()
        return res

    def MoveRight(self):
        res = True
        new_head = ((self._head[0] + 1) % self._grid._columns, self._head[1])
        self._coordinate_seq.append(new_head)
        self._head = new_head
        if self._grid._grid[self._head[1]][self._head[0]] == self._color:
            res = False
        self._grid._Put([self._coordinate_seq.popleft()], self._grid._color)
        self._grid._Put(self._coordinate_seq, self._color)
        if self._grid._objects["Food"].IsEaten():
            self.Eat()
        return res

    def MoveUp(self):
        res = True
        new_head = (self._head[0], (self._head[1] - 1) % self._grid._rows)
        self._coordinate_seq.append(new_head)
        self._head = new_head
        if self._grid._grid[self._head[1]][self._head[0]] == self._color:
            res = False
        self._grid._Put([self._coordinate_seq.popleft()], self._grid._color)
        self._grid._Put(self._coordinate_seq, self._color)
        if self._grid._objects["Food"].IsEaten():
            self.Eat()
        return res

    def MoveDown(self):
        res = True
        new_head = (self._head[0], (self._head[1] + 1) % self._grid._rows)
        self._coordinate_seq.append(new_head)
        self._head = new_head
        if self._grid._grid[self._head[1]][self._head[0]] == self._color:
            res = False
        self._grid._Put([self._coordinate_seq.popleft()], self._grid._color)
        self._grid._Put(self._coordinate_seq, self._color)
        if self._grid._objects["Food"].IsEaten():
            self.Eat()
        return res

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
 
