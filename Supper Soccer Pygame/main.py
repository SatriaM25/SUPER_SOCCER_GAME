# reference : https://www.101computing.net/pong-tutorial-using-pygame-adding-a-scoring-system/
# Import the pygame library and initialise the game engine
import pygame,sys
from pygame import mixer
from paddle import Paddle
from ball import Ball
from arrow import Arrow
from button import Button
from player import Player
from endscreen import Endscreen
 
pygame.init()
 
# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255,1)
RED = (255,0,0)
ActivateMenu = [True]
ActivateWinMenu = [False]
winMessage = ""
# Open a new window
size = (630, 385)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Super Soccer")
a=pygame.image.load("assets/Logos.png")
pygame.display.set_icon(a)

#initialize arrow, ball, and paddle
arrowA = Arrow(180)
arrowB = Arrow(0)

paddleA = Paddle("PLeftRun.png","PLeftSlide.png","PLeftStun.png")
paddleA.rect.x = 15
paddleA.rect.y = 150
 
paddleB = Paddle("PRightRun.png","PRightSlide.png","PRightStun.png")
paddleB.rect.x = 550
paddleB.rect.y = 150
 
ball = Ball(20,20)
ball.rect.x = 305
ball.rect.y = 180

#Handle Screen
mainMenuAlreadyActive = False
winMenuAlreadyActive = False

#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()
 
# Add the 2 paddles and the ball to the list of objects
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)
all_sprites_list.add(arrowA)
all_sprites_list.add(arrowB)

# Sound Effects
goal = mixer.Sound("sound/goal.mp3")
kick = mixer.Sound("sound/kick.mp3")
whistleStart = mixer.Sound("sound/whistleStart.mp3")
whistleEnd = mixer.Sound("sound/whistleEnd.mp3")

# The loop will carry on until the user exits the game (e.g. clicks the close button).
carryOn = True
 
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#Initialise player scores
scoreA = 0
scoreB = 0
#set backgrounds
background=pygame.image.load("assets/field.jpg")
background=pygame.transform.scale(background,(700,450))

# Game Timer
clock = pygame.time.Clock()
counter, text2 = 60, '60'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)

# Background for main menu
BG = pygame.image.load("assets/Background.png")

#create group of sorites
#create group of sorites
moving_sprites = pygame.sprite.Group()
player = Player(-25,-23)
moving_sprites.add(player)


moving_sprites2 = pygame.sprite.Group()
endscreen = Endscreen(-16,-13)
moving_sprites2.add(endscreen)

#menu screen adder
tampilan1=pygame.image.load('Tampilan screen/3.png')
tampilan1=pygame.transform.scale(tampilan1,(600,390))

#last screen adder
tampilan2=pygame.image.load('Tampilan screen/4.png')
tampilan2=pygame.transform.scale(tampilan2,(630,395))

#change font
def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

#main menu page
def main_menu():
    while ActivateMenu[0]:
        screen.blit(BG, (0, 0))
        
        moving_sprites.draw(pygame.display.set_mode(size)) #draw the sprites to the screen
        player.attack() #start the main menu
        screen.blit(tampilan1,(30,0)) #set the screen image
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        
        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect2.png"), width =150, height = 40, pos=(310, 219),text_input="PLAY", font=get_font(22), base_color="#fafafa", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect2.png"), width =100, height = 25, pos=(70, 355),text_input="QUIT", font=get_font(15), base_color="#f51850", hovering_color="White")

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    ActivateMenu[0] = False
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        #update speed of sprites 
        moving_sprites.update(0.25)
        pygame.display.update()

