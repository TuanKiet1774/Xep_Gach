from grid import Grid
from blocks import *
import random

class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [I_block(), L_block(), J_block(), O_block(), S_block(), T_block(), Z_block()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False

    def get_random_block(self):
        # Nếu không còn khối nào trong danh sách, khởi tạo lại danh sách
        if len(self.blocks) == 0:
            self.blocks = [I_block(), L_block(), J_block(), O_block(), S_block(), T_block(), Z_block()]
        # Chọn khối ngẫu nhiên từ danh sách
        block = random.choice(self.blocks)
        # Xóa khỏi danh sách để tránh chọn lại khối này
        self.blocks.remove(block)
        return block

    # Di chuyển sang trái
    def move_left(self):
        self.current_block.move(0, -1)
        if not self.block_inside() or self.block_fits() == False:
            self.current_block.move(0, 1)

    # Di chuyển sang phải
    def move_right(self):
        self.current_block.move(0, 1)
        if not self.block_inside() or self.block_fits() == False:
            self.current_block.move(0, -1)
    
    # Di chuyển xuống
    def move_down(self):
        self.current_block.move(1, 0)
        if not self.block_inside() or self.block_fits() == False:
            self.current_block.move(-1, 0)
            self.lock_block()

    # Khóa vị trí khi các khối chạm đáy, nóc
    def lock_block(self):
        tiles = self.current_block.get_cell_position()
        for position in tiles:
            self.grid.grid[position.row][position.col] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        self.grid.clear_full()
        if self.block_fits() == False:
            self.game_over = True

    # Các khối va chạm
    def block_fits(self):
        tiles = self.current_block.get_cell_position()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.col) == False:
                return False
        return True

    # Xoay khối
    def rotate(self):
        self.current_block.rotate()
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.undo_rotate()
    
    # Kiểm tra xem tất cả các ô của khối có nằm trong lưới không
    def block_inside(self):
        tiles = self.current_block.get_cell_position()
        for tile in tiles:
            if not self.grid.is_inside(tile.row, tile.col):
                return False
        return True

    # Vẽ khối và lưới lên màn hình
    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen)

    # Khởi động lại game
    def reset (self):
        self.grid.reset()
        self.blocks = [I_block(), L_block(), J_block(), O_block(), S_block(), T_block(), Z_block()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
