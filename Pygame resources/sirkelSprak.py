import pygame
import random

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)

done = False

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

colors = [BLACK, GREEN, RED]

# Returnerer en tilfeldig posisjon
def randomPosition():
  x = random.randint(50, 650)
  y = random.randint(50, 450)
  return (x, y)

# Returnerer en tilfeldig farge
def randomColor():
  return random.choice(colors)
  
# Tegner sirkelen
def drawCircle(radius):
  # Setter en tilfeldig posisjon
  position = randomPosition()
  # Henter en tilfeldig farge
  color = randomColor()
  
  pygame.draw.circle(screen, color, position, radius)

clock = pygame.time.Clock()
screen.fill(WHITE)

# Tegner x-antall sirkler
for i in range(100):
  drawCircle(20)

while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True

  pygame.display.flip()
  
  clock.tick(60)
  
pygame.quit()
  