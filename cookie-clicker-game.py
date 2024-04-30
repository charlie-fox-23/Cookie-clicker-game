import pygame, sys

from pygame import image
from pygame.constants import MOUSEBUTTONDOWN

pygame.init()

class Cookie :
  def __init__(self,image_path,position):
    self.original_image = pygame.image.load(image_path)
    self.image = self.original_image.copy()
    self.rect = self.image.get_rect(center = position)
    self.click_count = 0
  def draw(self,screen):
    screen.blit(self.image,self.rect)

  def click(self):
    self.click_count +=1
    self.image = pygame.transform.scale(self.original_image,(110,110))
    self.rect = self.image.get_rect(center = self.rect.center)
    pygame.time.set_timer(pygame.USEREVENT,100)
  def reset_size(self):
    self.image = self.original_image.copy()
    self.rect = self.image.get_rect(center = self.rect.center)

screen_width = 640
screen_height = 480

screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
cookie = Cookie("cookie.png",(screen_width//2,screen_height//2))
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.MOUSEBUTTONDOWN and cookie.rect.collidepoint(event.pos):
      cookie.click()
    elif event.type == pygame.USEREVENT:
      cookie.reset_size()

  screen.fill((255,255,255))
  cookie.draw(screen)
  font = pygame.font.Font(None,36)
  text = font.render(str(cookie.click_count),True,(0,0,0))
  screen.blit(text,(screen_width//2-10,screen_height//2+60))
  pygame.display.flip()
  clock.tick(60)
pygame.quit()
sys.exit()