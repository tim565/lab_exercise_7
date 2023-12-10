import enum


class Direction(enum.Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


class Turtle:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = Direction.NORTH

    def turn_right(self):
        self.direction = Direction((self.direction.value + 1) % 4)

    def turn_left(self):
        self.direction = Direction((self.direction.value - 1) % 4)

    def move_forward(self):
        if self.direction == Direction.NORTH:
            self.y += 1
        elif self.direction == Direction.EAST:
            self.x += 1
        elif self.direction == Direction.SOUTH:
            self.y -= 1
        elif self.direction == Direction.WEST:
            self.x -= 1

    def __str__(self):
        direction_names = {
            Direction.NORTH: 'North',
            Direction.EAST: 'East',
            Direction.SOUTH: 'South',
            Direction.WEST: 'West',
        }
        return f"Turtle at ({self.x}, {self.y}) facing {direction_names[self.direction]}"


# Test the turtle

turtle = Turtle(0, 0)

print(turtle)  # "Turtle at (0, 0) facing North"

turtle.move_forward()
print(turtle)  # "Turtle at (0, 1) facing North"

turtle.turn_right()
turtle.move_forward()
print(turtle)  # "Turtle at (1, 1) facing East"

turtle.turn_right()
turtle.move_forward()
print(turtle)  # "Turtle at (1, 0) facing South"

turtle.turn_right()
turtle.move_forward()
print(turtle)  # "Turtle at (0, 0) facing West"