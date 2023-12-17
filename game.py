import shelve
from random import choice

import pygame.time

from objects import *
from sounds import *

pygame.mixer.pre_init()
pygame.init()
pygame.font.init()


class Game:
    def __init__(self, w, h, mine_number, name=None):
        self.w = w
        self.h = h
        self.mine_number = mine_number
        self.user_name = name
        print(self.user_name)
        self.field_width = self.w * 48
        self.field_height = self.h * 48
        self.field = pygame.display.set_mode((self.field_width, self.field_height + 60))
        self.x_cell_list = [x for x in range(0, self.field_width, 48)]
        self.y_cell_list = [y for y in range(60, self.field_height + 48, 48)]

    pygame.display.set_caption('Minesweeper by Pygame')

    x_mine_list = list()
    y_mine_list = list()
    list_of_deleted_mines_topleft = list()
    user_list_time = list()

    time_m = 0
    time_s = 0

    fake_count = None

    file_name = ''

    def draw_start_field(self):
        """  Draw start field
        """
        for i in self.x_cell_list:
            for j in self.y_cell_list:
                cell = Cell()
                cell.rect.topleft = (i, j)
                # cell.image.set_alpha(100)  # Uncomment to see bombs.
                self.field.blit(cell.image, cell.rect)

    def set_mine_random(self):
        """ Fills the playing field by mines
            with random coordinates,
            eliminates the possibility of two mines
            in the same cell.
        """
        m = 0
        while m < self.mine_number:
            x_mine = choice(self.x_cell_list)
            y_mine = choice(self.y_cell_list)
            self.y_mine_list.append(y_mine)
            if self.check_of_duplicate_mines(x_mine):
                del self.y_mine_list[-1]
                continue
            else:
                self.x_mine_list.append(x_mine)
                m += 1
                mine = Mine()
                mine.rect.topleft = (x_mine, y_mine)
            # self.field.blit(mine.image, mine.rect)  # Uncomment to see bombs.

    def check_of_duplicate_mines(self, x_mine):
        """ Checks for duplicate mines.
        """
        list_of_occurrences = [i for i in range(len(self.x_mine_list)) if self.x_mine_list[i] == x_mine]
        if x_mine in self.x_mine_list:
            for i in list_of_occurrences:
                if self.y_mine_list[-1] == self.y_mine_list[i]:
                    return True
        else:
            return False
        del list_of_occurrences

    @staticmethod
    def check_nearby_mines(mine_list, x, y):
        """ Checks the number of mines around the given cell
            and creates an instance of the Digit class.
        """
        dict_of_nearby_cells = \
            {
                1: ((x - 48), (y - 48)), 2: (x, (y - 48)), 3: ((x + 48), (y - 48)),
                4: ((x - 48), y), 5: (x, y), 6: ((x + 48), y),
                7: ((x - 48), (y + 48)), 8: (x, (y + 48)), 9: ((x + 48), (y + 48))
            }
        number_of_nearby_mines = 0
        for i in dict_of_nearby_cells:
            if dict_of_nearby_cells[i] in mine_list:
                number_of_nearby_mines += 1
        if number_of_nearby_mines > 0:
            digit = Digit()
            digit.image.blit(digit_list[number_of_nearby_mines - 1], (0, 0))
            digit.rect.topleft = x, y

    def set_nearby_mines(self):
        """ Creates instances of the Digit class
            all over the playing field,
            Skips cells with mines.
        """
        mine_list = list(zip(self.x_mine_list, self.y_mine_list))
        for i in self.x_cell_list:
            for j in self.y_cell_list:
                cell_ = (i, j)
                if cell_ in mine_list:
                    continue
                else:
                    self.check_nearby_mines(mine_list, i, j)
        del mine_list

    def open_empty_cell(self, x_pos, y_pos):
        """ Recursively opens empty cells and
            cells with the closest digits.
        """
        dict_ = \
            {
                1: ((x_pos - 48), (y_pos - 48)), 2: (x_pos, (y_pos - 48)), 3: ((x_pos + 48), (y_pos - 48)),
                4: ((x_pos - 48), y_pos), 5: (x_pos, y_pos), 6: ((x_pos + 48), y_pos),
                7: ((x_pos - 48), (y_pos + 48)), 8: (x_pos, (y_pos + 48)), 9: ((x_pos + 48), (y_pos + 48))
            }
        empty_list = []
        for i, j in dict_.values():
            for cell in empty_cell:
                if cell.rect.collidepoint(i, j):
                    self.field.blit(empty, cell.rect)
                    empty_list.append(cell.rect.topleft)
                    cell.kill()
            for digit in all_digits:
                if digit.rect.collidepoint(i, j):
                    self.field.blit(digit.image, digit.rect)
                    digit.kill()
            for cell in all_cells:
                if cell.rect.collidepoint(i, j):
                    cell.kill()
        unique_empty_list = list(set(empty_list))
        del empty_list
        for cell in empty_cell:
            if cell.rect.collidepoint(x_pos, y_pos) and cell.rect.topleft in unique_empty_list:
                unique_empty_list.remove(cell.rect.topleft)
                cell.kill()
        if len(unique_empty_list) != 0:
            pygame.mixer.Sound.play(cell_sound)
            for i in unique_empty_list:
                u, v = i
                self.open_empty_cell(u, v)
        del unique_empty_list

    def open_digit_cell(self, x_pos, y_pos, digit):
        """ Opens the cell with the number.
        """
        self.field.blit(digit.image, digit.rect)
        digit.kill()
        for cell in all_cells:
            if cell.rect.collidepoint(x_pos, y_pos):
                cell.kill()
                break

    def draw_flag(self, x, y):
        """ Draws the flag.
            You cannot set a flag on an empty cell, digit, or other flag.
        """
        flag = Flag()
        for cell in all_cells:
            if cell.rect.collidepoint(x, y):
                self.fake_count -= 1
                flag.rect.topleft = cell.rect.topleft
                self.field.blit(empty, cell.rect)
                self.field.blit(flag.image, cell.rect.topleft)
                cell.kill()
                if pygame.sprite.spritecollideany(cell, all_mines):
                    pygame.sprite.spritecollideany(cell, all_mines).kill()
                    self.list_of_deleted_mines_topleft.append(cell.rect.topleft)
                break

    def run_game(self):
        time_millis = False
        clock = None
        game = True
        end = False
        self.set_mine_random()
        self.set_nearby_mines()
        self.draw_start_field()
        self.fake_count = self.mine_number
        for cell in all_cells:
            if not pygame.sprite.spritecollideany(cell, all_digits):
                if not pygame.sprite.spritecollideany(cell, all_mines):
                    emptycell = EmptyCell()
                    emptycell.rect.topleft = cell.rect.topleft
        while game:
            pygame.draw.rect(self.field, (44, 41, 40), (0, 0, self.field_width, 60))
            self.field.blit(bomb, (30, 8))
            self.print_text(f': {self.fake_count}', 100, 15, (200, 40, 40),
                            font_type='fonts/MangabeyRegular-rgqVO.otf', font_size=50)
            self.display_time(self.time_s, self.time_m)
            if len(all_mines) == 0 and len(all_flags) == self.mine_number:
                end = True
                pygame.mixer.Sound.play(win_sound)
                self.you_win()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    x, y = event.pos

                    if event.button == 3:
                        self.draw_flag(x, y)

                    elif event.button == 2:
                        for flag in all_flags:
                            if flag.rect.collidepoint(x, y):
                                cell = Cell()
                                cell.rect.topleft = flag.rect.topleft
                                self.field.blit(cell.image, cell.rect)
                                if flag.rect.topleft in self.list_of_deleted_mines_topleft:
                                    mine = Mine()
                                    coord = self.list_of_deleted_mines_topleft.index(flag.rect.topleft)
                                    mine.rect.topleft = self.list_of_deleted_mines_topleft[coord]
                                    self.list_of_deleted_mines_topleft.pop(coord)
                                    print(len(all_mines))
                                flag.kill()
                                self.fake_count += 1
                                break

                    elif event.button == 1:
                        for mine in all_mines:
                            if mine.rect.collidepoint(x, y):
                                end = True
                                pygame.mixer.Sound.play(boom_sound)
                                self.game_over()
                                break
                        for digit in all_digits:
                            if digit.rect.collidepoint(x, y):
                                self.open_digit_cell(x, y, digit)
                                break
                        for cell in empty_cell:
                            if cell.rect.collidepoint(x, y):
                                self.open_empty_cell(x, y)
                                break
                        clock = pygame.time.Clock()
                        time_millis = clock.tick(15)

            if not end and time_millis:
                time_millis = clock.tick(15)
                self.time_s += time_millis / 1000
                self.time_m += time_millis / 60000

            pygame.display.flip()
            pygame.display.update()

    def game_over(self):
        stopped = True
        while stopped:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            for mine in all_mines:
                self.field.blit(mine.image, mine.rect)
                mine.kill()
            self.print_text('Game over', self.field_width // 2 - 150, self.field_height // 2)
            pygame.display.update()
            self.restart()

    def restart(self):
        pygame.draw.rect(screen, (0, 0, 200), pygame.Rect(self.field_width // 2 - 90,
                                                          self.field_height // 2 + 100, 150, 70))
        self.print_text('menu', self.field_width // 2 - 75, self.field_height // 2 + 105, font_size=60)
        pygame.display.flip()
        all_cells.empty()
        all_digits.empty()
        all_flags.empty()
        empty_cell.empty()
        self.y_mine_list.clear()
        self.x_mine_list.clear()
        self.list_of_deleted_mines_topleft.clear()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                if event.button == 1:
                    if self.field_width // 2 - 90 < x < self.field_width // 2 + 60 \
                            and self.field_height // 2 + 100 < y < self.field_height // 2 + 170:
                        self.field = pygame.display.set_mode((432, 144 * 4))
                        from main import run_main
                        run_main(name=self.user_name)

    def display_time(self, time_s, time_m):
        time_str_s = str(int(time_s) - int(time_m) * 60)
        time_str_m = str(int(time_m))
        if 0 <= int(time_s) - int(time_m) * 60 < 10:
            self.print_text(f'Time: {time_str_m}: 0{time_str_s}', self.field_width - 200, 15,
                            (200, 40, 40), 'fonts/MangabeyRegular-rgqVO.otf', 50)
        else:
            self.print_text(f'Time: {time_str_m}: {time_str_s}', self.field_width - 200, 15,
                            (200, 40, 40), 'fonts/MangabeyRegular-rgqVO.otf', 50)

    def you_win(self):
        stopped = True
        if self.mine_number == 10:
            self.file_name = 'easy_best_time'
        elif self.mine_number == 40:
            self.file_name = 'middle_best_time'
        else:
            self.file_name = 'strong_best_time'
        if self.user_name:
            self.wright_count_best(self.file_name, self.time_s)
            import count_tkinter
            count_tkinter.final_widow(self.file_name, self.time_s)
        while stopped:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.print_text('You win!', self.field_width // 2 - 120, self.field_height // 2 - 100)
            pygame.display.update()
            self.restart()

    def print_text(self, message, x, y, font_color=(220, 90, 87), font_type='fonts/FrostbiteBossFight-dL0Z.ttf',
                   font_size=80):
        font_type = pygame.font.Font(font_type, font_size)
        text = font_type.render(message, True, font_color)
        self.field.blit(text, (x, y))

    def wright_count_best(self, file_name: str, time_s):
        with shelve.open(file_name) as file:

            if self.user_name not in file:
                self.user_list_time = [time_s, ]
                print(self.user_list_time)
                file[self.user_name] = self.user_list_time
            else:
                self.user_list_time = file[self.user_name]
                self.user_list_time.append(time_s)
                file[self.user_name] = self.user_list_time
                file.sync()
                file.close()
