# Example file showing a basic pygame "game loop"
import pygame
import random


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

player = pygame.Rect(player_pos.x, player_pos.y, 30, 30)
bumpSpeed = 35
direction = pygame.Vector2(0, 1)
head_x = screen.get_width() / 2
head_y = screen.get_height() / 2

snake = []



def generateFood():
    return pygame.Rect(random.randint(0, screen.get_width()), random.randint(0, screen.get_height()), 30, 30)


# generate food for snake

food = pygame.Rect(random.randint(0, screen.get_width()), random.randint(0, screen.get_height()), 30, 30)
snake.append(player)



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE

    



    # snake.append(player)


    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        direction = pygame.Vector2(0, -1)
    if keys[pygame.K_s]:
        direction = pygame.Vector2(0, 1)
    if keys[pygame.K_a]:
        direction = pygame.Vector2(-1, 0)
    if keys[pygame.K_d]:
        direction = pygame.Vector2(1, 0)

    

    head_x = player.left + (direction.x*bumpSpeed)
    head_y = player.top + (direction.y*bumpSpeed)

    # player.move(player.left + (direction.x*bumpSpeed), player.top + (direction.y*bumpSpeed))
    if(head_x < 0 or head_x > 1280):
        break
    if(head_y < 0 or head_y > 720):
        break
    print(head_y)
    
    player = pygame.Rect(head_x, head_y, 30, 30)
    snake.insert(0, player)
    print(len(snake))
    snake.pop(len(snake)-1)
    print(len(snake))




    for r in snake:
        pygame.draw.rect(screen, 'white', r)
    
    if pygame.Rect.colliderect(food, snake[0]):
        print("eat")
        snake.append(player)
        food = generateFood()


    pygame.draw.rect(screen, 'white', food)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(15)  # limits FPS to 60

pygame.quit()


