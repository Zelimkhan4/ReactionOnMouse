import pygame



class Board:
    def __init__(self, width, height, left, top, cell_size):
        self.width = width
        self.height = height
        self.left = left
        self.top = top
        self.cell_size = cell_size
        # Cписок с цветами
        self.colors = ['White', 'Red', 'Blue']
        
        self.board = [[0] * self.width for i in range(self.height)]
    
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for row in range(self.height):
            for col in range(self.width):
                pygame.draw.rect(screen, pygame.Color(self.colors[self.board[row][col]]), (self.left + (row * self.cell_size), self.top + (col * self.cell_size), self.cell_size, self.cell_size), 1)

    def interface(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        print(cell)
        # Дальше всё ограничивается только фантазией

    def get_cell(self, mouse_pos):
        for row in range(self.height):
            for col in range(self.width):
                upper_left = (self.left + (col * self.cell_size), (self.top + (row * self.cell_size)))
                if upper_left[0] < mouse_pos[0] < upper_left[0] + self.cell_size and\
                    upper_left[1] < mouse_pos[1] < upper_left[1] + self.cell_size:
                    # Возвращаю значение в виде (строка, столбец)
                    return row, col
  

running = True
size = 500, 500
screen = pygame.display.set_mode(size)
board = Board(15, 15, 10, 10, 25)
while running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            board.interface(ev.pos)
    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()