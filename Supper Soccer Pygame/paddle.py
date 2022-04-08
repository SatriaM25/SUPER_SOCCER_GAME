from turtle import pos
import pygame
from pygame import mixer
BLACK = (0,0,0)
 
class Paddle(pygame.sprite.Sprite):
    #This class represents a paddle. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, originalImage, slidingImage, dizzyImage):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.cheering = mixer.Sound("sound/cheering.wav")
        self.invulnerabilityTime = 0
        self.slidingTime = 60
        self.dizzyTime = 120
        self.isSliding = False
        self.dizzy = False
        self.bringBall = False

        #Set Images
        self.originalImage = pygame.image.load(f"assets/{originalImage}").convert_alpha()
        self.slidingImage = pygame.image.load(f"assets/{slidingImage}").convert_alpha()
        self.dizzyImage = pygame.image.load(f"assets/{dizzyImage}").convert_alpha()

        self.image = self.originalImage

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        self.prevX = self.rect.x
        self.prevY = self.rect.y
    
    # move the player one pixel to top 
    def moveUp(self, pixels):
      if not self.dizzy:
        if not self.isSliding:
          self.prevY = self.rect.y
          self.rect.y -= pixels
          #Check that you are not going too far (off the screen)
          if self.rect.y < 5:
            self.rect.y = 5
    # move the player one pixel to bottom    
    def moveDown(self, pixels):
      if not self.dizzy:
        if not self.isSliding:
          self.prevY = self.rect.y
          self.rect.y += pixels
          #Check that you are not going too far (off the screen)
          if self.rect.y > 320:
            self.rect.y = 320
    # move the player one pixel to right 
    def moveRight(self, pixels):
      if not self.dizzy:
        if not self.isSliding:
          self.prevX = self.rect.x
          self.rect.x += pixels
          #Check that you are not going too far (off the screen)
          if self.rect.x > 540:
            self.rect.x = 540
    # move the player one pixel to left
    def moveLeft(self, pixels):
      if not self.dizzy:
        if not self.isSliding:
          self.prevX = self.rect.x
          self.rect.x -= pixels
          #Check that you are not going too far (off the screen)
          if self.rect.x < 27:
            self.rect.x = 27
    
    def invulnerable(self):
        self.invulnerabilityTime = 10
    
    def deductInvulnerable(self):
        self.invulnerabilityTime -= 1
        if self.invulnerabilityTime < 0.1:
          self.invulnerabilityTime = 0
    
    def sliding(self):
        self.isSliding = True
        
    def moveSlide(self):
      if self.rect.x > self.prevX:
          self.rect.x+=3
      elif self.rect.x < self.prevX:
        self.rect.x-=3
      if self.rect.y > self.prevY:
          self.rect.y+=3
      elif self.rect.y < self.prevY:
        self.rect.y-=3
    
    def slidingAnimation(self, play):
      if play:
        if self.slidingTime > 1 and self.isSliding:
          self.image = self.slidingImage
        else:
          self.image = self.originalImage
      else:
          self.image = self.originalImage

    def Dizzy(self):
      self.dizzy = True
      mixer.Sound.play(self.cheering)

    def dizzyAnimation(self):
      if self.dizzyTime > 1:
        self.image = self.dizzyImage
      else:
          self.image = self.originalImage