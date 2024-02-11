
import pygame

class Circle:
    def __init__(self, color, x, y, radius):
    self.color = color
    self.x = x
    self.y = y
    self.radius = radius

    def draw(self):



pygame.init()
width = 500
height = 500
win = pygame.display.set_mode((width, height))

x = 0
y = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    win.fill((255, 255, 255))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 3
    if keys[pygame.K_RIGHT]:
        x += 3
    if keys[pygame.K_UP]:
        y -= 3
    if keys[pygame.K_DOWN]:
        y += 3
    kryg.draw

    circle = Circle ((255, 255, 0), 0, 0, 30)
    pygame.draw.circle(win, (255, 255, 0), (x, y), 30)
    pygame.display.update()


































