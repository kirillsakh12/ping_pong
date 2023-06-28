#pinf_pong
from pygame import *
from random import *
from time import time as times
cjo = (255, 200, 135)
class GameSprite(sprite.Sprite):
    def __init__(self, p_image, p_x, p_y, p_speed, r1, r2):
        super().__init__()
        self.image = transform.scale(image.load(p_image), (r1, r2))
        self.speed = p_speed
        self.rect = self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        key_pr = key.get_pressed()
        if key_pr[K_UP] and self.rect.y >5:
            self.rect.y -= self.speed
        if key_pr[K_DOWN] and self.rect.y < 355:
            self.rect.y += self.speed
    def update_r(self):
        key_pr = key.get_pressed()
        if key_pr[K_w] and self.rect.y >5:
            self.rect.y -= self.speed
        if key_pr[K_s] and self.rect.y < 355:
            self.rect.y += self.speed

win = display.set_mode((600, 500))
display.set_caption('Shooter')
win.fill(cjo)
hero = Player('palka.png', 30, 200, 4, 50, 150)
hero1 = Player('palka.png', 500, 200, 4,50, 150)
speed_m = 4
sp_x = 4
sp_y = 4
mach = GameSprite('mach.png', 200, 200, speed_m, 50, 50)
mixer.init()
mixer.music.load('Battleship.ogg')
mixer.music.play()
fire = mixer.Sound('udar-po-metallicheskomu-disku1.ogg')
font.init()
font1 = font.Font(None, 70)
font2 = font.Font(None, 36)
winer = font1.render('GAME OWER Win 2' , True, (255, 0, 0))
lose = font1.render('GAME OWER Win 1' , True, (255, 0, 0))
game = True
finish = True
clock = time.Clock()
FPS = 60
while game:
    
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                finish = False
                mach = GameSprite('mach.png', 200, 200, speed_m, 50, 50)
    if finish!=True:
        win.fill(cjo)
        hero.reset()
        hero1.reset()
        hero.update_r()
        hero1.update()
        mach.reset()
        mach.rect.x += sp_x
        mach.rect.y += sp_y
        if mach.rect.y < 0 or mach.rect.y > 450:
            sp_y = sp_y * (-1)
        if sprite.collide_rect(hero, mach) or sprite.collide_rect(hero1, mach):
            sp_x = sp_x*(-1)
            fire.play()

        if mach.rect.x < 0 :
            finish = True
            win.blit(winer, (110, 200))
        if mach.rect.x > 550:
            finish = True
            win.blit(lose, (110, 200))
            
    
    display.update()
    clock.tick(FPS)
