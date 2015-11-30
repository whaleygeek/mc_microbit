# fontwriter.py  30/11/2015  D.J.Whale
#
# Write text in minecraft, using fonts

#---- _FONTWRITER -----------------------------------------------------------------------

class _FontWriter():
    RIGHT_X        = "+x"
    LEFT_X         = "-x"
    RIGHT_Y        = "+y"
    LEFT_Y         = "-y"
    RIGHT_Z        = "+z"
    LEFT_Z         = "-z"

    DOWN_X         = "+x"
    DOWN_X_INVERT  = "-x"
    DOWN_Y         = "-y"
    DOWN_Y_INVERT  = "+y"
    DOWN_Z         = "+z"
    DOWN_Z_INVERT  = "-z"

    PAD            = 1 # inter char pad

    PIXEL_DELAY    = 0
    
    def __init__(self, mc=None, font=None):
        if mc != None:
            self.mc = mc
        else:
            import mcpi.minecraft as minecraft
            self.mc = minecraft.Minecraft.create()

        if font != None:
            self.font = font
        else:
            import fonts
            self.font = fonts.microbitFont 

        self.wscale = 1
        self.hscale = 1
        self.dscale = 1
        self.right  = self.RIGHT_X
        self.down   = self.DOWN_Y
        self.on     = 41     # GOLD BLOCK
        self.off    = 0      # AIR


    def set_scale(self, wscale, hscale, dscale):
        self.wscale = wscale
        self.hscale = hscale
        self.dscale = dscale


    def set_direction(self, right, down):
        self.right = right
        self.down  = down


    def set_blocks(self, on, off):
        self.on  = on
        self.off = off


    def write(self, msg, x=None, y=None, z=None):
        """Write a string message"""

        # Set sensible parameters

        if x == None or y == None or z == None:
            pos = self.mc.player.getTilePos()
            if x == None: x = pos.x
            if y == None: y = pos.y
            if z == None: z = pos.z

        # start at the bottom left corner of the text
        for ch in msg:
            g = self.font.get(ch)
            self.draw(g, x, y, z)
            x, y, z = self.advance_right(x, y, z, (self.font.WIDTH * self.wscale) + self.PAD)


    def draw(self, glyph, x, y, z):
        """Draw a single glyph"""
        #print("draw:%s" % glyph)

        startx, starty, startz = x,y,z

        for p in glyph:
            if p == '\n': # move to start of next row
                if self.right != self.RIGHT_X:
                   raise RuntimeError("not yet implemented")
                x = startx # x back to start of row (CR)
                x,y,z = self.advance_down(x, y, z, self.hscale) # y down to next row (LF)
            else:
                if p == '0': # OFF
                    self.plot_pixel(x, y, z, self.off)
                else:
                    self.plot_pixel(x, y, z, self.on)
                x,y,z = self.advance_right(x, y, z, self.wscale)


    def plot_pixel(self, x, y, z, blockid):
        """Plot a single pixel"""
        #print("plot_pixel: %d,%d,%s=%s" % (x,y,z, str(blockid)))

        if self.wscale == 1 and self.hscale == 1:
            self.mc.setBlock(x, y, z, blockid)
        else:
            if self.right != self.RIGHT_X and self.down != self.DOWN_Y:
                raise RuntimeError("Not yet implemented") # TODO
            self.mc.setBlocks(x, y, z, x+self.hscale, y+self.wscale, z+self.dscale, blockid)
            if self.PIXEL_DELAY != 0:
                import time
                time.sleep(self.PIXEL_DELAY)


    def advance_right(self, xpos, ypos, zpos, amount):
        """Move right by 'amount' pixels"""

        if self.right != self.RIGHT_X:
            raise RuntimeError("not yet implemented") #TODO: based on 'right'
        return xpos+amount, ypos, zpos


    def advance_down(self, xpos, ypos, zpos, amount):
        """Move down by 'amount' pixels"""
    
        if self.down != self.DOWN_Y:
            raise RuntimeError("not yet implemented")
        return xpos, ypos-amount, zpos


#---- FONTWRITER --------------------------------------------------------------------

class FontWriter():
    def __init__(self, mc=None, font=None):
        self.fw = _FontWriter(mc, font)


    def configure(self, wscale, hscale, right, down, on, off):
        self.fw.set_scale(wscale, hscale)
        self.fw.set_direction(right, down)
        self.fw.set_blocks(on, off)


    def write(self, msg, x=None, y=None, z=None, wscale=None, hscale=None, dscale=None, 
        right=None, down=None, on=None, off=None):

        if wscale != None and hscale != None and dscale!=None:
            self.fw.set_scale(wscale, hscale, dscale)
        if right != None and down != None:
            self.fw.set_direction(right, down)
        if on != None and off != None:
            self.fw.set_blocks(on, off)

        self.fw.write(msg, x, y, z)


#----- IDEAS ------------------------------------------------------------------------

# TODO implement a console, so newline processing, backspace processing, cursor processing
# in stored state in x,y,z and also need to process control chars.
# might also need clipping at edges. No scrolling though.
        

#----- TEST HARNESS ---------------------------------------------------------------

def example():
    # Should write 'Hello world' at player position
    f = FontWriter()
    f.write("Hello world")

if __name__ == "__main__":
    example()

# END

