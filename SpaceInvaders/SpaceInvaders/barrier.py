import pygame as pg
from pygame.sprite import Sprite, Group

class Barrier(Sprite):
    color = 0, 0, 255
    black = 0, 0, 0

    def __init__(self, game, rect):
        super().__init__()
        self.screen = game.screen
        self.rect = rect
        self.settings = game.settings

        # self.settings = game.settings
        # self.image = pg.image.load('images/alien0.bmp')
        # self.rect = self.image.get_rect()
        # self.rect.y = self.rect.height
        # self.x = float(self.rect.x)
        
    def hit(self):
        self.rect.inflate_ip(-5, -3)


    def update(self): 
        self.draw()
    def draw(self): 
        pg.draw.rect(self.screen, Barrier.color, self.rect, 0, 20)
        # pg.draw.circle(self.screen, self.black, (self.rect.centerx, self.rect.bottom), self.rect.width/6)


class Barriers:
    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        self.create_barriers()
       

        self.ship_lasers = game.ship_lasers.lasers
        self.aliens_lasers = game.alien_lasers

    def create_barriers(self): 
        self.barrier_health = 4    
        width = self.settings.screen_width / 10
        height = 2.0 * width / 4.0
        top = self.settings.screen_height - 2.1 * height
        rects = [pg.Rect(x * 2 * width + 1.5 * width, top, width, height) for x in range(4)]   # SP w  3w  5w  7w  SP
        self.barriers = [Barrier(game=self.game, rect=rects[i]) for i in range(4)]


    def check_collisions(self):
        
        collisions = pg.sprite.groupcollide(self.barriers,self.aliens_lasers.lasers, False, True )
        if collisions:
            for barrier in self.barriers:
                barrier.hit()

        collisions = pg.sprite.groupcollide(self.barriers, self.ship_lasers, False, True)
        if collisions:
            for barrier in self.barriers:
                barrier.hit()
                        

    # def hit(self):
    #     print( "Barrier was Hit!")

    
    def reset(self):
        self.create_barriers()

    def update(self):
        for barrier in self.barriers:
            barrier.update()
        self.check_collisions()

    def draw(self):
        for barrier in self.barriers: barrier.draw()

