import pygame

# load all the image used for the soccer player gif in the end screen
im1 = pygame.image.load('sprite/1.png')
im1=pygame.transform.scale(im1,(663, 410))
im2 = pygame.image.load('sprite/2.png')
im2=pygame.transform.scale(im2,(663, 410))
im3 = pygame.image.load('sprite/3.png')
im3=pygame.transform.scale(im3,(663, 410))
im4 = pygame.image.load('sprite/4.png')
im4=pygame.transform.scale(im4,(663, 410))
im5 = pygame.image.load('sprite/5.png')
im5=pygame.transform.scale(im5,(663, 410))
im6 = pygame.image.load('sprite/6.png')
im6=pygame.transform.scale(im6,(663, 410))
im7 = pygame.image.load('sprite/7.png')
im7=pygame.transform.scale(im7,(663, 410))
im8 = pygame.image.load('sprite/8.png')
im8=pygame.transform.scale(im8,(663, 410))
im9 = pygame.image.load('sprite/9.png')
im9=pygame.transform.scale(im9,(663, 410))
im10 = pygame.image.load('sprite/10.png')
im10=pygame.transform.scale(im10,(663, 410))

class Endscreen(pygame.sprite.Sprite):
    
    # initialization
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
		self.rect.topleft = [pos_x,pos_y] # set the position of gif 

	# start playing the gif
	def attack(self):
		self.attack_animation = True

	# check the gif state each frame
	def update(self,speed):
		if self.attack_animation == True:
			self.current_sprite += speed
			if int(self.current_sprite) >= len(self.sprites):
				self.current_sprite = 0
				self.attack_animation = False

		self.image = self.sprites[int(self.current_sprite)]