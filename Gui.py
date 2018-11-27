import pygame
import sys
from pygame.locals import *
import numpy as np
from time import sleep

time_step = 0.1
escala = 5
CLICK_LEFT = 1
CLICK_RIGHT = 3
rows = 'ABCDEFGHI'
cols = '123456789'
peso = dict(zip(rows,cols))

color = np.zeros((20,3))
color[0]  = (255,255,255)	#blanco
color[1]  = (255,255,0)		#amarillo
color[2]  = (34,113,179)	#azul
color[3]  = (87,166,57)		#verde
color[4]  = (213,48,50)		#rojo
color[5]  = (99,58,52)		#cafe
color[6]  = (215,45,109)	#magenta
color[7]  = (255,117,20)	#naranja
color[8]  = (127,181,181)	#turquesa
color[9]  = (234,137,154)	#rosa
color[10] = (40,114,51)		#esmeralda
color[11] = (1,93,82)		#opalo
color[12] = (0,247,0)		#verde brillante
color[13] = (244,169,0)		#melon
color[14] = (71,64,46)		#oliva
color[15] = (37,109,123)	#agua
color[16] = (194,176,120)	#beige
color[17] = (110,28,52)		#brudeos
color[18] = (125,132,113)	#gris cemento
color[19] = (10,10,10)		#negro
cuadro_size = 70
ventana = pygame.display.set_mode((cuadro_size*9,cuadro_size*9))

class GUI:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Sudoku solver V0")
        ventana.fill(color[0])
        self.pintar_grilla()

    def cargar_sudoku(self,board):
        pygame.font.init()
        myfont = pygame.font.SysFont('arial', int(0.4 * cuadro_size))

        for x in range(9):
            for y in range(9):
                text = board[x][y]
                if text != 0:
                    textsurface = myfont.render(str(text), False, color[19])
                    ventana.blit(textsurface, ((cuadro_size * y) + 25, (cuadro_size * x) + 25))
        pygame.display.update()

    def step(self,grid):#A1 string 1-9
        ventana.fill(color[0])
        pygame.font.init()
        for row in rows:
            for col in cols:
                key = str(row) + str(col)#key = "A1"
                value = grid[key]
                if len(value) == 1:#esta asignada
                    texto = value
                    y = int(col)-1
                    x = int(peso[row])-1
                    myfont = pygame.font.SysFont('arial', int(0.4 * cuadro_size))
                    textsurface = myfont.render(texto, False, color[19])
                    ventana.blit(textsurface, ((cuadro_size * y) + 25, (cuadro_size * x) + 25))
                else: #muestra el dominio
                    texto = value
                    y = int(col) - 1
                    x = int(peso[row]) - 1
                    myfont = pygame.font.SysFont('arial', int(0.2 * cuadro_size))
                    textsurface = myfont.render(texto, False, color[7])
                    ventana.blit(textsurface, ((cuadro_size * y) + 0, (cuadro_size * x) + 0))
        self.pintar_grilla()
        sleep(time_step)

    def pintar_cuadro(self,x,y,num):
        pygame.draw.rect(ventana, color[num], (cuadro_size * x, cuadro_size * y, cuadro_size, cuadro_size))
        self.pintar_grilla()

    def pintar_grilla(self):
        for x in range(9):
            if (x == 2) or (x == 5):
                grosor = 5
            else:
                grosor = 1
            pygame.draw.line(ventana, color[19],(cuadro_size*(x+1),0),(cuadro_size*(x+1),cuadro_size*10),grosor)
        for x in range(9):
            if (x == 2) or (x == 5):
                grosor = 5
            else:
                grosor = 1
            pygame.draw.line(ventana, color[19],(0,cuadro_size*(x+1)),(cuadro_size*10,cuadro_size*(x+1)),grosor)
        pygame.display.update()

    def wait(self):
        while True:
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #if event.type == MOUSEBUTTONDOWN and event.button == CLICK_LEFT:
            pygame.display.update()
