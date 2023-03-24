import pygame

class Explosion():
    def __init__(self):
        super().__init__()
        self.explosion = pygame.image.load('./img/Explosion.png')
        self.explosion = pygame.transform.scale(self.explosion,(70,70))
        self.explode_sound = pygame.mixer.Sound('./sound/explosion_sound.wav')
    
    def Play(self):
        self.explode_sound.play()

    def Explode(self,Surface,x,y):
        self.explosion_rect = self.explosion.get_rect(center = (x,y))
        Surface.blit(self.explosion,self.explosion_rect)

    
