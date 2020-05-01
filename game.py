import pygame

successes, failures = pygame.init()
print("{0} successes and {1} failures".format(successes, failures))

#define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#open window
screen = pygame.display.set_mode(700, 500)
pygame.display.set_caption("MarkPong")

#loop to keep the game moving
continueGame = True

#update interval
updat = pygame.time.Clock()

#---Main loop---
while continueGame:
    for event in pygame.event.get(): #actionEvent
        if event.type == pygame.QUIT:
            continueGame = False

    #---Main PLAY GAME Loop

    #clear screen to black
    screen.fill(BLACK)

    #draw net
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)

    #update screen
    pygame.display.flip()

    #30fps cap
    updat.tick(30)

pygame.quit #happens when continue = False