#Code by bigmohammad
#---------------------
#Youtube: bigmohammad
#---------------------
#Instagram: bigmohammad.official

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys

# Constants
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 10
ROWS, COLS = 3, 3
SQUARE_SIZE = WIDTH // COLS

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")
screen.fill(WHITE)
board = [[' ' for _ in range(COLS)] for _ in range(ROWS)]
turn = 'X'
game_over = False

def draw_grid():
    for i in range(1, ROWS):
        pygame.draw.line(screen, BLACK, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, BLACK, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] != ' ':
                center_x = col * SQUARE_SIZE + SQUARE_SIZE // 2
                center_y = row * SQUARE_SIZE + SQUARE_SIZE // 2
                radius = SQUARE_SIZE // 3
                if board[row][col] == 'X':
                    pygame.draw.line(screen, BLUE, (center_x - radius, center_y - radius),
                                     (center_x + radius, center_y + radius), LINE_WIDTH)
                    pygame.draw.line(screen, BLUE, (center_x - radius, center_y + radius),
                                     (center_x + radius, center_y - radius), LINE_WIDTH)
                    draw_text('X', pygame.font.Font(None, 60), BLACK, screen, center_x, center_y)
                else:
                    pygame.draw.circle(screen, RED, (center_x, center_y), radius, LINE_WIDTH)
                    draw_text('O', pygame.font.Font(None, 60), BLACK, screen, center_x, center_y)

def check_winner():
    # Check rows, columns, and diagonals for a win
    for i in range(ROWS):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

def is_board_full():
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == ' ':
                return False
    return True

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if not game_over and event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()
            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE

            if board[clicked_row][clicked_col] == ' ':
                board[clicked_row][clicked_col] = turn
                winner = check_winner()
                if winner:
                    game_over = True
                elif is_board_full():
                    game_over = True
                turn = 'O' if turn == 'X' else 'X'

        if game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                # Reset the game
                board = [[' ' for _ in range(COLS)] for _ in range(ROWS)]
                game_over = False
                turn = 'X'
                screen.fill(WHITE)

    screen.fill(WHITE)
    draw_grid()
    draw_board()

    if game_over:
        if winner:
            draw_text(f"Player {winner} wins!", pygame.font.Font(None, 40), BLACK, screen, WIDTH // 2, HEIGHT // 2)
        else:
            draw_text("It's a tie!", pygame.font.Font(None, 40), BLACK, screen, WIDTH // 2, HEIGHT // 2)
        draw_text("Press 'R' to play again", pygame.font.Font(None, 24), BLACK, screen, WIDTH // 2, HEIGHT - 50)

    pygame.display.flip()
