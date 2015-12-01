# mc_microbit.py  30/11/2015  D.J.Whale
#
# First pass at building a working micro:bit inside Minecraft
# Note: it *should* be possible to have more than one micro:bit
# inside Minecraft simultaneously.
# TODO: Might have to be a bit clever to share button hit events.
# TODO: constants for button position

#   buttons.a_was_pressed
#   buttons.b_was_pressed

import mcpi.minecraft as minecraft
import mcpi.block as block
import fonts
import time


class Display():
    XSTEP   = 5
    YSTEP   = 4

    ON      = block.WOOL.id, 14
    OFF     = block.WOOL.id, 13

    def __init__(self, parent, xoffset, yoffset, zoffset):
        # x is x positive (EAST)
        # z is z negative (NORTH)
        # y is flat
        self.x  = parent.x + xoffset
        self.y  = parent.y + yoffset
        self.z  = parent.z - zoffset
        self.mc = parent.mc

        
    def set_pixel(self, x, y, state):
        # x is x positive (EAST)
        # z is z negative (NORTH)
        # y is flat
        self.mc.setBlock(self.x + (x*self.XSTEP),
                         self.y,
                         self.z + (y*self.YSTEP),
                         state)


    def clear(self):
        for x in range(5):
            for y in range(5):
                self.set_pixel(x, y, self.OFF)


    def all_on(self):
        for x in range(5):
            for y in range(5):
                self.set_pixel(x, y, self.ON)


    def show(self, image, offset=0):
        # image is "ppppp\n" * 5
        x = 0
        y = 0
        # assumes no spaces, and well formed
        i = offset # skip to offset for first row
        while True:
            ch = image[i]
            i += 1
            if ch == '\n':
                x = 0
                y += 1
                if y >= 5: return # bail early
                # assumes well formed
                i += offset
            else:
                if x < 5:
                    if ch == '0':
                        p = self.OFF
                    else:
                        p = self.ON
                    self.set_pixel(x, y, p)
                    x += 1


    def show_char(self, msg):
        i = fonts.microbitFont.get(msg[0])
        self.show(i)


    def scroll(self, msg, delay=400):
        # assumes a clean 5x5 font, always!
        # convert from milliseconds to seconds
        delay = float(delay)/1000

        if len(msg) == 0: return
        if len(msg) == 1:
            self.show_char(msg[0])
            return

        # Add a space at beginning and end, for a clean scroll
        msg = " " + msg + " "

        # build 5 rows based on font glyphs
        output_rows = ["","","","",""]
        for ch in msg:
            g = fonts.microbitFont.get(ch)
            for row in range(5):
                r = g[row*6:(row*6)+5] # 6 because of nl
                output_rows[row] += r

        #for r in output_rows:
        #    print(str(r))
        # Merge into an image string with newlines at end
        img = ""
        for row in range(5):
            img += output_rows[row] + '\n'

        #print("IMAGE:\n" + str(img))
        
        # scroll
        for i in range(len(msg)*5):
            self.show(img, i)
            time.sleep(delay)

class Microbit():
    FILENAME = "microbit.csv"
    # TODO palette of skin colours
    BACKGROUND = 1
    FLASH      = 2
    BUTTON     = 3
    LED_ON     = 4
    LED_OFF    = 5
    PAD        = 6
    
    # origin = bottom left of microbit, but drawn at 90 degrees!
    # X,Y,Z mc coordinates
    DISPLAY_X_OFFSET  = 18
    DISPLAY_Y_OFFSET  = 0
    DISPLAY_Z_OFFSET  = 23
    
    # x,y offsets onto microbit
    #DISPLAY_X_SIZE = 1
    #DISPLAY_Y_SIZE = 1
    #DISPLAY_X_STEP = 4
    #DISPLAY_Y_STEP = 5
    #BUTTON_A_X
    #BUTTON_A_Y
    #BUTTON_B_X
    #BUTTON_B_Y
    
    def __init__(self, mc, x, y, z):
        self.mc = mc
        self.x  = x
        self.y  = y
        self.z  = z

        self.display = Display(self,
                    self.DISPLAY_X_OFFSET, self.DISPLAY_Y_OFFSET,
                    self.DISPLAY_Z_OFFSET)

        #buttons = Buttons(self, self.BUTTON_A_X, self.BUTTON_A_Y,
        #   self.BUTTON_B_X, self.BUTTON_B_Y)


    def draw(self, filename=None):
        # Note, the micro:bit is stored in a strange rotation
        # origin is bottom left
        # increases in x move up
        # increases in z move right
        # We correct this rotation as it is read-in from the file
        # otherwise fonts are hard to draw.
        # Later, we might just rotate the file data.

        # So, it is drawn x moving x positive (east)
        # z moving z negative (north)
        # y flat
        if filename == None: filename=self.FILENAME
        f  = open(filename)
        mc = self.mc
        x  = 0
        z  = 0
        
        for line in f.readlines():
            line = line.strip()
            csv = line.split(',')
            for b in csv:
                b = int(b)
                mc.setBlock(self.x+x, self.y, self.z+z, b)
                z -= 1
            z = 0
            x += 1
        f.close()


#----- TEST HARNESS -----------------------------------------------------------

mc = None
microbit = None

def build():
    global mc, microbit
    
    mc = minecraft.Minecraft.create()
    pos = mc.player.getTilePos()
    microbit = Microbit(mc, pos.x, pos.y, pos.z)
    microbit.draw()
    microbit.display.clear()
    microbit.display.set_pixel(0,0,microbit.display.ON)


def hello():
    build()
    msg = 'Hello'
    for ch in msg:
        microbit.display.show_char(ch)
        time.sleep(1)


def test_bigimage():    
    build()
    time.sleep(5)
    IMG = \
      "10000000000000100000\n" \
      "01000000000001000000\n" \
      "00100000000010000000\n" \
      "00010000000100000000\n" \
      "00001111111000000000\n"

    time.sleep(5)
    for i in range(15):
        microbit.display.show(IMG, i)
        time.sleep(1)


def test_scroll():
    # would be nice to use no parameters and get an 'in memory model' only?
    #microbit = Microbit(0, 1, 2, 3) # dummy parameters
    build()
    for i in range(5):
        microbit.display.scroll("Hello")


if __name__ == "__main__":
    test_scroll()
    
# END
