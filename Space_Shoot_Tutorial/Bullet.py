import pygame
from Parameter import BULLET_WIDTH,BULLET_HEIGHT,BULLET_SPEED

bullet_list = []

class Bullet():
    def __init__(self,x,y):
        super().__init__()
        self.bullet = pygame.image.load('./img/bullet.png')
        self.bullet = pygame.transform.scale(self.bullet, (BULLET_WIDTH, BULLET_HEIGHT))
        self.bullet_rect = self.bullet.get_rect(center = (x,y))
        self.shoot_sound = pygame.mixer.Sound('./sound/shoot_sound.wav')
    
    def Show_Bullet(self,Surface):
        Surface.blit(self.bullet,self.bullet_rect)

    def Bullet_Out(self):
        if self.bullet_rect.bottom < 0:
            return True

    def Bullet_collide(self,enemy_rect):
        if self.bullet_rect.colliderect(enemy_rect):
              return True

    def Play(self):
        self.shoot_sound.play()

    def Update(self,Surface):
        self.Show_Bullet(Surface)
        self.bullet_rect.centery -= BULLET_SPEED




        