# Example file showing a basic pygame "game loop"
import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# CONSTANTS
UP = pygame.Vector2(0, -1)
DOWN = pygame.Vector2(0, 1)
LEFT = pygame.Vector2(-1, 0)
RIGHT = pygame.Vector2(1, 0)

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

player = pygame.Rect(player_pos.x, player_pos.y, 30, 30)
bumpSpeed = 35
direction = pygame.Vector2(0, 1)
head_x = screen.get_width() / 2
head_y = screen.get_height() / 2

snake = []

def generateFood():
    return pygame.Rect(random.randint(0, screen.get_width()), random.randint(0, screen.get_height()), 30, 30)

food = pygame.Rect(random.randint(0, screen.get_width()), random.randint(0, screen.get_height()), 30, 30)
snake.append(player)

score=0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if(direction != DOWN):
            direction = UP
    if keys[pygame.K_s]:
        if(direction != UP):
            direction = DOWN
    if keys[pygame.K_a]:
        if(direction != RIGHT):
            direction = LEFT
    if keys[pygame.K_d]:
        if(direction != LEFT):
            direction = RIGHT

    head_x = player.left + (direction.x*bumpSpeed)
    head_y = player.top + (direction.y*bumpSpeed)

    if(head_x < 0 or head_x > 1280):
        break
    if(head_y < 0 or head_y > 720):
        break
    
    player = pygame.Rect(head_x, head_y, 30, 30)
    snake.insert(0, player)
    snake.pop(len(snake)-1)



    end = False
    for i, r in enumerate(snake):
        pygame.draw.rect(screen, 'white', r)
        if i != 0 and pygame.Rect.colliderect(r, snake[0]):
            print('gameover')
            end = True

    if end:
        break

    
    if pygame.Rect.colliderect(food, snake[0]):
        snake.append(player)
        food = generateFood()
        score = score + 1


    pygame.draw.rect(screen, 'white', food)

    pygame.display.flip()

    clock.tick(11)

print(score)

pygame.quit()


