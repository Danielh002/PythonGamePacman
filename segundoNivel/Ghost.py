import pygame
class Ghost(pygame.sprite.Sprite):
    def __init__(self):
        self.image=pygame.image.load("images/monster_green.png")
        self.rect=self.image.get_rect()
        self.rect.top=500
        self.rect.left=500
    def move(self,playerX,playerY):
        dx=playerX-self.rect.left
        dy=playerY-self.rect.top
        if(dy!=0 or dx!=0):
            d=(dx/abs(float((dy**2+dx**2)**(1/2.0))),dy/abs(float((dy**2+dx**2)**(1/2.0))))
            self.rect.move_ip(d[0]*9,d[1]*9)