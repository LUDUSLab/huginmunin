import pygame
from flask import Flask
import threading

app = Flask(__name__)

SIZE = WIDTH, HEIGHT = 480, 320 #the width and height of our screen
BACKGROUND_COLOR = pygame.Color('white') #The background colod of our window
FPS = 20 #Frames per second

class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()
        #adding all the images to sprite array
        self.animation = []
        self.idle = []  
        self.idle.append(pygame.image.load('Sprites/01 - Iddle/10001.png'))
        self.idle.append(pygame.image.load('Sprites/01 - Iddle/10002.png'))
        self.idle.append(pygame.image.load('Sprites/01 - Iddle/10003.png'))
        self.idle.append(pygame.image.load('Sprites/01 - Iddle/10004.png'))
        self.idle.append(pygame.image.load('Sprites/01 - Iddle/10005.png'))
        self.idle.append(pygame.image.load('Sprites/01 - Iddle/10006.png'))
        self.idle.append(pygame.image.load('Sprites/01 - Iddle/10007.png'))
        self.idle.append(pygame.image.load('Sprites/01 - Iddle/10008.png'))
        self.idle.append(pygame.image.load('Sprites/01 - Iddle/10009.png'))      
        self.blink = []
        self.blink.append(pygame.image.load('Sprites/03 - flashing and loocking E/10015.png'))
        self.blink.append(pygame.image.load('Sprites/03 - flashing and loocking E/10016.png'))
        self.blink.append(pygame.image.load('Sprites/03 - flashing and loocking E/10017.png'))
        self.blink.append(pygame.image.load('Sprites/03 - flashing and loocking E/10018.png'))
        self.blink.append(pygame.image.load('Sprites/03 - flashing and loocking E/10019.png'))
        self.blink.append(pygame.image.load('Sprites/03 - flashing and loocking E/10015.png'))
        self.blink.append(pygame.image.load('Sprites/03 - flashing and loocking E/10016.png'))
        self.blink.append(pygame.image.load('Sprites/03 - flashing and loocking E/10017.png'))
        self.blink.append(pygame.image.load('Sprites/03 - flashing and loocking E/10018.png'))
        self.blink.append(pygame.image.load('Sprites/03 - flashing and loocking E/10019.png'))
        self.animation = self.idle
        #index value to get the image from the array
        #initially it is 0 
        self.index = 0
        #now the image that we will display will be the index from the image array 
        self.image = self.animation[self.index]
        #creating a rect at position x,y (5,5) of size (150,198) which is the size of sprite 
        self.rect = pygame.Rect(0, 0, 480, 320)

    def changeAnimation(self):
        self.animation = self.blink
        self.index = 0
        

    def update(self):        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RETURN]:
            self.changeAnimation() 

        #when the update method is called, we will increment the index
        self.index += 1

        #if the index is larger than the total images
        if self.index >= len(self.animation):
            #we will make the index to 0 again
            self.animation = self.idle
            self.index = 0
        
        #finally we will update the image that will be displayed
        self.image = self.animation[self.index]

#creating our sprite object
my_sprite = MySprite()
def main():
    #initializing pygame
    pygame.init()
    #getting the screen of the specified size
    screen = pygame.display.set_mode(SIZE)
    #creating a group with our sprite
    my_group = pygame.sprite.Group(my_sprite)
    #getting the pygame clock for handling fps
    clock = pygame.time.Clock()

    while True:
        #if the event is quit means we clicked on the close window button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #quit the game
                pygame.quit()
                quit()

        #updating the sprite
        my_group.update()

        #filling the screen with background color
        screen.fill(BACKGROUND_COLOR)

        #drawing the sprite
        my_group.draw(screen)

        #updating the display
        pygame.display.update()

        #finally delaying the loop to with clock tick for 10fps 
        clock.tick(10)

@app.route("/blink")
def hello():
    my_sprite.changeAnimation()
    return 'Blink'

def flask_run():
    app.run(host='0.0.0.0', port='5000', debug=False)

if __name__ == '__main__':
    thread = threading.Thread(target=flask_run)
    thread.start()
    main()
