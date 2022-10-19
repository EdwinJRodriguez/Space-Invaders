from tkinter.tix import TEXT
import pygame as pg
from settings import Settings
import game_functions as gf


from laser import Lasers, LaserType
from alien import Aliens
from ship import Ship
from sound import Sound
from scoreboard import Scoreboard
from barrier import Barriers
import sys
from button import Button
from ufo import Ufo
from os import path
from random import randint


TEXT_COL = ( 255, 255, 255)

class Game:
    def __init__(self):
        pg.init()
        self.settings = Settings()
        size = self.settings.screen_width, self.settings.screen_height   # tuple
        self.screen = pg.display.set_mode(size=size)
        pg.display.set_caption("Alien Invasion")
        self.bg_image = pg.image.load(f'images/space_background.jpg')
        


        self.game_paused = False

        self.run = True
        

        self.font = pg.font.SysFont("arialblack", 60)
        self.font1 = pg.font.SysFont("arialblack", 40)

        self.alien_img0 = pg.image.load(f'images/alien__00.png').convert_alpha()
        self.alien_img1 = pg.image.load(f'images/alien__10.png').convert_alpha()
        self.alien_img2 = pg.image.load(f'images/alien__20.png').convert_alpha()
        self.ufo_img0 = pg.image.load('images/ufo__00.png').convert_alpha()

        self.play_image = pg.image.load(f'images/pbutton.png').convert_alpha()
        self.play_button = Button(500, 550, self.play_image,1)

        ##self.resume_image = pg.image.load(f'images/resumebutton.png').convert_alpha()
        ##self.resume_button = Button(450, 300, self.resume_image, 1)

        self.sound = Sound(bg_music="sounds/zelda.wav")
        self.scoreboard = Scoreboard(game=self)  
        self.ship_lasers = Lasers(settings=self.settings, type=LaserType.SHIP)
        self.alien_lasers = Lasers(settings=self.settings, type=LaserType.ALIEN)
        
        ##ufo set up
        self.ufo = pg.sprite.GroupSingle()
        self.ufo_spawn_time = randint(40,80)



        self.barriers = Barriers(game=self)
        self.ship = Ship(game=self)
        self.aliens = Aliens(game=self)
        self.settings.initialize_speed_settings()

    def ufo_timer(self):
        self.ufo_spawn_time -=1
        if self.ufo_spawn_time <= 0:
            self.ufo.add(Ufo(self.settings.screen_width, self.settings.screen_height))
            self.ufo_spawn_time = randint(40,800)


    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        self.screen.blit(img, (x,y))

    def draw_aliens(self, img, scale, x, y):
        self.image = pg.transform.scale(img, (int(self.settings.screen_width * scale), int(self.settings.screen_height * scale)))
        self.screen.blit(img, (x, y))

    def draw_ufo(self, img, scale, x, y):
        self.image = pg.transform.scale(img, (int(self.settings.screen_width * scale), int(self.settings.screen_height * scale)))
        self.screen.blit(img, (x, y))

    def draw_bg(self, img, scale, x, y):
        self.image = pg.transform.scale(img, (int(self.settings.screen_width * scale), int(self.settings.screen_height * scale)))
        self.screen.blit(img, (x, y))

    def start_menu(self):

        running = True

        while running:
            self.screen.blit(self.bg_image, (0,0))
    
            gf.check_events(settings=self.settings, ship=self.ship, game = self)

            gf.check_events(settings=self.settings, ship=self.ship, game = self)
            # file = open('high_score.txt', 'r')
            
            file = open('highscore.txt', 'r')
            hs_text = str(file.read())
            file.close()
            hs_score = self.font1.render(hs_text, True, (255, 255, 255), (0,0,0))
            hs_rect = hs_score.get_rect()
            hs_rect.center = (325, 179)
            self.screen.blit(hs_score, hs_rect)

            self.draw_text("HighScore:  ", self.font1, TEXT_COL, 25, 150)
      
            

            self.draw_text("SPACE INVADERS", self.font, TEXT_COL, 300, 50)
            self.draw_text("= 10 points", self.font1, TEXT_COL, 500, 200)
            self.draw_text("= 20 points", self.font1, TEXT_COL, 500, 315)
            self.draw_text("= 30 points", self.font1, TEXT_COL, 500, 415)
            self.draw_text("= 50 points", self.font1, TEXT_COL, 500, 515)


            self.draw_aliens(self.alien_img0, 0.5, 375, 150)
            self.draw_aliens(self.alien_img1, 0.5, 375, 270)
            self.draw_aliens(self.alien_img2, 0.5, 375, 370)
            self.draw_ufo(self.ufo_img0, 0.5, 375, 470)

            if self.play_button.draw(self.screen):
                running = False
            
            pg.display.flip()

    def reset(self):
        print('Resetting game...')
        # self.lasers.reset()
        self.barriers.reset()
        self.ship.reset()
        self.aliens.reset()
        # self.scoreboard.reset()

    def game_over(self):
        print('All ships gone: game over!')
        self.sound.gameover()
        pg.quit()
        sys.exit()

    def play(self):
        self.sound.play_bg() 

        while self.run:     # at the moment, only exits in gf.check_events if Ctrl/Cmd-Q pressed
            gf.check_events(settings=self.settings, ship=self.ship, game = self)

            self.screen.blit(self.bg_image, (0,0))
  
            self.ship.update()

            self.aliens.update()
            self.barriers.update()
            self.ufo_timer()
            self.ufo.draw(self.screen)
            self.ufo.update()
            # self.lasers.update()
            self.scoreboard.update()
            pg.display.flip()


def main():
    g = Game()
    g.start_menu()

    g.play()



if __name__ == '__main__':
    main()
