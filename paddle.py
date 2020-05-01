import pygame

BLACK = (0, 0, 0)

class paddle(pygame.sprite.Sprite):
    #class for paddle using Sprite

    def __init__(self, color, width, height):
        super().__init__()

        #init color, pos and size
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        #draw paddle (rectangle)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        #fetch object
        self.rect = self.image.get_rect()

    #---BOUND FUNCTIONS---

    def moveUp(self, pixels):
        self.rect.y -= pixels

        if self.rect.y < 0:
            self.rect.y = 0

    def moveDown(self, pixels):
        self.rect.y += pixels

        if self.rect.y > 400:
            self.rect.y = 400