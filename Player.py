import pgzrun

from pgzhelper import *


class Player(Actor):
    def __init__(self, image: Union[str, pygame.Surface], pos=POS_TOPLEFT, anchor=ANCHOR_CENTER, **kwargs):
        super().__init__(image, pos=POS_TOPLEFT, anchor=ANCHOR_CENTER, **kwargs)
        self.x = 100
        self.y = 100
        self.dir_x = 0
        self.dir_y = 0
        self.speed = 5
        self.HP = 10

        run_images = ['skeleton-move_0_small', 'skeleton-move_1_small', 'skeleton-move_2_small',
                      'skeleton-move_3_small',
                      'skeleton-move_4_small', 'skeleton-move_5_small', 'skeleton-move_6_small',
                      'skeleton-move_7_small',
                      'skeleton-move_8_small', 'skeleton-move_9_small', 'skeleton-move_10_small',
                      'skeleton-move_11_small',
                      'skeleton-move_12_small', 'skeleton-move_13_small', 'skeleton-move_14_small',
                      'skeleton-move_15_small', 'skeleton-move_16_small']
        self.images = run_images

    def move(self, surface):
        self.next_image()
        w, h = surface.get_size()
        self.x += self.dir_x * self.speed
        if self.x < 0:
            self.x = 0
        if self.x > w:
            self.x = w
        self.y += self.dir_y * self.speed
        if self.y < 0:
            self.y = 0
        if self.y > h:
            self.y = h

    def draw(self, screen):
        super().draw()
        screen.draw.text(str(self.HP), pos=(0, 0))
