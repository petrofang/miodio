import board
import touchio
import displayio
import pulseio
import time

BMP1 = "miodio.bmp"
BMP2 = "whappen.bmp"

# initialize the screen and backlight:
backlight = pulseio.PWMOut(board.TFT_BACKLIGHT)
screen = displayio.Group()
board.DISPLAY.show(screen)
max_brightness = 2 ** 15        # 
backlight.duty_cycle = 0 

# display bitmap from disk
image_file = open(BMP1, "rb")
odb = displayio.OnDiskBitmap(image_file)
face = displayio.Sprite(odb, pixel_shader=displayio.ColorConverter(), position=(0, 0))
screen.append(face)
board.DISPLAY.wait_for_frame()
backlight.duty_cycle = max_brightness

# do nothing so the program doesn't end
while True:
    pass
    