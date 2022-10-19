import pygame as pg
from laser import LaserType
import time


class Sound:
    def __init__(self, bg_music):
        pg.mixer.init()
        pg.mixer.music.load(bg_music)
        pg.mixer.music.set_volume(0.1)
        lasergun_sound = pg.mixer.Sound('sounds/lasergun.wav')
        shiplaser_sound = pg.mixer.Sound('sounds/shiplaser.wav')
        gameover_sound = pg.mixer.Sound('sounds/marioGameOver.wav')
        self.sounds = {'lasergun': lasergun_sound, 'shiplaser': shiplaser_sound,
                       'marioGameOver': gameover_sound}

    def play_bg(self):
        pg.mixer.music.play(-1, 0.0)

    def stop_bg(self):
        pg.mixer.music.stop()

    def shoot_laser(self, type): 
        pg.mixer.Sound.play(self.sounds['lasergun' if type == LaserType.ALIEN else 'shiplaser'])
    def gameover(self): 
        self.stop_bg() 
        pg.mixer.music.load('sounds/marioGameOver.wav')
        self.play_bg()
        time.sleep(2.8)
