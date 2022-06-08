import random

import pgzrun
from pgzero.clock import clock
from pgzhelper import *


class Enemy(Actor):
    def __init__(self, image: Union[str, pygame.Surface], pos=POS_TOPLEFT, anchor=ANCHOR_CENTER, max_x=100, max_y=100, **kwargs):
        super().__init__(image, pos=POS_TOPLEFT, anchor=ANCHOR_CENTER, **kwargs)
        spawn = random.randint(0, 3)
        self.x = random.randint(0, max_x)
        self.y = random.randint(0, max_y)
        if spawn == 0:
            self.x = 0
        elif spawn == 1:
            self.x = max_x
        elif spawn == 2:
            self.y = 0
        else:
            self.y = max_y
        self.speed = 1

        run_images = ['skeleton-move_0_small', 'skeleton-move_1_small', 'skeleton-move_2_small',
                      'skeleton-move_3_small',  'skeleton-move_4_small', 'skeleton-move_5_small', 'skeleton-move_6_small',
                      'skeleton-move_7_small',   'skeleton-move_8_small', 'skeleton-move_9_small', 'skeleton-move_10_small',
                      'skeleton-move_11_small',   'skeleton-move_12_small', 'skeleton-move_13_small', 'skeleton-move_14_small',
                      'skeleton-move_15_small', 'skeleton-move_16_small']
        self.images = run_images
        clock.schedule_interval(self.speedup, 2)

    def speedup(self):
        self.speed += 1

    def move(self, x, y):
        self.next_image()
        self.point_towardsXY(x, y)
        self.move_forward(self.speed)
