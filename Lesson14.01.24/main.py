import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                exit()

    color = (0, 0, 255)



    pygame.draw.rect(win, (255, 255, 255), (0, 0, 100, 100), 50)
    pygame.draw.rect(win, (255, 255, 255), (0, 0, 100, 100), 50)









    pygame.display.update()


