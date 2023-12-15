
from images import *

all_cells = pygame.sprite.Group()
all_mines = pygame.sprite.Group()
all_digits = pygame.sprite.Group()
empty_cell = pygame.sprite.Group()
all_flags = pygame.sprite.Group()


class Cell(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = cell_image
        self.rect = self.image.get_rect()
        self.image.blit(cell_image, (0, 0))
        self.add(all_cells)


class Mine(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = mine_image
        self.rect = self.image.get_rect()
        self.image.blit(mine_image, (0, 0))
        self.add(all_mines)


class Digit(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((48, 48))
        self.rect = self.image.get_rect()
        self.add(all_digits)


class Flag(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = flag_image
        self.rect = self.image.get_rect()
        self.image.blit(flag_image, (0, 0))
        self.add(all_flags)


class EmptyCell(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = empty
        self.rect = self.image.get_rect()
        self.image.blit(empty, (0, 0))
        self.add(empty_cell)
