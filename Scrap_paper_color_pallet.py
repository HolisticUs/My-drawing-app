import pygame
import sys

# Initialize Pygame
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
#set up display
screen_width = 800
iw = screen_width / 10 
screen_width_in_game_unit = screen_width / iw
screen_height = 600
ih = screen_height / 10
screen_height_in_game_unit = screen_height / ih 
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('Drawing Pad')
# Set up components
framecount = 0

class Button:
     def __init__(self, x, y, width=100, height=70, text='Untitled Button', text_size=30, color=(255, 0, 0), text_color=(255,255,255), boarder1=(255,255,255), boarder2=(255,0,0)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text_color = text_color
        self.boarder1 = boarder1
        self.boarder2 = boarder2
        self.text = text
        self.text_size = text_size

     def draw(self, screen=screen):
        boarder = self.boarder1
        if event.type == pygame.MOUSEMOTION:
            if self.is_over(event.pos):
                boarder = self.boarder2

        back_rect = pygame.Rect(self.x-(self.width/20), self.y-(self.height/20), self.width*1.1, self.height*1.1)
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, boarder, back_rect)
        pygame.draw.rect(screen, self.color, rect)
        button_font = pygame.font.SysFont('Comic Sans MS', self.text_size)
        button_text = button_font.render(self.text, True, self.text_color)
        text_rect = button_text.get_rect(center=(self.x + self.width/2, self.y + self.height/2))
        screen.blit(button_text, text_rect)
              
     def is_over(self, pos):
          return pygame.Rect(self.x-(self.width/20), self.y-(self.height/20), self.width*1.1, self.height*1.1).collidepoint(pos)
     
color_dict = {}

sample_button = Button(200, 200, 10, 10,None, 0,(150,150,150))

# Set up the clock for controlling the frame rate
clock = pygame.time.Clock()
# Main game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Game logic update
    text_surface = my_font.render(str(framecount), False, (255,255,255))
    # (update your game state here)
    # Rendering
    
    screen.fill((0, 0, 0)) # Clear screen with black
    screen.blit(text_surface, (0,0))
    sample_button.draw()
    framecount += 1
    # (draw your game elements here)
    pygame.display.flip() # Update the display
    # Control the frame rate
    clock.tick(60) # 60 frames per second