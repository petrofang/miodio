import board
import displayio
import pulseio
import time

BMP1 = "miodio.bmp"
BMP2 = "whappen.bmp"

# initialize the screen and backlight:
backlight = pulseio.PWMOut(board.TFT_BACKLIGHT)
screen = displayio.Group()
board.DISPLAY.show(screen)
max_brightness = 2 ** 15
backlight.duty_cycle = 0 

# display bitmap from disk
def show_image(filename):
    image_file = open(filename, "rb")
    odb = displayio.OnDiskBitmap(image_file)
    face = displayio.Sprite(odb, pixel_shader=displayio.ColorConverter(), position=(0, 0))
    time.sleep(1)
    screen.append(face)
    board.DISPLAY.wait_for_frame()
    backlight.duty_cycle = max_brightness

while True:
    show_image(BMP2)
    time.sleep(1)
    show_image(BMP1)       # why does this end in "RuntimeError: Group full" ?
    time.sleep(1)