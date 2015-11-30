# fonts.py  26/11/2015  D.J.Whale

class Font():
    def get(self, ch):
        if self.FONTDATA.has_key(ch):
            return self.FONTDATA[ch]
        else:
            return self.FONTDATA[self.U]


    def get_row(self, ch, y):
        d = self.get(ch)
        return d[y*self.WIDTH:y*self.WIDTH+(self.WIDTH)]


    def get_pixel(self, ch, x, y):
        d = self.get(ch)
        return d[x+y*self.WIDTH]


class MicrobitFont(Font):
    WIDTH, HEIGHT = 5,5

    U = 'UNKNOWN'

    FONTDATA = {
      # SYMBOLS

      ' ':"00000\n" \
          "00000\n" \
          "00000\n" \
          "00000\n" \
          "00000\n",

      U:  "11111\n" \
          "10001\n" \
          "10101\n" \
          "10001\n" \
          "11111\n",

      '!':"01000\n" \
          "01000\n" \
          "01000\n" \
          "00000\n" \
          "01000\n",

      '?':"01110\n" \
          "10001\n" \
          "00110\n" \
          "00000\n" \
          "00100\n",

      '>':"01000\n" \
          "00100\n" \
          "00010\n" \
          "00100\n" \
          "01000\n",

      '<':"00010\n" \
          "00100\n" \
          "01000\n" \
          "00100\n" \
          "00010\n",

      '-':"00000\n" \
          "00000\n" \
          "01110\n" \
          "00000\n" \
          "00000\n",

      '+':"00000\n" \
          "00100\n" \
          "01110\n" \
          "00100\n" \
          "00000\n",

      # DIGITS: 0123456789

      '0':"01100\n" \
          "10010\n" \
          "10010\n" \
          "10010\n" \
          "01100\n",

      '1':"00100\n" \
          "01100\n" \
          "00100\n" \
          "00100\n" \
          "01110\n",

      '2':"11100\n" \
          "00010\n" \
          "01100\n" \
          "10000\n" \
          "11110\n",

      '3':"11110\n" \
          "00010\n" \
          "00100\n" \
          "10010\n" \
          "01100\n",

      '4':"00110\n" \
          "01010\n" \
          "10010\n" \
          "11111\n" \
          "00010\n",

      '5':"11111\n" \
          "10000\n" \
          "11110\n" \
          "00001\n" \
          "11110\n",

      '6':"00010\n" \
          "00100\n" \
          "01110\n" \
          "10001\n" \
          "01110\n",

      '7':"11111\n" \
          "00010\n" \
          "00100\n" \
          "01000\n" \
          "10000\n",

      '8':"01110\n" \
          "10001\n" \
          "01110\n" \
          "10001\n" \
          "01110\n",

      '9':"01110\n" \
          "10001\n" \
          "01110\n" \
          "00100\n" \
          "01000\n",

      # UPPER CASE LETTERS: ABCDEFGHIJKLMNOPQRSTUVWXYZ

      'A':"01100\n" \
          "10010\n" \
          "11110\n" \
          "10010\n" \
          "10010\n",

      'B':"11100\n" \
          "10010\n" \
          "11100\n" \
          "10010\n" \
          "11100\n",

      'C':"01110\n" \
          "10000\n" \
          "10000\n" \
          "10000\n" \
          "01110\n",

      'D':"11100\n" \
          "10010\n" \
          "10010\n" \
          "10010\n" \
          "11100\n",

      'E':"11110\n" \
          "10000\n" \
          "11100\n" \
          "10000\n" \
          "11110\n",

      'F':"11110\n" \
          "10000\n" \
          "11100\n" \
          "10000\n" \
          "10000\n",

      'G':"01110\n" \
          "10000\n" \
          "10011\n" \
          "10001\n" \
          "01110\n",

      'H':"10010\n" \
          "10010\n" \
          "11110\n" \
          "10010\n" \
          "10010\n",

      'I':"11100\n" \
          "01000\n" \
          "01000\n" \
          "01000\n" \
          "11100\n",

      'J':"11111\n" \
          "00010\n" \
          "00010\n" \
          "10010\n" \
          "01100\n",

      'K':"10010\n" \
          "10100\n" \
          "11000\n" \
          "10100\n" \
          "10010\n",

      'L':"10000\n" \
          "10000\n" \
          "10000\n" \
          "10000\n" \
          "11110\n",

      'M':"10001\n" \
          "11011\n" \
          "10101\n" \
          "10001\n" \
          "10001\n",

      'N':"10001\n" \
          "11001\n" \
          "10101\n" \
          "10011\n" \
          "10001\n",

      'O':"01100\n" \
          "10010\n" \
          "10010\n" \
          "10010\n" \
          "01100\n",

      'P':"11100\n" \
          "10010\n" \
          "11100\n" \
          "10000\n" \
          "10000\n",

      'Q':"01100\n" \
          "10010\n" \
          "10010\n" \
          "01100\n" \
          "00110\n",

      'R':"11100\n" \
          "10010\n" \
          "11100\n" \
          "10010\n" \
          "10001\n",

      'S':"01110\n" \
          "10000\n" \
          "01100\n" \
          "00010\n" \
          "11100\n",

      'T':"11111\n" \
          "00100\n" \
          "00100\n" \
          "00100\n" \
          "00100\n",

      'U':"10010\n" \
          "10010\n" \
          "10010\n" \
          "10010\n" \
          "01100\n",

      'V':"10001\n" \
          "10001\n" \
          "10001\n" \
          "01010\n" \
          "00100\n",

      'W':"10001\n" \
          "10001\n" \
          "10101\n" \
          "11011\n" \
          "10001\n",

      'X':"10010\n" \
          "10010\n" \
          "01100\n" \
          "10010\n" \
          "10010\n",

      'Y':"10001\n" \
          "01010\n" \
          "00100\n" \
          "00100\n" \
          "00100\n",

      'Z':"11110\n" \
          "00100\n" \
          "01000\n" \
          "10000\n" \
          "11110\n",

      # LOWER CASE LETTERS: abcdefghijklmnopqrstuvwxyz

      'a':"00000\n" \
          "01110\n" \
          "10010\n" \
          "10010\n" \
          "01111\n",

      'b':"10000\n" \
          "10000\n" \
          "11100\n" \
          "10010\n" \
          "11100\n",

      'c':"00000\n" \
          "01110\n" \
          "10000\n" \
          "10000\n" \
          "01110\n",

      'd':"00010\n" \
          "00010\n" \
          "01110\n" \
          "10010\n" \
          "01110\n",

      'e':"01100\n" \
          "10010\n" \
          "11100\n" \
          "10000\n" \
          "01110\n",

      'f':"00110\n" \
          "01000\n" \
          "11100\n" \
          "01000\n" \
          "01000\n",

      'g':"01110\n" \
          "10010\n" \
          "01110\n" \
          "00010\n" \
          "01100\n",

      'h':"10000\n" \
          "10000\n" \
          "11100\n" \
          "10010\n" \
          "10010\n",

      'i':"01000\n" \
          "00000\n" \
          "01000\n" \
          "01000\n" \
          "01000\n",

      'j':"00010\n" \
          "00000\n" \
          "00010\n" \
          "00010\n" \
          "01100\n",

      'k':"10000\n" \
          "10100\n" \
          "11000\n" \
          "10100\n" \
          "10010\n",

      'l':"01000\n" \
          "01000\n" \
          "01000\n" \
          "01000\n" \
          "00110\n",

      'm':"00000\n" \
          "11011\n" \
          "10101\n" \
          "10001\n" \
          "10001\n",

      'n':"00000\n" \
          "11100\n" \
          "10010\n" \
          "10010\n" \
          "10010\n",

      'o':"00000\n" \
          "01100\n" \
          "10010\n" \
          "10010\n" \
          "01100\n",

      'p':"00000\n" \
          "11100\n" \
          "10010\n" \
          "11100\n" \
          "10000\n",

      'q':"00000\n" \
          "01110\n" \
          "10010\n" \
          "01110\n" \
          "00010\n",

      'r':"00000\n" \
          "01110\n" \
          "10000\n" \
          "10000\n" \
          "10000\n",

      's':"00000\n" \
          "00110\n" \
          "01000\n" \
          "00100\n" \
          "11000\n",

      't':"01000\n" \
          "01000\n" \
          "01110\n" \
          "01000\n" \
          "00111\n",

      'u':"00000\n" \
          "10010\n" \
          "10010\n" \
          "10010\n" \
          "01111\n",

      'v':"00000\n" \
          "10001\n" \
          "10001\n" \
          "01010\n" \
          "00100\n",

      'w':"00000\n" \
          "10001\n" \
          "10001\n" \
          "10101\n" \
          "11011\n",

      'x':"00000\n" \
          "10010\n" \
          "01100\n" \
          "01100\n" \
          "10010\n",

      'y':"00000\n" \
          "10001\n" \
          "01010\n" \
          "00100\n" \
          "11000\n",

      'z':"00000\n" \
          "11110\n" \
          "00100\n" \
          "01000\n" \
          "11110\n",
    }

microbitFont = MicrobitFont()


# END
