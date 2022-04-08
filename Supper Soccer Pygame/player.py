import pygame
# load all the image used for the soccer player gif in the main menu screen
im1 = pygame.image.load('sprite/tile000.png')
im1=pygame.transform.scale(im1,(680, 430))
im2 = pygame.image.load('sprite/tile001.png')
im2=pygame.transform.scale(im2,(680, 430))
im3 = pygame.image.load('sprite/tile002.png')
im3=pygame.transform.scale(im3,(680, 430))
im4 = pygame.image.load('sprite/tile003.png')
im4=pygame.transform.scale(im4,(680, 430))
im5 = pygame.image.load('sprite/tile004.png')
im5=pygame.transform.scale(im5,(680, 430))
im6 = pygame.image.load('sprite/tile005.png')
im6=pygame.transform.scale(im6,(680, 430))
im7 = pygame.image.load('sprite/tile006.png')
im7=pygame.transform.scale(im7,(680, 430))
im8 = pygame.image.load('sprite/tile007.png')
im8=pygame.transform.scale(im8,(680, 430))
im9 = pygame.image.load('sprite/tile008.png')
im9=pygame.transform.scale(im9,(680, 430))
im10 = pygame.image.load('sprite/tile009.png')
im10=pygame.transform.scale(im10,(680, 430))
class Player(pygame.sprite.Sprite):
    
	def __init__(self, pos_x, pos_y):
		super().__init__()
		self.attack_animation = False
		self.sprites = []
		self.sprites.append(im1)
		self.sprites.append(im2)
		self.sprites.append(im3)
		self.sprites.append(im4)
		self.sprites.append(im5)
		self.sprites.append(im6)
		self.sprites.append(im7)
		self.sprites.append(im8)
		self.sprites.append(im9)
		self.sprites.append(im10)
        
        
		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]

		self.rect = self.image.get_rect()
		self.rect.topleft = [pos_x,pos_y] #set the image position

	#start playing the gif
	def attack(self):
		self.attack_animation = True

	#check the gif state each frame
	def update(self,speed):
		if self.attack_animation == True:
			self.current_sprite += speed
			if int(self.current_sprite) >= len(self.sprites):
				self.current_sprite = 0
				self.attack_animation = False

		self.image = self.sprites[int(self.current_sprite)]