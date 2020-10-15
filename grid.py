import pygame

class Grid(object):
    def __init__(self, rows, columns, color, window, grid = None):
        self._rows = rows
        self._columns = columns
        self._color = color
        self._window = window
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

    def Draw(self, surface = None):
        if surface == None: surface = self._window
        width = surface.get_width()  
        height = surface.get_height()
        step_x = width // self._columns
        step_y = height // self._rows
        for y in range(self._rows):
            for x in range(self._columns):
                pygame.draw.rect(surface, self._grid[y][x],
                    pygame.Rect(x * step_x, y * step_y, step_x, step_y))
