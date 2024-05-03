import pygame, sys

from pygame import image
from pygame.constants import MOUSEBUTTONDOWN

pygame.init()

class Upgrade :
  def __init__(self,image_path,position,cost):
    self.image = pygame.image.load(image_path)
    self.image = pygame.transform.scale(self.image,(50,50))
    self.rect = self.image.get_rect(topleft = position)
    self.cost = cost
  def draw(self,screen):
    screen.blit(self.image,self.rect)
  def is_affordable(self,clicks):
    return clicks >= self.cost
  def purchase(self,cookie):
    if cookie.click_count >= self.cost :
      cookie.click_count -= self.cost
      return True 
    return False

class Cookie :
  def __init__(self,image_path,position,initial_size=(100,100)):
    self.original_image = pygame.image.load(image_path)
    self.original_image = pygame.transform.scale(self.original_image,initial_size)
    self.image = self.original_image.copy()
    self.rect = self.image.get_rect(center = position)
    self.click_count = 0
  def draw(self,screen):
    screen.blit(self.image,self.rect)

  def click(self):
    self.click_count +=1
    self.image = pygame.transform.scale(self.original_image,(110,110))
    self.rect = self.image.get_rect(center = self.rect.center)
    pygame.time.set_timer(pygame.USEREVENT,200)
  def reset_size(self):
    self.image = self.original_image.copy()
    self.rect = self.image.get_rect(center = self.rect.center)

screen_width = 640
screen_height = 480

background_image = pygame.image.load("background.png")
background_image = pygame.transform.scale(background_image,(screen_width,screen_height))

screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
cookie = Cookie("cookie.png",(screen_width//5,screen_height//2))
upgrade = Upgrade("mouse_cursor.png",(screen_width//2,screen_height//10),16)
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.MOUSEBUTTONDOWN: #and cookie.rect.collidepoint(event.pos):
      if cookie.rect.collidepoint(event.pos):
        cookie.click()
      elif upgrade.rect.collidepoint(event.pos) and upgrade.is_affordable(cookie.click_count):
        if upgrade.purchase(cookie):
          print ("Upgrade purchased")
          
    elif event.type == pygame.USEREVENT:
      cookie.reset_size()
  screen.blit(background_image,(0,0))
  cookie.draw(screen)
  upgrade.draw(screen)
  font = pygame.font.Font(None,36)
  text = font.render(str(cookie.click_count),True,(0,0,0))
  screen.blit(text,(screen_width//5-10,screen_height//2+60))
  if upgrade.is_affordable(cookie.click_count):
    upgrade_text = font.render("Click to buy",True,(0,128,0))
  else:
    upgrade_text = font.render(f"Cursor {upgrade.cost} cookies.",True,(255,0,0))
  screen.blit(upgrade_text,(screen_width//2+60,screen_height//10))
  pygame.display.flip()
  clock.tick(60)
pygame.quit()