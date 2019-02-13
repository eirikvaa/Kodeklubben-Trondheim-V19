import pygame

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)

done = False

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

clock = pygame.time.Clock()

while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
  
  screen.fill(WHITE)
  pygame.display.flip()
  
  clock.tick(60)
  
pygame.quit()
  