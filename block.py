from colors import Colors
from location import Position
import pygame

class Block:
  def __init__(self, id):
    self.id = id
    self.cells = {}
    self.cell_size = 30 #Kích thước mỗi ô
    self.rotation_state = 0 #Trạng thái của khôi
    self.colors = Colors.get_cell_colors()
    self.row_offset = 0 
    self.col_offset = 0
  
  # Di chyển các khối
  def move(self,rows, cols):
    self.row_offset += rows
    self.col_offset += cols
  # Lấy vị trí các ô 
  def get_cell_position(self):
    tiles = self.cells[self.rotation_state]
    moved_tiles = []
    for position in tiles:
      position = Position(position.row + self.row_offset, position.col + self.col_offset)
      moved_tiles.append(position)
    return moved_tiles

  def draw(self, screen):
    tiles = self.get_cell_position()
    for tile in tiles:
      tile_rect = pygame.Rect(tile.col * self.cell_size + 1, tile.row * self.cell_size + 1, self.cell_size -1, self.cell_size -1)
      pygame.draw.rect(screen, self.colors[self.id], tile_rect)

  # Xoay các khối 
  def rotate(self):
    self.rotation_state += 1
    if self.rotation_state == len(self.cells):
      self.rotation_state = 0
  
  #Xoay ngược
  def undo_rotate(self):
    self.rotation_state -= 1
    if self.rotation_state == 0:
      self.rotation_state = len(self.cells) - 1