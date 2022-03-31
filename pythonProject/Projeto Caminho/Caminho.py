import pygame
import math
from queue import PriorityQueue

LARGURA = 800
JAN = pygame.display.set_mode((LARGURA, LARGURA))
pygame.display.set_caption("Algoritmo de Caminho")

VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 255, 0)
AMARELO = (155, 155, 0)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
ROXO = (128, 0, 128)
LARANJA = (255, 165, 0)
CINZA = (128, 128, 128)
TURQUESA = (64, 224, 208)


class Node:
    def __init__(self, fileira, col, largura, total_fileiras):
        self.fileira = fileira
        self.col = col
        self.x = fileira * largura
        self.y = col * largura
        self.cor = BRANCO
        self.vizihnos = []
        self.largura = largura
        self.total_fileira = total_fileiras

    def get_pos(self):
        return self.fileira, self.col

    def bloqueado(self):
        return self.cor == VERMELHO

    def aberto(self):
        return self.cor == VERDE

    def barrerira(self):
        return self.cor == PRETO

    def comeco(self):
        return self.cor == LARANJA

    def fim(self):
        return self.cor == TURQUESA

    def resetar(self):
        self.cor == BRANCO

    def fazer_fechado(self):
        self.cor = VERMELHO

    def fazer_aberto(self):
        self.cor = VERDE

    def fazer_barreira(self):
        self.cor = PRETO

    def fazer_fim(self):
        self.cor = TURQUESA

    def fazer_caminho(self):
        self.cor = ROXO

    def desenho(self, JAN):
        pygame.draw.rect( JAN, self.cor, (self.x, self.y, self.largura, self.largura))

    def vizinho_update(self, grid):
        pass

    def __lt__(self, other):
        return False

# Definição Heuristica
# Distância "Manhattan/Taxi Cab"


def h(p1, p2):
    x1, x2 = p1
    y1, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def fazer_grade(fileira, largura):
    grade = []
    vao = largura // fileira
    for i in range(fileira):
        grade.append([])
        for j in range(fileira):
            node = Node(i, j, vao, fileira)
            grade[i].append(node)

    return grade

def desenhar_grade(JAN, fileira, largura):
    vao = largura // fileira
    for i in range(fileira):
        pygame.draw.line(JAN, CINZA, (0, i * vao), (largura, i *vao))
        for j in range(fileira):
            pygame.draw.line(JAN, CINZA, (j * vao, 0), (j * vao, largura))
