import pygame
import heapq

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

WIDTH = 600
ROWS = 50
WINDOW = pygame.display.set_mode((WIDTH,WIDTH))
pygame.display.set_caption("Path Visualizer")

class Spot:
    def __init__(self,row,col,size,total_rows):
        self.row = row
        self.col = col
        self.x = row*size
        self.y = col*size
        self.color = WHITE
        self.total_rows = total_rows
        self.color = WHITE
        self.neigbhours = []
    
    def is_visited(self):
        return self.color == RED
    
    def get_pos(self):
        return self.row , self.col
    
    def is_start(self):
        return self.color == ORANGE
    
    def is_end(self):
        return self.color == TURQUOISE
    
    def is_barrier(self):
        return self.color == BLACK
    
    def make_start(self):
        self.color = ORANGE
    
    def make_end(self):
        self.color = TURQUOISE
    
    def make_barrier(self):
        self.color = BLACK
    
    def reset(self):
        self.color = WHITE

    def draw(self,win,size):
        pygame.draw.rect(win,self.color,(self.x,self.y,size,size))

    def make_visited(self):
        self.color = RED
    
    def make_path(self):
        self.color = PURPLE

    def __lt__(self, other):
        return False 

    def add_neigbhours(self,grid):
        # down
        if self.row < self.total_rows - 1 and not grid[self.row+1][self.col].is_barrier():
            self.neigbhours.append(grid[self.row+1][self.col])
        # up
        if self.row > 0 and not grid[self.row-1][self.col].is_barrier():
            self.neigbhours.append(grid[self.row-1][self.col])
        #right
        if self.col < self.total_rows - 1 and not grid[self.row][self.col+1].is_barrier():
            self.neigbhours.append(grid[self.row][self.col+1])
        #left
        if self.col > 0 and not grid[self.row][self.col-1].is_barrier():
            self.neigbhours.append(grid[self.row][self.col-1])
        
    
def h(p1,p2):
    x1,y1 = p1.get_pos()
    x2,y2 = p2.get_pos()
    return abs(x1-x2)+abs(y1-y2)
    
def make_grid(rows,width):
    grid = []
    size = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i,j,size,rows)
            grid[i].append(spot)
    return grid
    
def draw_lines(win,width,rows):
    size = width // rows
    # making the vertical lines
    for i in range(rows):
        pygame.draw.line(win,GREY,(0,size*i),(WIDTH,size*i))
    # making the horizontal lines
    for i in range(rows):
        pygame.draw.line(win,GREY,(size*i,0),(size*i,WIDTH))

def draw_grid(win,width,rows,grid):
    win.fill(WHITE)
    size = width // rows
    for row in grid:
        for spot in row:
            spot.draw(win,size)
    draw_lines(win,width,rows)
    pygame.display.update()
    return

def get_position(pos,rows,width):
    size = width // rows
    x,y = pos
    row = x // size
    col = y // size 
    return row,col

def Informed_search(draw, grid, start, end):
    pq = []
    heapq.heappush(pq, (0, start))
    g_score = {}
    f_score = {}
    came_from = {}  # To reconstruct the path
    
    for row in grid:
        for spot in row:
            g_score[spot] = float('inf')
            f_score[spot] = float('inf')
    
    g_score[start] = 0
    f_score[start] = h(start, end)
    
    while pq:
        _, current = heapq.heappop(pq)
        
        if current == end:
            # Reconstruct path
            while current in came_from:
                current = came_from[current]
                if current != start:
                    current.make_path()
                draw()
            return True
            
        for neighbor in current.neigbhours:
            temp_g_score = g_score[current] + 1
            
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = g_score[neighbor] + h(neighbor, end)
                heapq.heappush(pq, (f_score[neighbor], neighbor))
                if neighbor != end:
                    neighbor.make_visited()
        
        draw() 
        
    return False

 
def main(win,width,rows):
    run = True
    grid = make_grid(rows,width)
    start_check = False
    end_check = False
    start = None
    end = None
    while run:
        draw_grid(win,width,rows,grid)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row , col = get_position(pos,rows,width) 
                spot = grid[row][col]
                if not start_check:
                    spot.make_start()
                    start = spot
                    start_check = True
                elif not end_check:
                    spot.make_end()
                    end = spot
                    end_check = True 
                elif spot != start and spot != end:
                    spot.make_barrier()
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row , col = get_position(pos,rows,width)
                spot = grid[row][col]
                spot.reset()
                if spot == start:
                    start_check = False
                elif spot == end:
                    end_check = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:  # Make sure we have start and end
                    for row in grid:
                        for spot in row:
                            spot.add_neigbhours(grid)
                    
                    Informed_search(lambda: draw_grid(win, width, rows, grid), grid, start, end)

main(WINDOW,WIDTH,ROWS)