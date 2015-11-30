# mc_microbit.py  30/11/2015  D.J.Whale
#
# First pass at building a working micro:bit inside Minecraft
#
# TODO: Turn this into a python class
# TODO: Store the x,y,z pos as instance variables
# TODO: constants for button position, led size and location

# perhaps index numbers in the map only,
# each index number maps to a blockid + extradata
# This makes it re-skinnable from a palette

# Class MicroBit
# has all the same methods as the MicroPython.micro:bit
# only implement at the moment (Minimum Viable Product)
#   display.scroll(msg)
#   display.show(image) - single image for now
#   buttons.a_was_pressed
#   buttons.b_was_pressed
#
# Add all the other stuff later if this works well.

# draw(mc) method that draws it via a minecraft canvas
# 

def draw(filename, x,y,z):
    f = open(filename)
    xpos = x
    ypos = y
    zpos = z
    for line in f.readlines():
        #print(line)
        line = line.strip()
        csv = line.split(',')
        for b in csv:
            b = int(b)
            mc.setBlock(xpos, ypos, zpos, b)
            xpos += 1
        xpos = x
        zpos += 1
    f.close()


def all_leds(x,y,z, blockid, blockdata):
    # origin = bottom left of microbit, but drawn at 90 degrees!
    XOFFSET = 7
    XSTEP   = 4
    ZOFFSET = 18
    ZSTEP   = 5
    
    for xpos in range(5):
        for zpos in range(5):
            mc.setBlock(x+XOFFSET+(xpos*XSTEP), y, z+ZOFFSET+(zpos*ZSTEP), blockid, blockdata)


def led(x,y,z, led_x, led_y, blockid, blockdata):
    # origin = bottom left of microbit, but drawn at 90 degrees!
    XOFFSET = 7
    XSTEP   = 4
    ZOFFSET = 18
    ZSTEP   = 5

    mc.setBlock(x+XOFFSET+(led_x*XSTEP), y, z+ZOFFSET+(led_z*ZSTEP), blockid, blockdata)

    
mc = None
def build():
    global mc
    import mcpi.minecraft as minecraft
    import mcpi.block as block
    
    mc = minecraft.Minecraft.create()
    pos = mc.player.getTilePos()
    draw("microbit.csv", pos.x, pos.y-1, pos.z)
    all_leds(pos.x, pos.y-1, pos.z, block.WOOL.id, 14)

        
if __name__ == "__main__":
    print("building...")
    build()
    print("done!")


# END
