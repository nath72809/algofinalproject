import pygame
pygame.init()
direction = 0
width = 800
height = 600
window = pygame.display.set_mode((width, height))
clock = time.Clock()

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
        
class Enemy(GameSprite):
   def update(self):
       if self.rect.x >= 50 and self.rect.x <= 450 and i == 0:
            self.rect.x += 10
       if self.rect.x >= 450:
            self.rect.y += 25
            i += 1
       if self.rect.x <= 50:
            self.rect.y += 25
            i -= 1
        if self.rect.x >= 50 and self.rect.x <= 450 and i == 1:
            self.rect.x -= 10
    def fire(self):
        bullet = Bullet(img_bullet, self.rect.centerx - 50, self.rect.top, 75, 60, -10)
        bullets.add(bullet)
        
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





            