#win menu page
def win_menu(message):
    while ActivateWinMenu[0]:
        screen.blit(BG, (0, 0))
        moving_sprites2.draw(pygame.display.set_mode(size))
        endscreen.attack()
        screen.blit(tampilan2,(0,5))

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        if message == "draw":
            MENU_TEXT = get_font(40).render("DRAW!!!", True, "#b68f40")
        else:
            MENU_TEXT = get_font(22).render("CONGRATULATION, PLAYER " + message + " WIN", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(310,160))
        
        PLAY_BUTTON = Button(image=pygame.image.load("assets/5.png"),width =230, height = 50, pos=(315, 340), text_input="Try Again", font=get_font(24), base_color="#000000", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    ActivateMenu[0] = True
                    ActivateWinMenu[0] = False
                
        #update speed of sprites 
        moving_sprites2.update(0.25)
        pygame.display.update()

#reset position of everything
def resetPos():
    paddleA.image = paddleA.originalImage
    paddleB.image = paddleB.originalImage
    paddleA.bringBall = False
    paddleB.bringBall = False
    paddleA.rect.x = 15
    paddleA.rect.y = 150
    paddleB.rect.x = 550
    paddleB.rect.y = 150
    paddleA.slidingTime = 60
    paddleA.dizzyTime = 120
    paddleA.isSliding = False
    paddleA.dizzy = False
    paddleB.slidingTime = 60
    paddleB.dizzyTime = 120
    paddleB.isSliding = False
    paddleB.dizzy = False
    ball.rect.x = 299
    ball.rect.y = 175
    ball.velocity = [0,0]

# -------- Main Program Loop -----------
while carryOn:
    if ActivateMenu[0]: #check if user proceed to main menu
        if not mainMenuAlreadyActive:
            mixer.music.stop()
            mixer.music.load("sound/mainmenu.mp3") #play background music for main menu
            mixer.music.play(-1)
            main_menu()
            mixer.Sound.play(whistleStart)
            mixer.music.load("sound/backgroundMusic.mp3")
            mixer.music.play(-1)
        mainMenuAlreadyActive = True
    if ActivateWinMenu[0]: #check if user proceed to end screen
        if not winMenuAlreadyActive:
            mixer.music.stop()
            mixer.music.load("sound/winning2.wav") #play background music for end screen
            mixer.music.play(-1)
            mixer.Sound.play(whistleEnd)
            win_menu(winMessage)
        winMenuAlreadyActive = True
        mainMenuAlreadyActive = False
    screen.fill(BLACK)
    screen.blit(background,(-35,-35))

    # Game Timer
    for e in pygame.event.get(): 
        if e.type == pygame.USEREVENT: #check if user is still playing
            counter -= 1
            if counter > 0:
                text2 = str(counter).rjust(3)
            else:
                if scoreA > scoreB:
                    winMessage = "1"
                elif scoreB > scoreA:
                    winMessage = "2"
                else:
                    winMessage = "draw"
                ActivateWinMenu[0] = True
                winMenuAlreadyActive = False
                counter, text2 = 10, '60'.rjust(3)
                resetPos()
                scoreA = 0
                scoreB = 0
        if e.type == pygame.QUIT: #check if user get out of the game
            carryOn = False
    
    # create goal line
    pygame.draw.rect(screen, WHITE, [0, 138, 10, 108])
    pygame.draw.rect(screen, WHITE, [620, 138, 10, 108])

    # check if player get out of the game
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we exit this loop
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: #Pressing the x Key will quit the game
                     carryOn=False

    #Check if player is allowed to move (player will not allowed to move if being slided by other player)
    if paddleA.dizzy:
        paddleA.dizzyAnimation() #play the dizzy animation
        paddleA.dizzyTime -= 1
        if paddleA.dizzyTime <= 0:
            paddleA.dizzy = False
            paddleA.dizzyTime = 120

    if paddleB.dizzy:
        paddleB.dizzyAnimation()
        paddleB.dizzyTime -= 1
        if paddleB.dizzyTime <= 0:
            paddleB.dizzy = False
            paddleB.dizzyTime = 120

    #Store previous position of player
    tempXplayerB = paddleB.prevX
    tempYplayerB = paddleB.prevY
    tempXplayerA = paddleA.prevX
    tempYplayerA = paddleA.prevY

    #Moving the paddles when the use uses the arrow keys (player A) or "W/S" keys (player B) 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)    
    
    if keys[pygame.K_a]:
        paddleA.moveLeft(5)
    if keys[pygame.K_d]:
        paddleA.moveRight(5)
    if keys[pygame.K_LEFT]:
        paddleB.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        paddleB.moveRight(5)  
    
    
    # --- Game logic should go here
    all_sprites_list.update()
    
    #Check if the ball is bouncing against any of the 4 walls, then make it bounce:
    if ball.rect.x>=595:
        if ball.rect.y >= 138 and ball.rect.y <= 246: #if the ball hit the goal line of player A, reset all pos
            scoreA+=1
            mixer.Sound.play(goal)
            resetPos()
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        if ball.rect.y >= 138 and ball.rect.y <= 246: # if the ball hit the goal line of player B, reset all pos
            scoreB+=1
            mixer.Sound.play(goal)
            resetPos()
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>360:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1] 
    
    #Detect if players slide each other
    if pygame.sprite.collide_mask(paddleA,paddleB):
        if paddleA.slidingTime != 60:
            if not paddleB.dizzy:
                paddleB.Dizzy()
        elif paddleB.slidingTime != 60:
            if not paddleA.dizzy:
                paddleA.Dizzy()

    #Detect collisions between the ball and the paddles
    if pygame.sprite.collide_mask(ball, paddleA) and paddleA.invulnerabilityTime == 0 and not paddleA.dizzy:
      if paddleA.isSliding:
          paddleA.isSliding = False
          paddleA.slidingTime = 60
          print("check")
          if paddleB.bringBall:
              print("ball is at player b")
              if not paddleB.dizzy:
                paddleB.Dizzy()
          else:
              print("ball is not at player b")
          paddleA.slidingAnimation(False)
      ball.sticky(paddleA.rect.x, paddleA.rect.y-10)
      paddleA.bringBall = True
      paddleB.bringBall = False
      arrowA.appear(paddleA.rect.x+50,paddleA.rect.y+40)
      arrowA.aim()
      if keys[pygame.K_SPACE]:
          paddleA.bringBall = False
          paddleA.invulnerable()
          ball.shoot(arrowA.curPos)
          mixer.Sound.play(kick)
    else:
      arrowA.transparent()
      if paddleA.isSliding:
          paddleA.moveSlide()
          paddleA.slidingAnimation(True)
          paddleA.slidingTime-=1
          if paddleA.slidingTime <= 0:
              paddleA.slidingTime = 60
              paddleA.isSliding = False
      else:
          if keys[pygame.K_LSHIFT] and paddleA.slidingTime > 0:
            paddleA.sliding()
            if tempXplayerA == paddleA.prevX:
                paddleA.prevX = paddleA.rect.x
            if tempYplayerA == paddleA.prevY:
                paddleA.prevY = paddleA.rect.y
      if paddleA.invulnerabilityTime > 0:
          paddleA.deductInvulnerable()
    
    if pygame.sprite.collide_mask(ball, paddleB) and paddleB.invulnerabilityTime == 0 and not paddleB.dizzy:
      if paddleB.isSliding:
          paddleB.isSliding = False
          paddleB.slidingTime = 60
          if pygame.sprite.collide_mask(ball, paddleA):
              if not paddleA.dizzy:
                paddleA.Dizzy()
          paddleB.slidingAnimation(False)
      paddleB.bringBall = True
      paddleA.bringBall = False
      ball.sticky(paddleB.rect.x-10, paddleB.rect.y-10)
      arrowB.appear(paddleB.rect.x-50,paddleB.rect.y+40)
      arrowB.aim()
      if keys[pygame.K_SPACE]:
          paddleB.bringBall = False
          paddleB.invulnerable()
          ball.shoot(arrowB.curPos)
          mixer.Sound.play(kick)
    else:
      arrowB.transparent()
      if paddleB.isSliding:
          paddleB.moveSlide()
          paddleB.slidingAnimation(True)
          paddleB.slidingTime-=1
          if paddleB.slidingTime <= 0:
              paddleB.slidingTime = 60
              paddleB.isSliding = False
      else:
          if keys[pygame.K_RSHIFT] and paddleB.slidingTime > 0:
            paddleB.sliding()
            if tempXplayerB == paddleB.prevX:
                paddleB.prevX = paddleB.rect.x
            if tempYplayerB == paddleB.prevY:
                paddleB.prevY = paddleB.rect.y
      if paddleB.invulnerabilityTime > 0:
          paddleB.deductInvulnerable()
      
    # --- Drawing code should go here

    #Now let's draw all the sprites in one go
    all_sprites_list.draw(screen) 
 
    #Display scores:
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (220,10))
    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (390,10))

    screen.blit(font.render(text2, True, (255, 0, 0)), (16, 8))
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

    
    
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()

