import start_tkinter
from game import *

start_tkinter.stub()

user_name = None

with shelve.open('current_user') as file:
    for i in file.values():
        user_name = i
    file.close()


class Menu(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((432, 144))
        self.rect = self.image.get_rect()

    def draw(self, color: tuple, topleft_x: int, topleft_y: int):
        self.image.fill(color)
        self.rect.topleft = (topleft_x, topleft_y)
        screen.blit(self.image, self.rect)


def print_text(message, x, y, font_color=(0, 0, 0), font_type='fonts/MangabeyRegular-rgqVO.otf', font_size=50):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    screen.blit(text, (x, y))


def run_main(name=None):
    easy = Menu()
    easy.draw((128, 255, 0), 0, 144)

    middle = Menu()
    middle.draw((255, 178, 102), 0, 288)

    strong = Menu()
    strong.draw((255, 102, 102), 0, 432)

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
                    easy_game = Game(9, 9, mine_number=10, name=name)
                    easy_game.run_game()
                if middle.rect.collidepoint(event.pos):
                    middle_game = Game(16, 16, mine_number=40, name=name)
                    middle_game.run_game()
                if strong.rect.collidepoint(event.pos):
                    strong_game = Game(30, 16, mine_number=99, name=name)
                    strong_game.run_game()
        pygame.display.flip()
        pygame.display.update()


os.remove('current_user.bak')
os.remove('current_user.dat')
os.remove('current_user.dir')

if __name__ == '__main__':
    run_main(name=user_name)
