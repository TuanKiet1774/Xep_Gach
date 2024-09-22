""" Tải Pygame: Mở PowerShell -> pip install pygame-ce """ 
import sys
import pygame 
from game import Game
from colors import Colors

# Khởi tạo tất cả các mô-đun của Pygame.
pygame.init()

#font chữ
title_font = pygame.font.Font("Font/SVN-Determination Sans.otf", 40)
# Điểm
score_surface = title_font.render("SCORE", True, Colors.white)
# Khối tiếp theo
next_surface = title_font.render("NEXT BLOCK", True, Colors.white)

# Thông báo két thúc
over_surface = title_font.render("GAME OVER !!!", True, Colors.red)

#Khung điểm, khối tiếp theo, thông báo, thời gian
score_rect = pygame.Rect(330, 70, 200, 60)
next_rect = pygame.Rect(330, 240, 200, 180)
over_rect = pygame.Rect(30, 150, 270, 100)
time_rect = pygame.Rect(330, 450, 200, 60)

# Cửa sổ trò chơi, chiều rộng , chiều dài
screen = pygame.display.set_mode((550,620))

# Tên của cửa sổ Game
pygame.display.set_caption("Tetris")

# Tốc độ khung hình
clock = pygame.time.Clock()
game = Game()

# Thời gian game, lấy thời gian bắt đầu
start = pygame.time.get_ticks()

# Biến tính thời gian dừng lại khi game over
end_game_time = None 

# Tạo sự kiện để đặt thời gian rơi xuống cho các khối
GAME_UPDATE = pygame.USEREVENT

# Thời gian của sự kiện 
speed_flag = False
speed_game = 700
pygame.time.set_timer(GAME_UPDATE,speed_game)

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
        start = pygame.time.get_ticks()
        end_game_time = None
        speed_game = 700
        pygame.time.set_timer(GAME_UPDATE, speed_game)
        speed_flag = False
      if event.key == pygame.K_LEFT and not game.game_over:
        game.move_left()
      if event.key == pygame.K_RIGHT and not game.game_over:
        game.move_right()
      if event.key == pygame.K_DOWN and not game.game_over:
        game.move_down() 
      if event.key == pygame.K_SPACE and not game.game_over:
        game.rotate()
    if event.type == GAME_UPDATE and not game.game_over:
      game.move_down()
    
  #Màu của giao diện
  screen.fill(Colors.dark_blue)

  #Tiêu đề điểm và khối tiếp theo
  screen.blit(score_surface,(385, 20, 50, 50))
  screen.blit(next_surface,(340, 180, 50, 50))

  #Khung điểm, khung khối tiếp theo, khung thời gian
  pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
  pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
  pygame.draw.rect(screen, Colors.light_blue, time_rect, 0, 20)
  
  # Nếu game over, giữ nguyên thời gian khi game kết thúc
  if game.game_over and end_game_time is None:
    end_game_time = (pygame.time.get_ticks() - start) // 1000
  if game.game_over:
    end = end_game_time
  else:
    end = (pygame.time.get_ticks() - start) // 1000

  # Tăng tốc game sau 1 thời gian game
  if (pygame.time.get_ticks() - start) // 1000 >= 30 and speed_flag == False:
    speed_game -= 300
    pygame.time.set_timer(GAME_UPDATE, speed_game)
    speed_flag = True


  # Thời gian tính bằng giây
  minutes = end // 60
  seconds = end % 60

  time_text = f"{minutes:02} : {seconds:02}"

  # Render thời gian và vẽ lên màn hình
  time_surface = title_font.render(time_text, True, Colors.green)
  screen.blit(time_surface, (380, 455 ,50, 50))

  # Hiển thị điểm
  score_value = title_font.render(str(game.score), True, Colors.yellow)
  screen.blit(score_value,score_value.get_rect(centerx = score_rect.centerx, centery = score_rect.centery))

  #Vẽ lên cửa sổ
  game.draw(screen)

  #thông báo khi game kết thúc
  if game.game_over == True:
    pygame.draw.rect(screen, Colors.black, over_rect, 0, 10)
    screen.blit(over_surface,(50, 180, 270, 100))
    
  #Cập nhật lại màn hình
  pygame.display.update() 

  #Số khung hình trên giây
  clock.tick(60) 

