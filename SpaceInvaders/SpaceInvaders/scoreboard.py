import pygame as pg 
from os import path
# import pygame.font

class Scoreboard:
    def __init__(self, game): 
        self.score = 0
        self.level = 0
        self.high_score = 0
        self.currentscore = self.score

        if self.high_score >= self.score:
            self.high_score = self.score

    
        
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.text_color = (30, 30, 30)
        self.font = pg.font.SysFont(None, 48)

        self.score_image = None 
        self.score_rect = None
        self.prep_score()

    def increment_score(self): 
        self.score += self.settings.alien_points
        self.prep_score()

    def prep_score(self): 
        score_str = str(self.score)
        self.score_image = self.font.render(score_str, True, (255, 255, 255), (0,0,0))

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def reset(self): 
        self.score = 0
        self.update()

    def update(self): 
        # TODO: other stuff
        self.draw()
    def update_hs(self):
        self.hs = open('high_score.txt', 'r')
        self.high_score = int(self.hs.read())
        self.hs.close()
        if self.high_score < self.score:
            hs_write = open('highscore.txt', 'w')
            hs_write.write(str(self.score))
            hs_write.close()
            
    def set_highschool(self):
        self.file = open("highscore.txt", 'w')
        self.file.write(str(self.high_score))
        self.file.close()


    def draw(self): 
        self.screen.blit(self.score_image, self.score_rect)

    def highscore():
        pass
