import unicornhat as unicorn
import time
from font import Font

unicorn.set_layout(unicorn.PHAT)
unicorn.brightness(0.2)
unicorn.rotation(0)

def show_time():
    current_time = time.strftime('%H%M')
    buffer = Font().string_to_pixels(current_time)
    for y in range(4):
        for x in range(8):
            if buffer[y][x] == 1:
                unicorn.set_pixel(x, y, 100, 100, 100)
    unicorn.show()

while True:
    show_time()
    time.sleep(1000)

