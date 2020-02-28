import pygame
import random
from dic import objec, correctsubject_py
import sys
import time
from LevelF import LevelFirst
from LevelS import LevelSECOND
class StartPage():
    def __init__(self):
        pygame.init()  # вызов библиотеки pygame
        pygame.display.set_caption("window")
        sc = pygame.display.set_mode((1188, 746))  # заводим главный экран и определяем его размеры и загружаем его в переменную sc
        sc.fill((100, 150, 200))
        field = pygame.image.load('Naca Rodina1.png')  # подгрузка файла для фоновой заливки в переменную fild
        background = field.get_rect(bottomright=(1188, 746))  # вливаем размеры и разрешение файла фоновой заливки в переменную bakground
        sc.blit(field, background)  # говорим показать
        pygame.display.update()  # первый раз прорисовываем экран
        k = 1
        b = True
        f = 0
        while b:  # заводим бесконечный цикл
            for i in pygame.event.get():
                # pygame.font.init()
                if i.type == pygame.QUIT:  # нажимаем кнопку закрытия экрана
                    pygame.time.delay(20)
                if i.type == pygame.MOUSEBUTTONDOWN:  # нажимаем что-нибудь на мыши
                    if i.button == 1:  # клик ЛКМ
                        x = i.pos[0]
                        y = i.pos[1]
                        if x > 844 and x < 1073 and y > 607 and y < 703:
                            pygame.init()  # вызов библиотеки pygame
                            sc = pygame.display.set_mode((1276,
                                                          724))  # заводим главный экран и определяем его размеры и загружаем его в переменную sc
                            # sc.fill((100, 150, 200))
                            field = pygame.image.load('RABOTA PERVAYA.jpg')  # подгрузка файла для фоновой заливки в переменную fild
                            background = field.get_rect(bottomright=(
                            1276, 724))  # вливаем размеры и разрешение файла фоновой заливки в переменную bakground
                            sc.blit(field, background)  # говорим показать
                            pygame.display.update()  # первый раз прорисовываем экран
                        if x > 46 and x < 421 and y > 111 and y < 261:  # это первый уровень субъекты федерации
                            f = 1  # метка первого уровня
                            pygame.init()  # вызов библиотеки pygame
                            sc = pygame.display.set_mode((1276,724))  # заводим главный экран и определяем его размеры и загружаем его в переменную sc
                            # sc.fill((100, 150, 200))
                            field = pygame.image.load('1 level.jpg')  # подгрузка файла для фоновой заливки в переменную fild
                            background = field.get_rect(bottomright=(
                            1276, 724))  # вливаем размеры и разрешение файла фоновой заливки в переменную bakground
                            sc.blit(field, background)  # говорим показать
                            pygame.display.update()  # первый раз прорисовываем экран
                        if x > 46 and x < 422 and y > 261 and y < 424:  # это второй уровень
                            f = 2
                            pygame.init()  # вызов библиотеки pygame
                            sc = pygame.display.set_mode((1276,724))  # заводим главный экран и определяем его размеры и загружаем его в переменную sc
                            # sc.fill((100, 150, 200))
                            field = pygame.image.load('2 level.jpg')  # подгрузка файла для фоновой заливки в переменную fild
                            background = field.get_rect(bottomright=(
                            1276, 724))  # вливаем размеры и разрешение файла фоновой заливки в переменную bakground
                            f2 = pygame.font.Font(None, 60)
                            sc.blit(field, background)  # говорим показать
                            pygame.display.update()  # первый раз прорисовываем экран
                        if x > 47 and x < 423 and y > 426 and y < 582:  # это третий уровень
                            f = 3
                            pygame.init()  # вызов библиотеки pygame
                            sc = pygame.display.set_mode((1276,724))  # заводим главный экран и определяем его размеры и загружаем его в переменную sc
                            # sc.fill((100, 150, 200))
                            field = pygame.image.load(
                                '3 level.jpg')  # подгрузка файла для фоновой заливки в переменную fild
                            background = field.get_rect(bottomright=(
                            1276, 724))  # вливаем размеры и разрешение файла фоновой заливки в переменную bakground
                            sc.blit(field, background)  # говорим показать
                            pygame.display.update()  # первый раз прорисовываем экран
                        if x > 125 and x < 354 and y > 611 and y < 707:
                            pygame.quit()
                            exit()
                        if x > 1004 and x < 1256 and y > 605 and y < 705 and f == 1:  # форма клика по региону
                            window1 = LevelFirst()
                            right = LevelFirst.RightAnsw
                        if x > 1004 and x < 1256 and y > 605 and y < 705 and f == 2:  # форма ответа на вопрос
                            window2 = LevelSECOND()
                            right = LevelSECOND.RightAnsw()
                        if x > 1004 and x < 1256 and y > 605 and y < 705 and f == 3:
                            pygame.init()  # вызов библиотеки pygame
                            sc = pygame.display.set_mode((1182,
                                                          770))  # заводим главный экран и определяем его размеры и загружаем его в переменную sc
                            # sc.fill((100, 150, 200))
                            field = pygame.image.load(
                                'ramka reka.png')  # подгрузка файла для фоновой заливки в переменную fild
                            background = field.get_rect(bottomright=(
                            1182, 770))  # вливаем размеры и разрешение файла фоновой заливки в переменную bakground
                            sc.blit(field, background)  # говорим показать
                            pygame.display.update()  # первый раз прорисовываем экран
        pygame.time.delay(20)
