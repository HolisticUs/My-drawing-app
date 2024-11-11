import pygame
draw_mode = None
color_picked = None
button_clicked = False
mouse_pressed = pygame.mouse.get_pressed()
pad_right_edge = 500
pad_bottom_edge = 500
pad_left_edge = 10
pad_top_edge = 10
dict_of_tiles = {}

def find_all_tiles(tiles_to_replace, dict_of_tiles, color_to_replace, new_color, tiles_checked=[]):
    tile_added = False
    for tile in tiles_to_replace:
        # check for each of the four adjacent tiles:
        top_tile = dict_of_tiles[(mouse_x, mouse_y - 10)]
        bottom_tile = dict_of_tiles[(mouse_x, mouse_y - 10)]
        left_tile = dict_of_tiles[(mouse_x -10, mouse_y)]
        right_tile = dict_of_tiles[(mouse_x + 10, mouse_y)] 
        adj_tiles = [top_tile, bottom_tile, left_tile, right_tile]
        for adj_tile in adj_tiles:
            if adj_tile in tiles_checked:
                continue
            elif adj_tile in dict_of_tiles and dict_of_tiles[adj_tile] == color_to_replace:
                tiles_to_replace.append(adj_tile)
                tile_added = True
            tiles_checked.append(adj_tile)
        
        # Recurse if an adjacent tile was found with the same color
        if tile_added == True:
            find_all_tiles(tiles_to_replace, dict_of_tiles, color_to_replace, new_color, tiles_checked)
        else:
            # Base case, no new tiles found, change the color
            for tile in tiles_to_replace:
                dict_of_tiles[tile] = new_color

if draw_mode == 'fill' and mouse_pressed[0] and not button_clicked:
    replacement_color = color_picked
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if pad_left_edge < mouse_x < pad_right_edge and pad_top_edge < mouse_y < pad_bottom_edge:
        round_x = (mouse_x // 10) * 10
        round_y = (mouse_y // 10) * 10
        if (mouse_x, mouse_y) not in dict_of_tiles:
            dict_of_tiles(mouse_x, mouse_y) = None
        tile_clicked = (mouse_x, mouse_y)
        tiles_to_replace = [(mouse_x, mouse_y)]
        find_all_tiles(tiles_to_replace, dict_of_tiles, dict_of_tiles[mouse_x, mouse_y], replacement_color, [(mouse_x, mouse_y)])
                
