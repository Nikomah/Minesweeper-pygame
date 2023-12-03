
from game import *


clock = pygame.time.Clock()


class Menu(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((432, 144))
        self.rect = self.image.get_rect()


def print_text(message, x, y, font_color=(0, 0, 0), font_type='fonts/MangabeyRegular-rgqVO.otf', font_size=50):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    screen.blit(text, (x, y))


def run_main():
    easy = Menu()
    easy.image.fill((128, 255, 0))
    easy.rect.topleft = 0, 144
    screen.blit(easy.image, easy.rect)

    middle = Menu()
    middle.image.fill((255, 178, 102))
    middle.rect.topleft = 0, 288
    screen.blit(middle.image, middle.rect)

    strong = Menu()
    strong.image.fill((255, 102, 102))
    strong.rect.topleft = 0, 432
    screen.blit(strong.image, strong.rect)

    print_text('choose field:', 110, 50, font_color=(220, 90, 87))
    print_text('9 x 9', 160, 194)
    print_text('16 x 16', 150, 338)
    print_text('32 x 16', 150, 482)

    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                if easy.rect.collidepoint(event.pos):
                    easy_game = Game(9, 9, mine_number=10)
                    easy_game.run_game()
                if middle.rect.collidepoint(event.pos):
                    middle_game = Game(16, 16, mine_number=40)
                    middle_game.run_game()
                if strong.rect.collidepoint(event.pos):
                    strong_game = Game(30, 16, mine_number=99)
                    strong_game.run_game()
        pygame.display.flip()
        clock.tick(30)
        pygame.display.update()
    quit()


run_main()
