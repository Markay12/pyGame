import pygame
from paddle import paddle
from ball import ball

successes, failures = pygame.init()
print("{0} successes and {1} failures".format(successes, failures))

#define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#open window
screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("MarkPong")

#implementation of paddles
leftPaddle = paddle(WHITE, 10, 100)
leftPaddle.rect.x = 20
leftPaddle.rect.y = 200

rightPaddle = paddle(WHITE, 10, 100)
rightPaddle.rect.x = 670
rightPaddle.rect.y = 200

#create and add ball sprite
ball = ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

#list that contains all of the sprites
sprites_list = pygame.sprite.Group()

#add paddles to list
sprites_list.add(leftPaddle)
sprites_list.add(rightPaddle)
sprites_list.add(ball)

#loop to keep the game moving
continueGame = True

#update interval
updat = pygame.time.Clock()

#init player scores
scoreA = 0
scoreB = 0

#---Main loop---
while continueGame:
    for event in pygame.event.get(): #actionEvent
        if event.type == pygame.QUIT:
            continueGame = False
        elif event.type == pygame.KEYDOWN:
            #press ESCAPE to QUIT
            if event.key == pygame.K_ESCAPE:
                continueGame = False;

    #---Main PLAY GAME Loop

    #move paddles via key
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        leftPaddle.moveUp(5)
    if keys[pygame.K_s]:
        leftPaddle.moveDown(5)
    if keys[pygame.K_UP]:
        rightPaddle.moveUp(5)
    if keys[pygame.K_DOWN]:
        rightPaddle.moveDown(5)

    #Game logic
    sprites_list.update() 

    #check ball boundaries
    if ball.rect.x >= 690:
        scoreA += 1 #update score
        ball.velocity[0] = -ball.velocity[0] #change direction
    if ball.rect.x <=0:
        scoreB += 1 #update score
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y > 490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]


    #detect collisions
    if pygame.sprite.collide_mask(ball, leftPaddle) or pygame.sprite.collide_mask(ball, rightPaddle):
        ball.bounce()

       

    #clear screen to black
    screen.fill(BLACK)

    #draw net
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)

    #update all sprites
    sprites_list.draw(screen)

    #Displaye scores
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (250, 10))
    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (420, 10))


    #update screen
    pygame.display.flip()

    #30fps cap
    updat.tick(30)



pygame.quit #happens when continue = False