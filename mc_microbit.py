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
    XSTEP   = 4
    YSTEP   = 5

    ON      = block.WOOL.id, 14
    OFF     = block.WOOL.id, 13

    def __init__(self, parent, xoffset, yoffset, zoffset):
        self.x  = parent.x + xoffset
        self.y  = parent.y + yoffset
        self.z  = parent.z + zoffset
        self.mc = parent.mc

        
    def set_pixel(self, x, y, state):
        self.mc.setBlock(self.x + (x*self.XSTEP), self.y, self.z + (y*self.YSTEP), state)


    def clear(self):
        for x in range(5):
            for y in range(5):
                self.set_pixel(x, y, self.OFF)


    def all_on(self):
        for x in range(5):
            for y in range(5):
                self.set_pixel(x, y, self.ON)


    def show(self, image):
        # image is "ppppp\n" * 5
        x = 0
        y = 0
        for ch in image:
            if ch == '\n':
                x = 0
                y += 1
            elif ch == ' ':
                pass
            else:
                if x < 5 and y < 5:
                    if ch == '0':
                        p = self.OFF
                    else:
                        p = self.ON
                    self.set_pixel(x, y, p)
                    x += 1


    def show_char(self, msg):
        i = fonts.microbitFont.get(msg[0])
        self.show(i)


    def scroll(self, msg):
        pass # TODO


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
    DISPLAY_X_OFFSET  = 7
    DISPLAY_Y_OFFSET  = 0
    DISPLAY_Z_OFFSET  = 18
    
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
        if filename == None: filename=self.FILENAME
        f = open(filename)
        xpos = self.x
        ypos = self.y
        zpos = self.z
        mc   = self.mc
        
        for line in f.readlines():
            line = line.strip()
            csv = line.split(',')
            for b in csv:
                b = int(b)
                mc.setBlock(xpos, ypos, zpos, b)
                xpos += 1
            xpos = self.x
            zpos += 1
        f.close()
        

#----- TEST HARNESS -----------------------------------------------------------

mc = None
microbit = None

def build():
    global mc, microbit
    
    mc = minecraft.Minecraft.create()
    pos = mc.player.getTilePos()
    microbit = Microbit(mc, pos.x, pos.y-1, pos.z)
    microbit.draw()
    microbit.display.all_on()
    microbit.display.set_pixel(2, 2, microbit.display.OFF)


def test():
    msg = 'Hello'
    for ch in msg:
        microbit.display.show_char(ch)
        time.sleep(1)
    
    
if __name__ == "__main__":
    build()
    time.sleep(5)
    test()
    
# END
