import turtle as t

SEG_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_new()
        self.head = self.segments[0]
        self.last = len(self.segments)-1

    def create_new(self):
        for position in SEG_POSITIONS:
            new_segment = t.Turtle(shape='square')
            new_segment.color('black')
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def detect_game_over(self):
        if abs(self.head.xcor()) > 290 or abs(self.head.ycor()) > 290:
            return False
        else:
            return True

    def add_tail(self):
        new_segment = t.Turtle(shape='square')
        new_segment.color('black')
        new_segment.penup()
        new_segment.goto(self.segments[-1].position())
        self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def turn_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def turn_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def turn_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def turn_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
