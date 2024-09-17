import sys
import pygame 
from game import Game

# Khởi tạo tất cả các mô-đun của Pygame.
pygame.init()

# Cửa sổ trò chơi, chiều rộng 300, chiều dài 600
screen = pygame.display.set_mode((300,600))

# Tên của cửa sổ Game
pygame.display.set_caption("Tetris")

# Tốc độ khung hình
clock = pygame.time.Clock()
game = Game()

# Tạo sự kiện để đặt thời gian rơi xuống cho các khối
GAME_UPDATE = pygame.USEREVENT
# Thời gian của sự kiện 
pygame.time.set_timer(GAME_UPDATE,300)

# Lấy các sự kiện của người chơi
while True: 
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
      pygame.quit() #Đóng game
      sys.exit()
    #Phím điều hướng, điều khiển của người chơi 
    if event.type == pygame.KEYDOWN: 
      if game.game_over == True:
        game.game_over = False
        game.reset()
      if event.key == pygame.K_LEFT and game.game_over == False:
        game.move_left()
      if event.key == pygame.K_RIGHT and game.game_over == False:
        game.move_right()
      if event.key == pygame.K_DOWN and game.game_over == False:
        game.move_down() 
      if event.key == pygame.K_SPACE and game.game_over == False:
        game.rotate()
    if event.type == GAME_UPDATE and game.game_over == False:
      game.move_down()
 
  #Màu của giao diện
  screen.fill((44,44,127))

  #Vẽ lên cửa sổ
  game.draw(screen)

  #Cập nhật lại màn hình
  pygame.display.update() 

  #Số khung hình trên giây
  clock.tick(60) 
