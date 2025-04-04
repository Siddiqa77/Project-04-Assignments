import pygame

# Constants
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
ROWS, COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
ERASER_SIZE = 40

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Eraser on Canvas")

# Create a grid of blue cells
grid = [[BLUE for _ in range(COLS)] for _ in range(ROWS)]

def draw_grid():
    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.rect(screen, grid[row][col], (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def erase(x, y):
    for row in range(ROWS):
        for col in range(COLS):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if rect.colliderect(pygame.Rect(x, y, ERASER_SIZE, ERASER_SIZE)):
                grid[row][col] = WHITE

def main():
    running = True
    while running:
        screen.fill(WHITE)
        draw_grid()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if pygame.mouse.get_pressed()[0]: 
            x, y = pygame.mouse.get_pos()
            erase(x, y)
        
        pygame.display.flip()
    
    pygame.quit()

if __name__ == '__main__':
    main()