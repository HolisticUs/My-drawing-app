import math

colors_list = []
for r in range(0, 256, 51):
    for g in range(0, 256, 51):
        for b in range(0, 256, 51):
            colors_list.append((r,g,b))

grid_coords = []
x = 0
y = 0
for i in range(1, len(colors_list) + 1):
    grid_coords.append((x,y))
    x += 10
    if x > math.sqrt(len(colors_list))*10:
        x = 0
        y += 10

print("colors list:", colors_list)
print('grid coordinates:', grid_coords)

print('color list length:', len(colors_list))
print('grid coordinates length:', len(grid_coords))