#Directions sorted in clockwise order

NORTH = 1
EAST = 2
SOUTH = 3
WEST = 4

class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.coordinates = (x, y)
        self.bearing = bearing

    def turn_right(self):
        self.bearing += 1
        if self.bearing == 5:
            self.bearing = 1

    def turn_left(self):
        self.bearing -= 1
        if self.bearing == 0:
            self.bearing = 4

    def simulate(self, moves):
        for move in moves:
            if move == 'R':
                self.turn_right()
            elif move == 'L':
                self.turn_left()
            elif move == 'A':
                self.advance()

    def advance(self):
        directions = {NORTH: (0, 1), SOUTH: (0, -1), EAST: (1, 0), WEST: (-1, 0)}
        self.coordinates = (self.coordinates[0] + directions[self.bearing][0],
                            self.coordinates[1] + directions[self.bearing][1])
