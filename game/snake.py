from box import Box
from snake_exceptions import SnakeException


class Snake:
    def __init__(self, box, color, direction):
        box.color = color
        self.body = [box]
        self.color = color
        self.direction = direction
        self.tail = None

    def self_collide_test(self):
        head = self.body[0]
        for box_index in range(1, len(self.body)):
            if head.rectangle.colliderect(self.body[box_index].rectangle):
                raise SnakeException("Snake self collision")

    def draw(self, screen):
        for box in self.body:
            box.draw(screen)

    def move(self):
        x_position = self.body[0].x_position
        y_position = self.body[0].y_position
        size = self.body[0].size
        color = self.body[0].color
        if self.direction == 'left':
            x_position -= size
        elif self.direction == 'right':
            x_position += size
        elif self.direction == 'up':
            y_position -= size
        elif self.direction == 'down':
            y_position += size
        self.body.insert(0, Box(x_position, y_position, size, color))
        self.tail = self.body.pop()
        self.self_collide_test()

    def change_direction(self, direction):
        self.direction = direction

    def eating(self):
        self.body.append(self.tail)