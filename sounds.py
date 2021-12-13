import pygame

pygame.init()
pygame.mixer.init()

win_sound = pygame.mixer.Sound('sounds/you_win.wav')
cell_sound = pygame.mixer.Sound('sounds/cell_sound.wav')
boom_sound = pygame.mixer.Sound('sounds/boom_sound.wav')
