import pygame

pygame.init()

screen = pygame.display.set_mode((432, 576))
cell_image = pygame.image.load('images/cell.png').convert_alpha()
mine_image = pygame.image.load('images/mine.png').convert_alpha()
icon = pygame.image.load('images/icon.png').convert_alpha()
bomb = pygame.image.load('images/pngwing.com.png')
flag = pygame.image.load('images/flag.png').convert_alpha()
none = pygame.image.load('images/none.png')
digit_list = [
              pygame.image.load('images/1.png').convert_alpha(), pygame.image.load('images/2.png').convert_alpha(),
              pygame.image.load('images/3.png').convert_alpha(), pygame.image.load('images/4.png').convert_alpha(),
              pygame.image.load('images/5.png').convert_alpha(), pygame.image.load('images/6.png').convert_alpha(),
              pygame.image.load('images/7.png').convert_alpha(), pygame.image.load('images/8.png').convert_alpha()
              ]
