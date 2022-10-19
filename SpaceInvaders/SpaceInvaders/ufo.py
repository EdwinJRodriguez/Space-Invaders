from ast import Or
from email.headerregistry import HeaderRegistry
from random import randint
import pygame as pg
from pygame.sprite import Sprite, Group
from laser import Lasers
from timer import Timer
import random
from settings import Settings



class Ufo(pg.sprite.Sprite):
    
    def __init__(self, side, screen_width):
        super().__init__()
        ##self.image = pg.image.load('images/ufo__01.png').convert_alpha()
        self.image = pg.image.load('images/ufo__00.png')
       ## self.rect = self.image.get_rect()
        if side == 'right':
            x =screen_width + 1200
            self.speed_factor = -3
        else: 
            x= -50
            self.speed_factor =3

        self.rect = self.image.get_rect(topleft = (x,-30) )

        ##self.timer_normal = Ufo.ufo_timers[type]              
        ##self.timer_explosion = Timer(image_list=Ufo.ufo_explosion_images, is_loop=False)  
        ##self.timer = self.timer_normal   
    def hit(self):
        if not self.dying:
            self.dying = True 
            self.timer = self.timer_explosion
            self.sb.increment_score()
    def update(self):
        
        self.rect.x += self.speed_factor

        # self.screen.blit(self.image, self.rect) 


# class Ufo(Sprite):
#     # alien_images = []
#     # for n in range(2):
#     #     alien_images.append(pg.image.load(f'images/alien{n}.bmp'))

#     # alien_images = [pg.image.load(f'images/alien{n}.bmp') for n in range(2)]

#     # alien_images0 = [pg.image.load(f'images/alien0{n}.bmp') for n in range(2)]
#     # alien_images1 = [pg.image.load(f'images/alien1{n}.bmp') for n in range(2)]
#     # alien_images2 = [pg.image.load(f'images/alien2{n}.bmp') for n in range(2)]

#     ufo_images0 = [pg.transform.rotozoom(pg.image.load(f'images/ufo__0{n}.png'), 0, 0.7) for n in range(2)]

#     # alien_images3 = [pg.image.load(f'images/alien3{n}.bmp') for n in range(2)]

#     # alien_types = {0: alien_images0, 1 : alien_images1, 2: alien_images2, 3: alien_images3}    
#     ufo_timers = {1 : Timer(image_list= ufo_images0) }
                  
#                 #    3 : Timer(image_list=alien_images3)}    

#     ufo_explosion_images = [pg.image.load(f'images/ship_explode{n}.png') for n in range(6)]

#     def __init__(self, game,type):
#         super().__init__()
#         self.screen = game.screen
#         self.settings = game.settings
#         self.image = pg.image.load('images/ufo__00.png')
#         self.rect = self.image.get_rect()
#         self.rect.y = self.rect.height
#         self.x = float(self.rect.x)
#         self.type = type
#         self.sb = game.scoreboard
        
#         self.dying = self.dead = False
        
#         # self.timer_normal = Timer(image_list=self.alien_images)   
#         # self.timer_normal = Timer(image_list=self.alien_types[type])
                      
#         self.timer_normal = Ufo.ufo_timers[1]              
#         self.timer_explosion = Timer(image_list =Ufo.ufo_explosion_images, is_loop=False)  
#         self.timer = self.timer_normal                                    

#     def check_edges(self): 
#         screen_rect = self.screen.get_rect()
#         return self.rect.right >= screen_rect.right or self.rect.left <= 0
#     def check_bottom_or_ship(self, ship):
#         screen_rect = self.screen.get_rect()
#         return self.rect.bottom >= screen_rect.bottom or self.rect.colliderect(ship.rect)
#     def hit(self):
#         if not self.dying:
#             self.dying = True 
#             self.timer = self.timer_explosion
#             self.sb.increment_score()
#     def update(self): 
#         if self.timer == self.timer_explosion and self.timer.is_expired():
#             self.kill()
#         settings = self.settings
#         self.x += (settings.ufo_speed_factor * settings.fleet_direction)
#         self.rect.x = self.x
#         self.draw()
#     def draw(self): 
#         image = self.timer.image()
#         rect = image.get_rect()
#         rect.left, rect.top = self.rect.left, self.rect.top
#         self.screen.blit(image, rect)
#         # self.screen.blit(self.image, self.rect) 


# class Ufos:
#     def __init__(self, game): 
#         self.model_ufo= Ufo(game=game, type=1)
#         self.game = game
#         self.sb = game.scoreboard
#         self.ufos = Group()

