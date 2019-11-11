# recCAPTCHA solver
# 11/11/2019
# Matthew Lee Parks Jr
# This program is used to solve the programming challenge at http://sloth.highschoolhack.me:6002/index.php
# In essence, a 3x3 grid od dot have 3 colors, gray, red and green
# Clicking a green earns the bot a point, 30 points are needed to win, clicking a red makes the count reset
# About every 40millis, the board changes, it can be all gray, all red, or all gray with 1 green
# Screenie of my setup: https://gyazo.com/39da3b6cbdb174ba92186c708b947dde(important for pixel mapping)

# Imports
from PIL import ImageGrab
from time import sleep
import mouse

# Used to track how many clicks we have, used so my mouse does not move forever
clicks = 0

# First, we grab the initial image
image = ImageGrab.grab()

# Used to determine screen size, now this returned (1920, 1080) in my case
print(image.size)

# First, I will prove how I got the location of each "dot"
# I began with 10 pixels, which hits the edge, so i added the radius of the circle
# This leaves 35 for the x. The y was a guess, half of 1080 is 540, minus 100 was about right
# By using crl + u(view source) on the website, i know each dot is 50px wide
# This is the 1st(bottom) row
print(image.getpixel((35, image.size[1] / 2 - 100)))
print(image.getpixel((75, image.size[1] / 2 - 100)))
print(image.getpixel((135, image.size[1] / 2 - 100)))

# Now, I know the location of the first row of dots, next, i translate it to the rows
# By adding 6-ish to each row, i know I have moved to the next row
print(image.getpixel((35, image.size[1] / 2 - 160)))
print(image.getpixel((75, image.size[1] / 2 - 160)))
print(image.getpixel((135, image.size[1] / 2 - 160)))

# This is the 3rd(top) row
print(image.getpixel((35, image.size[1] / 2 - 220)))
print(image.getpixel((75, image.size[1] / 2 - 220)))
print(image.getpixel((135, image.size[1] / 2 - 220)))

# Now, we know the location of each dot, using this we can loop, and wait for the correct dot
# I save the pixel location to save time later on, if these values where known, the above code has no use!
dot1 = (35, image.size[1] / 2 - 100)
dot2 = (75, image.size[1] / 2 - 100)
dot3 = (135, image.size[1] / 2 - 100)
dot4 = (35, image.size[1] / 2 - 160)
dot5 = (75, image.size[1] / 2 - 160)
dot6 = (135, image.size[1] / 2 - 160)
dot7 = (35, image.size[1] / 2 - 220)
dot8 = (75, image.size[1] / 2 - 220)
dot9 = (135, image.size[1] / 2 - 220)

# Begin the looping
print("Looping")

while clicks < 30:
    # Each iteration, we wait 50milli seconds so 1) The mouse does not lag 2) The website has a chance to change
    # renders Next, we get the screen again(image is like a screenshot) By using the pixel data, we know that 0, 255,
    # 0 is green, so we need to click it Note: The code below can be GREATLY improved, I tried to keep that "code
    # competition" style where copy-pasting is just faster
    sleep(0.05)
    image = ImageGrab.grab()
    pixel_data = image.getpixel(dot1)
    if pixel_data[1] == 255:
        print("FOUND")
        mouse.move(dot1[0], dot1[1])
        mouse.click()
        clicks = clicks + 1
    pixel_data = image.getpixel(dot2)
    if pixel_data[1] == 255:
        print("FOUND")
        mouse.move(dot2[0], dot2[1])
        mouse.click()
        clicks = clicks + 1
    pixel_data = image.getpixel(dot3)
    if pixel_data[1] == 255:
        print("FOUND")
        mouse.move(dot3[0], dot3[1])
        mouse.click()
        clicks = clicks + 1
    pixel_data = image.getpixel(dot4)
    if pixel_data[1] == 255:
        print("FOUND")
        mouse.move(dot4[0], dot4[1])
        mouse.click()
        clicks = clicks + 1
    pixel_data = image.getpixel(dot5)
    if pixel_data[1] == 255:
        print("FOUND")
        mouse.move(dot5[0], dot5[1])
        mouse.click()
        clicks = clicks + 1
    pixel_data = image.getpixel(dot6)
    if pixel_data[1] == 255:
        print("FOUND")
        mouse.move(dot6[0], dot6[1])
        mouse.click()
        clicks = clicks + 1
    pixel_data = image.getpixel(dot7)
    if pixel_data[1] == 255:
        print("FOUND")
        mouse.move(dot7[0], dot7[1])
        mouse.click()
        clicks = clicks + 1
    pixel_data = image.getpixel(dot8)
    if pixel_data[1] == 255:
        print("FOUND")
        mouse.move(dot8[0], dot8[1])
        mouse.click()
        clicks = clicks + 1
    pixel_data = image.getpixel(dot9)
    if pixel_data[1] == 255:
        print("FOUND")
        mouse.move(dot9[0], dot9[1])
        mouse.click()
        clicks = clicks + 1
