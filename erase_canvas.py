import pygame

pygame.init()

CANVAS_WIDTH, CANVAS_HEIGHT = 400, 400
CELL_SIZE = 40
ERASER_SIZE = 20

BLUE = (0, 0, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

screen = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))
pygame.display.set_caption("Eraser Effect in Pygame")

grid = {}
for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
    for col in range(0, CANVAS_WIDTH, CELL_SIZE):
        grid[(col, row)] = True

eraser = pygame.Rect(200, 200, ERASER_SIZE, ERASER_SIZE)

running = True
while running:
    screen.fill(WHITE)

    for (col, row), visible in grid.items():
        if visible:
            pygame.draw.rect(screen, BLUE, (col, row, CELL_SIZE, CELL_SIZE))
    mouse_x, mouse_y = pygame.mouse.get_pos()
    eraser.topleft = (mouse_x, mouse_y)
    if pygame.mouse.get_pressed()[0]:
        for (col, row) in list(grid.keys()):
            cell_rect = pygame.Rect(col, row, CELL_SIZE, CELL_SIZE)
            if eraser.colliderect(cell_rect):
                grid[(col, row)] = False

   
    pygame.draw.rect(screen, RED, eraser)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