#         # self.ship_lasers = game.ship.lasers.lasers    # a laser Group
#         # self.aliens_lasers = Lasers(settings=game.settings)

#         self.ship_lasers = game.ship_lasers.lasers    # a laser Group
#         #self.aliens_lasers = game.alien_lasers

#         self.screen = game.screen
#         self.settings = game.settings
#         self.shoot_requests = 0
#         self.ship = game.ship
#         self.create_fleet()
#     def get_number_ufos_x(self, ufo_width):
#         available_space_x = self.settings.screen_width - 6 * ufo_width
#         number_ufos_x = int(available_space_x / (1.2 * ufo_width))
#         return number_ufos_x
#     def get_number_rows(self, ship_height, ufo_height):
#         available_space_y = (self.settings.screen_height - (3 * ufo_height) - ship_height)
#         number_rows = int(available_space_y / (1 * ufo_height))
#         number_rows = 1
#         return number_rows        
#     def reset(self):
#         self.ufos.empty()
#         self.create_fleet()
#         #self.aliens_lasers.reset()
#     def create_ufo(self, ufo_number, row_number):
#         # if row_number > 5: raise ValueError('row number must be less than 6')
#         type = row_number // 1     
#         ufo = Ufo(game=self.game, type=type)
#         ufo_width = ufo.rect.width

#         ufo.x = ufo_width + 2 * ufo_width * ufo_number 
#         ufo.rect.x = ufo.x
#         ufo.rect.y = ufo.rect.height + 1.2 * ufo.rect.height * row_number 
#         self.ufos.add(ufo)     

#     def create_fleet(self):
#         number_ufos_x = self.get_number_ufos_x(self.model_ufo.rect.width) 
#         number_rows = self.get_number_rows(self.ship.rect.height, self.model_ufo.rect.height)
#         for row_number in range(number_rows):
#             for ufo_number in range(number_ufos_x):
#                    self.create_ufo(ufo_number, row_number)
#     def check_fleet_edges(self):
#         for ufo in self.ufos.sprites(): 
#             if ufo.check_edges():
#                 self.change_fleet_direction()
#                 break
#     def check_fleet_bottom(self):
#         for ufo in self.ufos.sprites():
#             if ufo.check_bottom_or_ship(self.ship):
#                 self.ship.hit()
#                 break
#     def check_fleet_empty(self):
#         if len(self.ufos.sprites()) == 0:
#             print('Aliens all gone!')
#             self.game.reset()
#     def change_fleet_direction(self):
#         for ufo in self.ufos.sprites():
#             ufo.rect.y += self.settings.fleet_drop_speed
#         self.settings.fleet_direction *= -1
#     # def shoot_from_random_ufo(self):
#     #     self.shoot_requests += 1
#     #     if self.shoot_requests % self.settings.ufos_shoot_every != 0:
#     #         return
        
#         num_ufo = len(self.ufos.sprites())
#         ufo_num = randint(0, num_ufo)
#         i = 0
#         # for ufo in self.ufos.sprites():
#         #     if i == ufo_num:
#         #         self.aliens_lasers.shoot(game=self.game, x=ufo.rect.centerx, y=ufo.rect.bottom)
#         #     i += 1

#     # alien_lasers hitting the ship Or
#     # alien_lasers hitting a barrier or
#     # alien_lasers hitting a ship_lasers

#     # ship_lasers hitting an alien or
#     # ship_lasers hitting a barrier or
#     # ship_lasers hitting an aliens_lasers


#     def check_collisions(self):  
#         collisions = pg.sprite.groupcollide(self.ufos, self.ship_lasers, False, True)  
#         if collisions:
#             for ufo in collisions:
#                 ufo.hit()

#         # collisions = pg.sprite.spritecollide(self.ship, self.aliens_lasers.lasers, True)
#         # if collisions:
#         #     self.ship.hit()

#         # aliens_lasers collide with barrier?

#         # ship_lasers collide with barrier?

#         # aliens_lasers collide with ship_lasers ?


#     def update(self): 
#         self.check_fleet_edges()
#         self.check_fleet_bottom()
#         self.check_collisions()
#         self.check_fleet_empty()
#         ##self.shoot_from_random_ufo()
#         for ufo in self.ufos.sprites():
#             if ufo.dead:      # set True once the explosion animation has completed
#                 ufo.remove()
#             ufo.update() 
#         #self.aliens_lasers.update()
#     def draw(self): 
#         for ufo in self.ufos.sprites(): 
#             ufo.draw() 

