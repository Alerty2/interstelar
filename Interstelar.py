import pygame
import sys
import random
import time

class Nave(pygame.sprite.Sprite):
    def __init__(self,imagen):
        super().__init__()
        self.image = pygame.image.load(imagen)
        self.rect = self.image.get_rect()

class Fondo(pygame.sprite.Sprite):
    def __init__(self, imagen):
        super().__init__()
        self.image = pygame.image.load(imagen)
        self.rect = self.image.get_rect()
class Asteroide(pygame.sprite.Sprite):
    def __init__(self, imagen):
        super().__init__()
        self.image = pygame.image.load(imagen)
        self.rect = self.image.get_rect()


    def update(self):
        pass

nave = Nave("data/images/nave.png")
cielo = Fondo("data/images/cielo.jpg")

meteorito = Asteroide("data/images/asteroide.png")
meteorito_2 = Asteroide("data/images/asteroide.png")
meteorito_3 = Asteroide("data/images/asteroide.png")
meteorito_4 = Asteroide("data/images/asteroide.png")
meteorito_5 = Asteroide("data/images/asteroide.png")
meteorito_6 = Asteroide("data/images/asteroide.png")
meteorito_7 = Asteroide("data/images/asteroide.png")
meteorito_8 = Asteroide("data/images/asteroide.png")

meteorito.rect.y = -8
def go():
    meteorito.rect.y = -8
    meteorito_2.rect.y = -8
    meteorito_3.rect.y = -8
    meteorito_4.rect.y = -8
    meteorito_5.rect.y = -8
    meteorito_6.rect.y = -8
    meteorito_7.rect.y = -8
    meteorito_8.rect.y = -8
    if random.randint(0, 2) == 1:
        meteorito.rect.x = random.randrange(0, 1000)
    if random.randint(0, 2) == 1:
        meteorito_2.rect.x = random.randrange(0, 1000)
    if random.randint(0, 2) == 1:
        meteorito_3.rect.x = random.randrange(0, 1000)
    if random.randint(0, 2) == 1:
        meteorito_4.rect.x = random.randrange(0, 1000)
    if random.randint(0, 2) == 1:
        meteorito_5.rect.x = random.randrange(0, 1000)
    if random.randint(0, 2) == 1:
        meteorito_6.rect.x = random.randrange(0, 1000)
    if random.randint(0, 2) == 1:
        meteorito_7.rect.x = random.randrange(0, 1000)
    if random.randint(0, 2) == 1:
        meteorito_8.rect.x = random.randrange(0, 1000)

fondos = pygame.sprite.Group()
cap_1 = pygame.sprite.Group()

cap_1.add(nave)
nave.rect.x = 400
nave.rect.y = 500

fondos.add(cielo)

cap_1.add(meteorito)
cap_1.add(meteorito_2)
cap_1.add(meteorito_3)
cap_1.add(meteorito_4)
cap_1.add(meteorito_5)
cap_1.add(meteorito_6)
cap_1.add(meteorito_7)
cap_1.add(meteorito_8)

pygame.init()
PANTALLA = pygame.display.set_mode((1000,600))
pygame.display.set_caption('Naves')
icono = pygame.image.load("data/images/asteroide.png")
pygame.display.set_icon(icono)

reloj = pygame.time.Clock()
BLANCO = 255, 255, 255
NEGRO = 0, 0, 0
ROJO = 255, 0, 0
AZUL = 0, 0, 255
VERDE = 0, 255, 0
AMARILLO = 255, 255, 0
HIERBAC = 70, 87, 23
NOCHEC = 0, 0 , 102

def game_over():
    fuente = pygame.font.Font(None, 60)
    over = fuente.render("Te has estrellado", 0, (215, 25, 206))
    PANTALLA.fill(NEGRO)
    cap_1.remove(nave)
    cap_1.remove(meteorito)
    cap_1.remove(meteorito_2)
    cap_1.remove(meteorito_3)
    cap_1.remove(meteorito_4)
    cap_1.remove(meteorito_5)
    cap_1.remove(meteorito_6)
    cap_1.remove(meteorito_7)
    cap_1.remove(meteorito_8)
    fondos.remove(cielo)
    PANTALLA.blit(over,(350,300))


PANTALLA.fill(NOCHEC)
go()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_LEFT]:
        nave.rect.move_ip(-10, 0)

    elif key_pressed[pygame.K_RIGHT]:
        nave.rect.move_ip(10, 0)

    if pygame.sprite.collide_mask(nave,meteorito):
        game_over()
    if pygame.sprite.collide_mask(nave,meteorito_2):
        game_over()
    if pygame.sprite.collide_mask(nave,meteorito_3):
        game_over()
    if pygame.sprite.collide_mask(nave,meteorito_4):
        game_over()
    if pygame.sprite.collide_mask(nave,meteorito_5):
        game_over()
    if pygame.sprite.collide_mask(nave,meteorito_6):
        game_over()
    if pygame.sprite.collide_mask(nave,meteorito_7):
        game_over()
    if pygame.sprite.collide_mask(nave,meteorito_8):
        game_over()

    meteorito.rect.move_ip(0,10)
    meteorito_2.rect.move_ip(0,10)
    meteorito_3.rect.move_ip(0,10)
    meteorito_4.rect.move_ip(0,10)
    meteorito_5.rect.move_ip(0,10)
    meteorito_6.rect.move_ip(0,10)
    meteorito_7.rect.move_ip(0,10)
    meteorito_8.rect.move_ip(0,10)
    if meteorito.rect.y > 600:
        go()



    pygame.display.flip()
    fondos.draw(PANTALLA)
    cap_1.draw(PANTALLA)
    reloj.tick(60)