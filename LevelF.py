import pygame
import random
from  dic import *
RED = (225, 0, 50)
BLACK=(0,0,0)
class LevelFirst():
    def __init__(self):
        self.b=True
        self.k=1
        self.p=0
        while self.b:  # заводим бесконечный цикл
            for self.i in pygame.event.get():
                if self.i.type == pygame.QUIT:  # нажимаем кнопку закрытия экрана
                    pygame.time.delay(20)
                if self.i.type == pygame.MOUSEBUTTONDOWN:  # нажимаем что-нибудь на мыши
                    if self.i.button == 1:  # клик ЛКМ
                       pygame.init()  # вызов библиотеки pygame
                       self.sc = pygame.display.set_mode((1128,729))  # заводим главный экран и определяем его размеры и загружаем его в переменную sc
                       self.field = pygame.image.load('ramka rf.png')  # подгрузка файла для фоновой заливки в переменную fild
                       self.background = self.field.get_rect(bottomright=(1128, 729))  # вливаем размеры и разрешение файла фоновой заливки в переменную bakground
                       pygame.display.update()
                       self.x1 = 0
                       self.y1 = 0
                       self.f2 = pygame.font.Font(None, 35)
                       self.n = random.randint(0, 80)
                       self.question = 'Вопрос номер ' + str(self.k) + ' Покажите, где находится - ' + objec[self.n]
                       self.text2 = self.f2.render(self.question, 1, (0, 0, 0))
                       self.sc.blit(self.field, self.background)  # говорим показать
                       self.sc.blit(self.text2, (70, 56))
                       self.x1 = self.i.pos[0]
                       self.y1 = self.i.pos[1]
                       pygame.draw.circle(self.sc, BLACK, self.i.pos, 5)
                       if self.x1 > correctsubject_py[objec[self.n]][0] \
                               and self.x1 < correctsubject_py[objec[self.n]][2] \
                               and self.y1 > correctsubject_py[objec[self.n]][1] \
                               and self.y1 < correctsubject_py[objec[self.n]][3]:
                           self.p=self.p+1
                       pygame.display.update()
                       self.k = self.k + 1
                       if self.k == 16: self.b=False
    def RightAnsw(self):
        return self.p