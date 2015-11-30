import mcpi.minecraft as minecraft

def scan(y,x1,z1,x2,z2):
  # the micro:bit is drawn as follows:
  # biggest x to smallest x
  # smallest z to biggest z
  xs = min(x1, x2)
  zs = min(z1, z2)
  xb = max(x1, x2)
  zb = max(z1, z2)

  for x in range(xb, xs-1, -1):
    line = ""
    for z in range(zs, zb+1):
      mc.setBlock(x,y+1,z, 7)
      b,d = mc.getBlockWithData(x,y,z)
      #print(x,y,z,b,d)
      mc.setBlock(x,y+1,z, 0)
      if line != "": line += ','
      line += str(b)
    print(line)


def choose():
  mc.postToChat("Go to bottom left corner")
  raw_input("ready?")
  bl = mc.player.getTilePos()
  print(bl)


  mc.postToChat("Go to top right corner")
  raw_input("ready?")
  tr = mc.player.getTilePos()
  print(tr)


def main():
  bl_x = 19
  bl_y = 231
  bl_z = -28

  tr_x = -33
  tr_y = 231
  tr_z = 10

  scan(bl_y-1, bl_x, bl_z, tr_x, tr_z)

mc = minecraft.Minecraft.create()
main()
