import sys
import pygame
from Parameter import*
import SpaceShip,Bullet,Enemy,Explosion

pygame.init()

Game_Window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Venture")

Game_Timer = pygame.time.Clock()

Game_Cover = pygame.image.load('./img/Game_Cover.png')
Game_Cover_rect = Game_Cover.get_rect(center = (WIDTH/2,HEIGHT/2))

Game_Over = pygame.image.load('./img/Game_Over.png')
Game_Over_rect = Game_Over.get_rect(center = (WIDTH/2,HEIGHT/2))

Space_Background = pygame.image.load('./img/space_background.jpg')
Space_Background_rect = Space_Background.get_rect(center = (WIDTH/2,HEIGHT/2))
Space_Background.set_alpha(80)

SpaceShip.Load_Spaceship()
Enemy.Load_Enemy()
Enemy.Lunch_Enemy()

explosion = Explosion.Explosion()

pygame.mixer.music.load('./sound/game_bgm.mp3')
pygame.mixer.music.set_volume(0.3)

while True:
    
    Game_Timer.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_j:
                spaceship.shoot = True
                x = spaceship.Get_Position()[0]
                y = spaceship.Get_Position()[1]
                bullet = Bullet.Bullet(x,y)
                Bullet.bullet_list.append(bullet)
                bullet.Play()
            if event.key == pygame.K_SPACE:
                GAME_ON = True
                pygame.mixer.music.play()
                
    if not GAME_ON and not GAME_OVER:
        Game_Window.blit(Game_Cover,Game_Cover_rect)
        pygame.display.update()

    elif GAME_ON and not GAME_OVER:
        Game_Window.fill(BASE_COLOR)
        Game_Window.blit(Space_Background,Space_Background_rect)
        Enemy.Lunch_Enemy()
        for spaceship in SpaceShip.Spaceship_on_task:
            spaceship.Update(Game_Window)
            if spaceship.shoot:
                for bullet in Bullet.bullet_list:
                    bullet.Update(Game_Window)
                    if bullet.Bullet_Out():
                        Bullet.bullet_list.remove(bullet)
                    for enemy in Enemy.Enemy_on_task:
                        if bullet.Bullet_collide(enemy.enemy_rect):
                            explosion.Explode(Game_Window,enemy.enemy_rect.centerx,enemy.enemy_rect.centery)
                            explosion.Play()
                            Enemy.Enemy_on_task.remove(enemy)
                            Bullet.bullet_list.remove(bullet)
        for spaceship in SpaceShip.Spaceship_on_task:
            for enemy in Enemy.Enemy_on_task:
                if spaceship.Spaceship_collide(enemy.enemy_rect):
                    explosion.Explode(Game_Window,spaceship.spaceship_rect.centerx,spaceship.spaceship_rect.centery)
                    explosion.Play()
                    SpaceShip.Spaceship_on_task.remove(spaceship)
                    if SpaceShip.remain_life>0:
                        SpaceShip.Load_Spaceship()
                        SpaceShip.remain_life -= 1
                    else:
                        GAME_OVER = True

        for enemy in Enemy.Enemy_on_task:
            enemy.Update(Game_Window)
            if enemy.Enemy_Out():
                Enemy.Enemy_on_task.remove(enemy)
        pygame.display.update()

    elif GAME_ON and GAME_OVER:
        Game_Window.blit(Game_Over,Game_Over_rect)
        pygame.display.update()