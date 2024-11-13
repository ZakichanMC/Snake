import pygame
import random

pygame.init()

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (24, 99, 44)
LIME = (97, 207, 106)

#window display
SCREEN = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

#the snake variables
snakePos = [300, 150]
snakeBody = [[300, 150], [310, 150], [320, 150], [330, 150]]
direction = "left"
changeTo = direction


#apples
class Apple(pygame.sprite.Sprite):

  def __init__(self, color, width, height):
    super().__init__()

    self.image = pygame.Surface([width, height])
    self.image.fill(LIME)
    self.image.set_colorkey(LIME)

    #draw the apple
    pygame.draw.rect(self.image, color, [0, 0, width, height])

    #get the object
    self.rect = self.image.get_rect()

  #to "spawn" "new" wink wink nudge nudge
  def spawn(self):
    apple.rect.x = (random.randint(1, 39) * 10)
    apple.rect.y = (random.randint(6, 29) * 10)


#initializing the apple when the game starts
apple = Apple(RED, 10, 10)
spritesList = pygame.sprite.Group()
spritesList.add(apple)
apple.spawn()
score = 0

#the main game loop
run = True
while run:
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_w or event.key == pygame.K_UP:
        changeTo = "up"
      if event.key == pygame.K_s or event.key == pygame.K_DOWN:
        changeTo = "down"
      if event.key == pygame.K_a or event.key == pygame.K_LEFT:
        changeTo = "left"
      if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
        changeTo = "right"
    if event.type == pygame.QUIT:
      run = False

  #to prevent from going backwards in on itself
  if changeTo == "up" and direction != "down":
    direction = "up"
  if changeTo == "down" and direction != "up":
    direction = "down"
  if changeTo == "left" and direction != "right":
    direction = "left"
  if changeTo == "right" and direction != "left":
    direction = "right"

  # Moving the snake
  if direction == "up":
    snakePos[1] -= 10
  if direction == "down":
    snakePos[1] += 10
  if direction == "left":
    snakePos[0] -= 10
  if direction == "right":
    snakePos[0] += 10

  #to add the current position of the snake to the snakeBody
  snakeBody.insert(0, list(snakePos))
  spritesList.update()

  #to check if colliding with apple
  if snakePos[0] == apple.rect.x and snakePos[1] == apple.rect.y:
    apple.spawn()
    score += 1
  else:
    snakeBody.pop()

  SCREEN.fill(LIME)

  #to draw each rect for each pos in snakebody
  for pos in snakeBody:
    pygame.draw.rect(SCREEN, GREEN, (pos[0], pos[1], 10, 10))

  #to draw the game
  pygame.draw.line(SCREEN, BLACK, [0, 50], [400, 50], 10)
  spritesList.draw(SCREEN)

  #display the scores
  font = pygame.font.Font(None, 50)
  text = font.render(str(score), 1, BLACK)
  SCREEN.blit(text, (200, 10))

  #if the snake goes offscreen
  def offscreen():
    global snakeBody
    apple.kill()
    snakeBody = []
    text = font.render("Game Over", 1, BLACK)
    SCREEN.blit(text, (100, 100))

  #if the snake hits itself
  for block in snakeBody[1:]:
    if block[0] < 0 or block[0] > 400 or block[1] < 50 or block[1] > 300:
      offscreen()
    if snakePos[0] == block[0] and snakePos[1] == block[1]:
      offscreen()
    if apple.rect.x == block[0] and apple.rect.y == block[1]:
      apple.spawn()

  pygame.display.update()

  clock.tick(10)