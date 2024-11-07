import pygame
import sys
import os
import datetime
import tkinter as tk
from tkinter import filedialog
import math

# Initialize Pygame
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
#set up display
screen_width = 900
iw = screen_width / 10 
screen_width_in_game_unit = screen_width / iw
screen_height = 600
ih = screen_height / 10
screen_height_in_game_unit = screen_height / ih 
screen = pygame.display.set_mode((screen_width, screen_height))
pad_right_edge = 500
pad_bottom_edge = 500
pad_left_edge = 10
pad_top_edge = 10
drawing_pad = pygame.Rect(pad_left_edge, pad_top_edge, pad_right_edge, pad_bottom_edge)
pygame.display.set_caption('Drawing Pad')
# Set up components
framecount = 0
button_clicked = False
draw_tile_ready = False
dict_of_tiles = {}
color_picked = (255,0,255)
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

# Initialize Tkinter
root = tk.Tk()
root.withdraw() # Hides the main tkinter window

loaded_image = None

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
     
draw_tile_button = Button(screen_width-150, screen_height-70, 120, 50, 'Draw')
red_color_button = Button(screen_width-150, screen_height-140, 120, 50, 'RED')
green_color_button = Button(screen_width-150, screen_height-210, 120, 50, 'GREEN')
blue_color_button = Button(screen_width-150, screen_height-280, 120, 50, 'BLUE')
erase_button = Button(screen_width-290, screen_height-70, 120, 50, 'ERASER')
yellow_color_button = Button(screen_width-150, screen_height-350, 120, 50, 'YELLOW')
brown_color_button = Button(screen_width-150, screen_height-420, 120, 50, 'BROWN')

save_button = Button(20, screen_height-70, 120, 50, 'SAVE')
load_button = Button(160, screen_height-70, 120, 50, 'LOAD')

def load_image():
    global loaded_image
    # Open file dialog to choose an image file
    file_path = filedialog.askopenfilename(
        title='Select an Image',
        filetypes=[('Image Files', "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
    )
    if file_path: # if a file was selected
        if os.path.exists(file_path):
            loaded_image = pygame.image.load(file_path)
        else:
            print(f'file "{file_path}" not found.')


# define a color_grid
colors_list = []
start = 0
stop = 256
step = 51
for r in range(start, stop, step):
    for g in range(start, stop, step):
        for b in range(start, stop, step):
            colors_list.append((r,g,b))

grid_coords = []
x = 0
y = 0
column_index = 1
for i in range(1, len(colors_list) + 1):
    grid_coords.append((x,y))
    x += 10
    column_index += 1
    if column_index > 36:
        x = 0
        y += 10
        column_index = 1

grid_x_offset = screen_width - 370
grid_y_offset = 20
color_grid = []
for i in range(len(colors_list)):
    button = Button(grid_x_offset + grid_coords[i][0], grid_y_offset + grid_coords[i][1], 10, 10, None, 0, colors_list[i])
    color_grid.append(button)

def draw_color_grid():
    for button in color_grid:
        button.draw()

def art_maker():
    global button_clicked, draw_tile_ready, dict_of_tiles, color_picked, timestamp

    pygame.draw.line(screen, (255,255,255), (pad_left_edge, pad_top_edge), (pad_right_edge, pad_top_edge), 1)
    pygame.draw.line(screen, (255,255,255), (pad_right_edge, pad_top_edge), (pad_right_edge, pad_bottom_edge), 1)
    pygame.draw.line(screen, (255,255,255), (pad_right_edge, pad_bottom_edge), (pad_left_edge, pad_bottom_edge), 1)
    pygame.draw.line(screen, (255,255,255), (pad_left_edge, pad_bottom_edge), (pad_left_edge, pad_top_edge), 1)

    draw_tile_button.draw()
    red_color_button.draw()
    green_color_button.draw()
    blue_color_button.draw()
    erase_button.draw()
    yellow_color_button.draw()
    brown_color_button.draw()
    
    save_button.draw()
    filename = f"screenshot_from_drawing_pad_{timestamp}.png"

    load_button.draw()

    if loaded_image:
        screen.blit(loaded_image, (pad_left_edge, pad_top_edge))

    for tile, color in dict_of_tiles.items():
         tile_rect = pygame.Rect(tile[0], tile[1], 10, 10) 
         pygame.draw.rect(screen, color, tile_rect)

    draw_color_grid()

    mouse_pressed = pygame.mouse.get_pressed()
    if mouse_pressed[0] and not button_clicked:
        if draw_tile_button.is_over(pygame.mouse.get_pos()):
            draw_tile_ready = not draw_tile_ready
            print('draw_tile_ready functionality', draw_tile_ready)
            button_clicked = True
        if red_color_button.is_over(pygame.mouse.get_pos()):
            color_picked = (255,0,0)
            print("You selected Red")
            button_clicked = True
        if green_color_button.is_over(pygame.mouse.get_pos()):
            color_picked = (0,255,0)
            print("You selected Green")
            button_clicked = True
        if blue_color_button.is_over(pygame.mouse.get_pos()):
            color_picked = (0,0,255)
            print("You selected Blue")
            button_clicked = True        
        if erase_button.is_over(pygame.mouse.get_pos()):
            color_picked = (0,0,0)
            print("You selected 'Eraser'")
            button_clicked = True    
        if yellow_color_button.is_over(pygame.mouse.get_pos()):
            color_picked = (255,255,0)
            print("You selected 'Yellow'")
            button_clicked = True    
        if brown_color_button.is_over(pygame.mouse.get_pos()):
            color_picked = (150,75,0)
            print("You selected 'Brown'")
            button_clicked = True  

        for button in color_grid:
            if button.is_over(pygame.mouse.get_pos()):
                color_picked = button.color
                print("You selected", str(button.color))
                button_clicked = True

        if save_button.is_over(pygame.mouse.get_pos()):
            #custom_filename = input('Enter the filename (with .pgn extennsion):')
            capture_surface = pygame.Surface((drawing_pad.width, drawing_pad.height))
            capture_surface.blit(screen, (0,0), drawing_pad)
            pygame.image.save(capture_surface, filename)
            print("Image saved")
            button_clicked = True   

        if load_button.is_over(pygame.mouse.get_pos()):
            print("You selected 'LOAD'")
            load_image()
            button_clicked = True   

    if draw_tile_ready:
        if mouse_pressed[0] and not button_clicked:
             mouse_x, mouse_y = pygame.mouse.get_pos()
             if pad_left_edge < mouse_x < pad_right_edge and pad_top_edge < mouse_y < pad_bottom_edge:
                round_x = (mouse_x // 10) * 10
                round_y = (mouse_y // 10) * 10
                dict_of_tiles[(round_x, round_y)] = color_picked
                button_clicked = True
                print(dict_of_tiles)


    if not mouse_pressed[0]:
        button_clicked = False
    







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
    # text_surface = my_font.render(str(framecount), False, (255,255,255))
    # (update your game state here)
    # Rendering
    
    screen.fill((0, 0, 0)) # Clear screen with black
    # screen.blit(text_surface, (0,0))
    art_maker()
    framecount += 1
    # (draw your game elements here)
    pygame.display.flip() # Update the display
    # Control the frame rate
    clock.tick(60) # 60 frames per second