import pygame
from colors import Colors

class Grid: 
  def __init__(self):
    self.num_rows = 20 #20 Hàng
    self.num_cols = 10 #10 Hàng
    #Kích thước của ô lưới
    self.cell_size = 30 #px
    # Lưới là mảng 2 chiều với tất cả các giá trị khởi tạo bằng 0
    self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
    self.colors = Colors.get_cell_colors()
  
  # In các giá trị lên các ô
  def print_grid(self):
    for row in range(self.num_rows):
      for col in range(self.num_cols):
        print(self.grid[row][col], end = " ")
      print()
      
  # Kiểm tri phạm vi
  def is_inside(self, row, col):
    if row >= 0 and row < self.num_rows and col >= 0 and col < self.num_cols:
      return True
    return False
  
  # Vẽ lưới lên của sổ Game 
  def draw(self, screen):
    for row in range(self.num_rows):
      for col in range(self.num_cols):
        cell_value = self.grid[row][col]
        cell_rect = pygame.Rect(col * self.cell_size + 11, row * self.cell_size + 11, self.cell_size - 1, self.cell_size - 1)
        pygame.draw.rect(screen, self.colors[cell_value], cell_rect)

  # Kiểm tra một ô có đang trống hay không
  def is_empty(self, row, col):
    if self.grid[row][col] == 0:
      return True
    return False
  
  # Hàng đầy
  def is_row_full(self, row):
    for col in range(self.num_cols):
      if self.grid[row][col] == 0:
        return False
    return True
  
  # Xoá hàng đầy
  def clear_row(self, row):
    for col in range(self.num_cols):
      self.grid[row][col] = 0

  #Di chuyển hàng xuống
  def move_row_down(self, row, num_rows):
    for col in range(self.num_cols):
      self.grid[row + num_rows][col] = self.grid[row][col]
      self.grid[row][col] = 0

  def clear_full (self):
    completed = 0
    for row in range(self.num_rows - 1, 0, -1):
      if self.is_row_full(row):
        self.clear_row(row)
        completed += 1
      elif completed > 0:
        self.move_row_down(row, completed)
    return completed
  
  # Khởi động lại toàn bộ khung 
  def reset(self):
    for row in range(self.num_rows):
      for col in range(self.num_cols):
        self.grid[row][col] = 0