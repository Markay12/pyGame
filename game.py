import pygame

successes, failures = pygame.init()
print("{0} successes and {1} failures".format(successes, failures))

game = pygame.display.set_mode((600, 400))

pygame.display.set_caption("My First Game")

input("press ENTER to exit application\n")