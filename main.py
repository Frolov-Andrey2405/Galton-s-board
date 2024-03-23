"""
Galton board modeling
"""

from random import randrange  # pylint: disable=C0411

import pygame as pg
import pymunk.pygame_util

pymunk.pygame_util.positive_y_is_up = False

RES = WIDTH, HEIGHT = 800, 600
FPS = 60

pg.init()
surface = pg.display.set_mode(RES)
clock = pg.time.Clock()
draw_options = pymunk.pygame_util.DrawOptions(surface)

space = pymunk.Space()
space.gravity = 0, 4000
ball_mass, ball_radius = 1, 5
segment_thickness = 4  # pylint: disable=C0103

a, b, c, d = 7, 50, 10, 25
x1, x2, x3, x4 = a, WIDTH // 2 - c, WIDTH // 2 + c, WIDTH - a
y1, y2, y3, y4, y5 = (
    b,
    HEIGHT // 4 - d,
    HEIGHT // 4,
    HEIGHT // 2 - 1.5 * b,
    HEIGHT - 4 * b,
)
L1, L2, L3, L4 = (x1, -50), (x1, y1), (x2, y2), (x2, y3)
R1, R2, R3, R4 = (x4, -50), (x4, y1), (x3, y2), (x3, y3)
B1, B2 = (0, HEIGHT), (WIDTH, HEIGHT)


def create_ball(space):  # pylint: disable=W0621
    """
    The create_ball function creates a ball object with the following properties:
        - mass = 1.0 kg
        - radius = 10 pixels (the size of the ball)
        - position is randomly generated within the boundaries of x4 and y4,
            which are defined in line 4 as 800 and 600 respectively.
            This means that each time you run this program,
            a new random position will be generated for each ball created by this function.
    """
    ball_moment = pymunk.moment_for_circle(ball_mass, 0, ball_radius)
    ball_body = pymunk.Body(ball_mass, ball_moment)
    ball_body.position = randrange(x1, x4), randrange(-y1, y1)
    ball_shape = pymunk.Circle(ball_body, ball_radius)
    ball_shape.elasticity = 0.1
    ball_shape.friction = 0.1
    space.add(ball_body, ball_shape)
    return ball_body


def create_segment(from_, to_, thickness, space, color):  # pylint: disable=W0621
    """
    The create_segment function creates a segment shape with the given parameters.
    """
    segment_shape = pymunk.Segment(space.static_body, from_, to_, thickness)
    segment_shape.color = pg.Color(color)
    space.add(segment_shape)


def create_peg(x, y, space, color):  # pylint: disable=W0621
    """
    The create_peg function creates a peg at the given x and y coordinates.
    The space argument is used to add the peg to the physics simulation,
    and color is used for visual representation of the peg.
    """
    circle_shape = pymunk.Circle(space.static_body, radius=6, offset=(x, y))
    circle_shape.color = pg.Color(color)
    circle_shape.elasticity = 0.1
    circle_shape.friction = 0.5
    space.add(circle_shape)


# Pegs
peg_y, step = y4, 40
for i in range(10):
    peg_x = -1.5 * step if i % 2 else -step
    for j in range(WIDTH // step + 2):
        create_peg(peg_x, peg_y, space, "darkslateblue")
        if i == 9:
            create_segment(
                (peg_x, peg_y + 30),
                (peg_x, HEIGHT),
                segment_thickness,
                space,
                "darkslategray",
            )
        peg_x += step
    peg_y += 0.5 * step

platforms = (L1, L2), (L2, L3), (L3, L4), (R1, R2), (R2, R3), (R3, R4)
for platform in platforms:
    create_segment(*platform, segment_thickness, space, "darkolivegreen")
create_segment(B1, B2, 20, space, "darkslategray")

# Balls
balls = [
    ((randrange(256), randrange(256), randrange(256)), create_ball(space))
    for _ in range(300)
]

while True:
    surface.fill(pg.Color("black"))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    space.step(1 / FPS)
    space.debug_draw(draw_options)
    for color, ball in balls:
        pg.draw.circle(
            surface, color, (int(ball.position[0]), int(ball.position[1])), ball_radius
        )
    pg.display.flip()
    clock.tick(FPS)
