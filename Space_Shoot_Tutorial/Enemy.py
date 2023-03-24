import pygame
import random
from Parameter import Enemies,WIDTH,HEIGHT,ENEMY_NUM,ENEMY_ON_TASK

Enemy_List = []

Enemy_on_task = []

BIRTH_POS = [[WIDTH/2,-100],[-100,50],[WIDTH+100,50]]

def Lunch_Enemy():
    while len(Enemy_on_task) < ENEMY_ON_TASK:
        enemy = random.choice(Enemy_List)
        Enemy_on_task.append(enemy)
        Enemy_List.remove(enemy)

def Load_Enemy():
    while len(Enemy_List)<ENEMY_NUM:
        enemy = Enemy()
        Enemy_List.append(enemy)

class Enemy():
    def __init__(self):
        super().__init__()
        self.enemy = pygame.image.load(random.choice(Enemies))
        self.enemy = pygame.transform.scale(self.enemy, (75, 75))
        self.birth_pos = random.choice(BIRTH_POS)
        self.enemy_rect = self.enemy.get_rect(center = (self.birth_pos[0],self.birth_pos[1]))
        self.direction = random.choice(['left','right'])
        self.speed = random.randint(1,3)
        self.down_speed = random.randint(1,3)
        self.turn_distance = random.randint(100,400)
        self.start_x = random.choice([0,WIDTH])
        if self.enemy_rect.centerx == -100:
            self.start_x = 0
        elif self.enemy_rect.centerx == WIDTH+100:
            self.start_x = WIDTH
    
    def Enemy_Move(self):
        self.enemy_rect.centery += self.down_speed

        if self.enemy_rect.left < 0:
            self.direction = 'right'
        elif self.enemy_rect.right > WIDTH:
            self.direction = 'left'
        
        if self.direction == 'right':
            self.enemy_rect.centerx += self.speed
        elif self.direction == 'left':
            self.enemy_rect.centerx -= self.speed
        
        if abs(self.enemy_rect.centerx - self.start_x) >= self.turn_distance:
            if self.direction == 'left':
                self.direction = 'right'
            elif self.direction == 'right':
                self.direction = 'left'
            self.start_x = self.enemy_rect.centerx

    def Enemy_Out(self):
        if self.enemy_rect.top > HEIGHT:
            return True

    def Show_Enemy(self,Surface):
        Surface.blit(self.enemy,self.enemy_rect)

    def Update(self,Surface):
        self.Show_Enemy(Surface)
        self.Enemy_Move()


