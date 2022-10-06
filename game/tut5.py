import pygame
x = pygame.init()

game_window = pygame.display.set_mode((1200,500))
pygame.display.set_caption("my first game")
#game specific variable
exit_game =False
game_over = False

while not exit_game:
    for i in pygame.event.get():
        print(i)
   # pass
pygame.quit()
quit()