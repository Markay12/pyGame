import pygame

from random import randint

BLACK = (0, 0, 0)

class ball(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        #call parent class
        super().__init__()

        #color and backgrounds
        self.image = pygame.Surface([width, height]) #instance object
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        #draw rectange ball
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.velocity = [randint(4, 8), randint(-8, 8)] #choose random integers between these ranges

        #fetch object
        self.rect = self.image.get_rect()

        #---update function---

    def update(self):
            self.rect.x += self.velocity[0]
            self.rect.y += self.velocity[1]

    def bounce(self):
            self.velocity[0] = -self.velocity[0]
            self.velocity[1] = randint(-8, 8) #random direction