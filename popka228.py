from pygame import*

class Wall(sprite.Sprite):
   def __init__(self, color, wall_x, wall_y, wall_width, wall_height):
       super().__init__()
       self.color = (R, G, B)
       self.width = wall_width
       self.height = wall_height
       # картинка стены - прямоугольник нужных размеров и цвета
       self.image = Surface((self.width, self.height))
       self.image.fill((color_1, color_2, color_3))
       # каждый спрайт должен хранить свойство rect - прямоугольник
       self.rect = self.image.get_rect()
       self.rect.x = wall_x
       self.rect.y = wall_y
def draw_wall(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
