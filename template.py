import os
import pygame
import sys
import abc
import pygame_gui

class Game(object):
    def __init__(self, width, height, FPS):
        pygame.init()
        self.display = pygame.display.set_mode((width, height))
        self.FPS = FPS

    def __mouse_effect_handler(self):
        pass

    # сразу продумать подсчёт дохода с одной территории, оптимально по памяти времени и прочей хуйне
    def __calculate_income(self):  # и прочие служебные функции
        pass

    def __new_turn(self):
        self.__calculate_income()

    def run(self):
        clock = pygame.time.Clock()
        game_over = False
        while not game_over:
            clock.tick(self.FPS)


class GameObject(abc.ABC):
    def __init__(self, img):
        self.img = img
        # прикрутить звук. Явно dict
        pass

    def animate(self):
        pass


class Surroundings(GameObject):
    def __init__(self, img):
        super().__init__(img)


class Tree(GameObject):
    def __init__(self, img):
        super().__init__(img)


class AbstractUnit(GameObject):
    level = int

    def __init__(self, img):
        super().__init__(img)


class Unit(AbstractUnit):
    def __init__(self, img):
        super().__init__(img)

    def move(self):  # получает клетку и проверяет что она достижима по координатам??
        pass


class Tower(AbstractUnit):
    def __init__(self, img):
        super().__init__(img)


class Cell(pygame.Surface):
    def __init__(self, img, coordinates):
        self.img = img
        self.coordinates = coordinates

    def animate(self):
        pass


class PlayableCell(Cell):

    def __find_neighbours(self):
        neighbours = []
        return neighbours

    def __init__(self, img, coordinates, content, owner=None):
        super().__init__(img, coordinates)
        self.neighbours = self.__find_neighbours()
        self.content = content
        self.owner = owner

    def animate(self):
        self.content.animate()


class Decoration(Cell):
    def __init__(self, img, coordinates):
        super().__init__(img, coordinates)


class Player(object):
    def __init__(self, name):
        self.name = name


class Button(object):
    pass
