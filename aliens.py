import pygame
pygame.init()

width = 800
height = 600
window = pygame.display.set_mode((width, height))
clock = time.Clock()
#главный класс
class GameSprite(sprite.Sprite):
   def __init__(self, y, x, player_image, player_x, player_y, player_speed):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (x, y))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
#класс врагов
class Emeny(GameSprite):
    def update(self):
        if self.rect.x >= 50:
            self.rect.x -= 50
        else:
            self.rect.y += 50
        
            
            
#управление
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
           self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
           self.rect.x += self.speed
    def fire(self):
        bullet = Bullet(img_bullet, self.rect.centerx - 50, self.rect.top, 75, 60, -10)
        bullets.add(bullet)

class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
           self.kill()
finish = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                fire_sound.play()
                ship.fire()
 
    if not finish:
        window.blit(background,(0,0))

        Bullet.update()





            

