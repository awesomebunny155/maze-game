#-----------------------------------------------------------------------------
# Name:        Under the Sea Maze Game (escape_labyrinth.py)
# Purpose:     This maze game is designed to allow the user to play through a sample 
# maze under the ocean through the fish character. They will have the ability to
# move the object with the comfort of their keyboard buttons. Furthermore, the user
# has opportunities to replay the game several times in randomized starting locations.
# Author:      Harini Karthik
# Created:     8-March-2021
# Updated:     14-March-2021
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Import pygame which is the required library for this mazeGame game
import pygame
import random

# Define the Constants for colors beforehand using the format (red, green, blue)
LIGHT_BLUE = (159, 217, 255)    # Color is used for background (window)
DARK_BLUE = (14, 14, 246)       # Color is used for the bars of the mazeGame to stand out
LIGHT_GREEN=(0,210,0)
LIGHT_RED=(230,0,0)
GRAY = (127,127,127)
MOON_GLOW = (235,245,255)
BLACK = (0,0,0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


# Initialize the pygame library by calling the init function
pygame.init()

# Create the pygame window with 800 by 600 size 
window = pygame.display.set_mode((800, 600))

# Set the title and logo of the game
pygame.display.set_caption('Maze Game Under the Sea')

# Store the image for the icon in pygame icon and use set_icon for implementing it 
# Image Credit: Flaticon Motion and Speed Icon
pygameIcon = pygame.image.load('C:\\GitHub\\HaltonSchool\\maze-game-awesomebunny155\\Assets\\wave.png')
pygame.display.set_icon(pygameIcon)

# Play music throughout the game (Music Credit: Bensound)
gameMusic = pygame.mixer.Sound('C:\\GitHub\\HaltonSchool\\maze-game-awesomebunny155\\Assets\\bensoundLittleIdea.wav')
pygame.mixer.Sound.play(gameMusic)

# Create a class for the mazeGame bars 
class mazeGameBars(pygame.sprite.Sprite):   

    # pygame.sprite.Sprite was initialized to control the visible objects of the game    
    # Initialize a method that takes in values of the position, dimensions, and colors that the user would be able to control
    def __init__(self, xIn, yIn, length, height, color):
        # Use super to call the parent function
        super().__init__()
 
        # Makes the surface to the dimensions and colors
        self.image = pygame.Surface((length, height))
        self.image.fill(color)
 
        # Set the boundaries for the borders through self.rect
        self.rect = self.image.get_rect()       # Use get rect to change the image set up through surface into a rectangle
        self.rect.x = xIn
        self.rect.y = yIn
 
# Create the class for the runner object 
# Since this will be controlled by the user's choices of key GuiButtons, pygame.sprite.Sprite will have to be initialized 
class mazeGameObj(pygame.sprite.Sprite):
    # Initialize the current changes in position before defining the position function for the mazeGame obj
    changeXIn = 0
    changeYIn = 0
    # Define the initial function for the mazeObject image
    def __init__(self, xIn, yIn):
        # Use super to call the parent function
        super().__init__()  

        # Set the mazeGame object as the loaded image (Image Credit: DL PNG )
        self.image = pygame.image.load("C:\\GitHub\\HaltonSchool\\maze-game-awesomebunny155\\Assets\\fish_player.png").convert()
        # Image will be treated as a rectange wherin the x and y value positions will be set 
        self.rect = self.image.get_rect()
        self.rect.x = xIn
        self.rect.y = yIn 
    
    # Define the new location by changing the position of the mazeGame object
    def changePosition(self, xIn, yIn):
        # Key type will indicate the change in xIn or yIn
        self.changeXIn += xIn
        self.changeYIn += yIn
    
    # Define a method to animate the mazeGame object with the press of the keys 
    def animate(self, bars):
        
        # Moving left and right (x-values)
        self.rect.x += self.changeXIn       # The current x position is the change in x + current one 
        
        # Use sprite collide the sprite that intersects or collides with other sprites
        collisionDetect = pygame.sprite.spritecollide(self, bars, False)
        # Define the collision detection obstacle: if right side, then set as the opposite side (left)
        for block in collisionDetect:
            if self.changeXIn > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
        
 
        # Moving up and down (y-values)
        self.rect.y += self.changeYIn   # The current y position is the change in y + current one
        
        # Sprite collide feature was used to detect collision by setting the collided side as the opposite side
        # Rect value was used to determine the collision
        collisionDetect = pygame.sprite.spritecollide(self, bars, False)
        for block in collisionDetect:
 
            # When there is a change in y, then the opposite side will be set the detection
            if self.changeYIn > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
        


# Define the class for current maze
class mazeGame(object):

    # Sets the base class using object wherin there is no return
    barsCount = None

    # Define an initial function to create the lists later on by grouping  bars and objects sprites
    def __init__(self):
        self.barsCount = pygame.sprite.Group()
 
# Define a class for creating the actual maze game
class mazeGame1(mazeGame):
    def __init__(self):
        # Use super to call the parent function
        super().__init__()

        # Test and try the list of bars with the template 
        # Template: (xIn, yIn, length, width, color)
        bars = [[0, 0, 250, 20, DARK_BLUE],
                 [550, 0, 20, 250, DARK_BLUE],
                 [780, 0, 20, 250, DARK_BLUE],
                 [780, 200, 20, 300, DARK_BLUE],
                 [20, 0, 760, 20, DARK_BLUE],
                 [100, 480, 760, 20, DARK_BLUE],
                 [20, 580, 760, 20, DARK_BLUE],
                 [0, 0, 20, 900, DARK_BLUE],
                 [0, 200, 450, 20, DARK_BLUE],
                 [450, 200, 20, 170, DARK_BLUE],
                 [100, 370, 370, 20, DARK_BLUE],
                 [0, 300, 230, 20, DARK_BLUE]
                ]

        # Add each of the parameters into a list that will be incorporated in the final game
        for i in bars:
            barsOutline = mazeGameBars(i[0], i[1], i[2], i[3], i[4])
            self.barsCount.add(barsOutline)
 
# Use function for rendering the text
def GuiText(text, font):
    # Use font to return the text with the specified color
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

# Define a class for the GuiButtons
def GuiButton(msg,x,y,w,h,ic,ac,action=None):
    # When the GuiButton is clicked with a mouse, then it will be detected
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # When the first GuiButton start is clicked on, then it will take to the window
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(window, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            main() 
            return    
    # If the quit GuiButton is clicked, it will be closed    
    else:
        pygame.draw.rect(window, ic,(x,y,w,h))
        if click[0] == 1:
            pygame.quit()
            quit() 
            

    # Text specifications are defined here 
    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = GuiText(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    window.blit(textSurf, textRect)
    

# Function is defined for the introduction screen
def gameIntro():

    intro = True
    clock = pygame.time.Clock()
    
    # While the intro is still true, the screen will be there until quit is pressed
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        # Window UI is specified        
        window.fill(GRAY)
        largeText = pygame.font.SysFont("comicsansms",90)
        TextSurf, TextRect = GuiText("UnderSea Maze", largeText)
        TextRect.center = ((800/2),(600/2))
        window.blit(TextSurf, TextRect)
        

        # The GuiButton colors and sizes are specified
        GuiButton("READY!",150,450,100,50,GREEN,LIGHT_GREEN,'play')
        GuiButton("QUIT?",550,450,100,50,RED,LIGHT_RED,None)

        # Update the screen
        pygame.display.update()
        clock.tick(15)

# Define a screen for the ending of the gane
def gameEnd():

    # The conditions are set so that the screen is not maze game
    end = True
    clock = pygame.time.Clock()

    # Quit game when the GuiButton is clicked on
    while end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                

        # Window colors and font specifications are defined        
        window.fill(MOON_GLOW)
        largeText = pygame.font.SysFont("comicsansms",90)
        TextSurf, TextRect = GuiText("Play Again?", largeText)
        TextRect.center = ((800/2),(600/2))
        window.blit(TextSurf, TextRect)

        # GuiButtons are defined 
        GuiButton("YES",150,450,100,50,GREEN,LIGHT_GREEN,'play')
        GuiButton("NO",550,450,100,50,RED,LIGHT_RED,None)

        # Update the screen
        pygame.display.update()
        clock.tick(15)

# Main function for the entire game
def main():
  
    # The initial x and y positions are defined 
    mazeObject = mazeGameObj(random.randint(50,200), random.randint(50, 200)) # Randomness in the replayability of the game

    # Group the sprites to run it 
    animateSprite = pygame.sprite.Group()
    animateSprite.add(mazeObject)
    
    # Add the game to an empty array 
    windows = []
    
    # Append the maze game that was created into the empty array of windows
    gamesList = mazeGame1()
    windows.append(gamesList)
    
    # Count the number of games through this
    currentGameRepeater = 0
    gameRepeater = windows[currentGameRepeater]
 
    clock = pygame.time.Clock()
    
    # Since the game is not finished, it will go through the loop wherin the keypress will be valid
    completion = False
 
    while not completion:
        # Define the ending condition 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                completion = True
            
            # When the down or up key is clicked, then the event keys will be valid 2 units in specified directions
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    mazeObject.changePosition(-2, 0)
                elif event.key == pygame.K_RIGHT:
                    mazeObject.changePosition(2, 0)
                elif event.key == pygame.K_UP:
                    mazeObject.changePosition(0, -2)
                elif event.key == pygame.K_DOWN:
                    mazeObject.changePosition(0, 2)
 
        # Execute the key presses
        mazeObject.animate(gameRepeater.barsCount)
 
        # To end the game, the xs must be greater than 800 which is the length of the entire screen
        if mazeObject.rect.x > 800:
           gameEnd()
        
        # The background details are specified accordingly
        window.fill(LIGHT_BLUE)

        # The windows and game is drawn 
        animateSprite.draw(window)
        gameRepeater.barsCount.draw(window)
        
        # Update the full surface to screen 
        pygame.display.flip()
 
        clock.tick(45)
 
    pygame.quit()

# Driver function for the pygame
if __name__ == "__main__":
    gameIntro()
    