import unicornhat as unicorn
import time
from font import Font

class Clock:

    width = 8
    height = 4
    background_color = [0, 0, 0]
    foreground_color = [0, 206, 209]
    direction = "right"
    speed = 0.5

    def __init__(self):
        unicorn.set_layout(unicorn.PHAT)
        unicorn.brightness(0.3)
        unicorn.rotation(180)

    def start(self):
        while True:
            current_time = time.strftime('%H:%M')
            buffer = Font().string_to_pixels(current_time)
            if self.direction == "right":
                self.scroll_right(buffer)
                self.direction = "left"
            else:
                self.scroll_left(buffer)
                self.direction = "right"
            time.sleep(0.5)

    @staticmethod
    def slice_columns(array, start, end):
        sliced = [];
        num_rows = len(array)
        for i in range(num_rows):
            sliced.append(array[i][start:end])
        return sliced

    # assume pixels is an 4x8 2d list
    @staticmethod
    def draw_pixels(pixels, bg_color, fg_color):
        num_rows = len(pixels)
        num_cols = len(pixels[0])
        unicorn.clear()
        for y in range(num_rows):
            for x in range(num_cols):
                if pixels[y][x] == 1:
                    unicorn.set_pixel(x, y, fg_color[0], fg_color[1], fg_color[2])
                else:
                    unicorn.set_pixel(x, y, bg_color[0], bg_color[1], bg_color[2])
        unicorn.show()

    def scroll_right(self, array):
        iterations = len(array[0]) - self.width
        start = 0
        end = self.width
        for i in range(iterations):
            self.draw_pixels(self.slice_columns(array, start, end), self.background_color, self.foreground_color)
            start += 1
            end += 1
            time.sleep(self.speed)

    def scroll_left(self, array):
        iterations = len(array[0]) - self.width
        start = len(array[0]) - self.width - 1
        end = len(array[0]) - 1
        for i in range(iterations):
            self.draw_pixels(self.slice_columns(array, start, end), self.background_color, self.foreground_color)
            start -= 1
            end -= 1
            time.sleep(self.speed)

Clock().start()

