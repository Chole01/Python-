import pygame
from Parameter import WIDTH,HEIGHT,PLAYER_LIFE

Spaceship_on_task = []

remain_life = PLAYER_LIFE

def Load_Spaceship():   
      spaceship = Spaceship()
      Spaceship_on_task.append(spaceship)

class Spaceship():
    def __init__(self):
        super().__init__()
        self.spaceship = pygame.image.load('./img/space_plane.png')
        self.spaceship = pygame.transform.scale(self.spaceship,(100,130))
        self.spaceship_rect = self.spaceship.get_rect(center=(WIDTH/2,HEIGHT-100))
        self.shoot = False
        
    
    def Show_spaceship(self,Surface):
        Surface.blit(self.spaceship,self.spaceship_rect)
    
    def Player_control(self):
        if pygame.key.get_pressed()[pygame.K_a] and self.spaceship_rect.left > 0:
                self.spaceship_rect.left -= 8
        if pygame.key.get_pressed()[pygame.K_d] and self.spaceship_rect.right < WIDTH:
                self.spaceship_rect.right += 8
        if pygame.key.get_pressed()[pygame.K_w] and self.spaceship_rect.top > 0:
                self.spaceship_rect.top -= 8
        if pygame.key.get_pressed()[pygame.K_s] and self.spaceship_rect.bottom < HEIGHT:
                self.spaceship_rect.bottom += 8
    
    def Spaceship_collide(self,enemy_rect):
        if self.spaceship_rect.colliderect(enemy_rect):
              return True

    def Get_Position(self):
          x = self.spaceship_rect.centerx
          y = self.spaceship_rect.top-20
          return x,y

    def Update(self,Surface):
        self.Show_spaceship(Surface)
        self.Player_control()