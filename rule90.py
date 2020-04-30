import pyglet
from random import randrange

class RULE_90:
    
## Lists and functions
    
    ## Generates a random rule list. 
    ## To make sure the rule isn't boring, the rule will be reset and try again.
    def rule_random(self):
        count = 0
        while count < 5:
            RULE_90.rulelist = []
            RULE_90.rulelist.append(0)
            count = 0
            for xx in range(0, 10):
                RULE_90.rulelist.append(randrange(2))
                if RULE_90.rulelist[xx] == 1:
                    count += 1
    
    rulelist = [0, 0, 1, 0, 1, 1, 0, 1]
    
    rule3 = []

    ## The next rulelist will not be the same as the last one.
    def proc_gen(self):
        RULE_90.rules3 = RULE_90.rulelist
        while RULE_90.rulelist == RULE_90.rules3:
            self.rule_random()
       
    def __init__(self, widow_width,  widow_high, pix):
        self.width = int(widow_width/ pix)
        self.height = int(widow_high/ pix)
        self.pix = pix
        self.arr = []
        self.sq1()
        self.arr2 = []
        self.sq2()
        self.arr3 = []
        self.sq3()
        self.arr4 = []
        self.sq4()

## These functions initialize the starting point of the cellular automata
    def sq1(self):
        for y in range(0, self.height):
            self.arr.append([])
            for x in range(0, self.width):
                self.arr[y].append(0)
        self.arr[int(self.height/2)][int(len(self.arr)/2)] = 1

    def sq3(self):
        for y in range(0, self.height):
            self.arr3.append([])
            for x in range(0, self.width):
                self.arr3[y].append(0)
        self.arr3[int(self.height/2)][int(len(self.arr3)/2)] = 1

    def sq2(self):
        for y in range(0, self.height):
            self.arr2.append([])
            for x in range(0, self.width):
                self.arr2[y].append(0)
        self.arr2[int(self.height/2)][int(len(self.arr2)/2)] = 1  

    def sq4(self):
        for y in range(0, self.height):
            self.arr4.append([])
            for x in range(0, self.width):
                self.arr4[y].append(0)
        self.arr4[int(self.height/2)][int(len(self.arr4)/2)] = 1           


    #computes an index in the random rule list, returns (0 or 1) 
    def binaryToDec(self, l, c, r):
        string_bin = "%s%s%s" % (l, r, c)
        dec = int(string_bin, base=2)
        ri = RULE_90.rulelist[dec]
        return ri

# Rule functions: These functions use the rule lists to decide the next generation of the cellular automata

    # alt_rule (alternative rule): Generates 2 unique cellular automata in a different way
    def alt_rule(self):
        change_index = randrange(0, self.height)
        for y in range(int(self.height/2), self.height):
            rulearry = []
            if y % change_index == 0:
                self.proc_gen()
            for x in range(0, self.width):
                if x < self.width-1 and x > 0:
                    left = self.arr[y][x-1]
                    current = self.arr[y][x]
                    right = self.arr[y][x+1]
                else:
                    left = self.arr[y][x]
                    current = self.arr[y][x]
                    right = self.arr[y][x]
                tp = self.binaryToDec(left, current, right)         
                rulearry.append(tp)
                
            if y < self.height-1:
                self.arr[y+1] = rulearry
            
        for yy in range(int(self.height/2), 0, -1):
            rry = []
            if yy % change_index == 0:
                self.proc_gen()
            for xx in range(0, self.width):
                if xx < self.width-1 and xx > 0:
                    left = self.arr[yy][xx-1]
                    current = self.arr[yy][xx]
                    right = self.arr[yy][xx+1]
                else:
                    left = self.arr[yy][xx]
                    current = self.arr[yy][xx]
                    right = self.arr[yy][xx]
                tp = self.binaryToDec(left, current, right)         
                rry.append(tp)
            if yy > 0:
                self.arr[yy-1] = rry

    # m_rule (mirrored rule): Generates 1 unique cellular automata
    def m_rule(self):
        for y in range(0, self.height):
            if y > 0:
                change_index = randrange(y, self.height)
            if y in range(int(self.height/2), self.height):
                rulearry = []
                if y % change_index == 0:
                    self.proc_gen()
                for x in range(0, self.width):
                    if x < self.width-1 and x > 0:
                        left = self.arr[y][x-1]
                        current = self.arr[y][x]
                        right = self.arr[y][x+1]
                    else:
                        left = self.arr[y][x]
                        current = self.arr[y][x]
                        right = self.arr[y][x]
                    tp = self.binaryToDec(left, current, right)         
                    rulearry.append(tp)
                    
                if y < self.height-1:
                    self.arr[y+1] = rulearry
                
    # rule : Generates 2 unique cellular automata
    def rule(self):
        for y in range(int(self.height/2), self.height):
            rulearry = []
            change_index1 = randrange(int(self.height/2), self.height)
            if y == change_index1:
                self.proc_gen()
            for x in range(0, self.width):
                if x < self.width-1 and x > 0:
                    left = self.arr[y][x-1]
                    current = self.arr[y][x]
                    right = self.arr[y][x+1]
                else:
                    left = self.arr[y][x]
                    current = self.arr[y][x]
                    right = self.arr[y][x]
                tp = self.binaryToDec(left, current, right)         
                rulearry.append(tp)
            
            if y < self.height-1:
                self.arr[y+1] = rulearry
           
        self.proc_gen()
        for yy in range(int(self.height/2), 0, -1):
            rry = []
            change_index = randrange(0, int(self.height/2))
            if yy == change_index:
                self.proc_gen()
            for xx in range(0, self.width):
                if xx < self.width-1 and xx > 0:
                    left = self.arr2[yy][xx-1]
                    current = self.arr2[yy][xx]
                    right = self.arr2[yy][xx+1]
                else:
                    left = self.arr2[yy][xx]
                    current = self.arr2[yy][xx]
                    right = self.arr2[yy][xx]
                tp = self.binaryToDec(left, current, right)         
                rry.append(tp)
            
            if yy > 0:
                self.arr2[yy-1] = rry

    # un_rule (unique rule): Generates 4 unique cellular automata
    def un_rule(self):
        for y in range(int(self.height/2), self.height):
            rulearry = []
            change_index1 = randrange(y, self.height)
            if y == change_index1:
                self.proc_gen()
            for x in range(0, self.width):
                if x < self.width-1 and x > 0:
                    left = self.arr[y][x-1]
                    current = self.arr[y][x]
                    right = self.arr[y][x+1]
                else:
                    left = self.arr[y][x]
                    current = self.arr[y][x]
                    right = self.arr[y][x]
                tp = self.binaryToDec(left, current, right)         
                rulearry.append(tp)
            
            if y < self.height-1:
                self.arr[y+1] = rulearry

        for y in range(int(self.height/2), self.height):
            rulearry = []
            change_index1 = randrange(y, self.height)
            if y == change_index1:
                self.proc_gen()
            for x in range(0, self.width):
                if x < self.width-1 and x > 0:
                    left = self.arr3[y][x-1]
                    current = self.arr3[y][x]
                    right = self.arr3[y][x+1]
                else:
                    left = self.arr3[y][x]
                    current = self.arr3[y][x]
                    right = self.arr3[y][x]
                tp = self.binaryToDec(left, current, right)         
                rulearry.append(tp)
            
            if y < self.height-1:
                self.arr3[y+1] = rulearry
        self.proc_gen()
        for yy in range(int(self.height/2), 0, -1):
            rry = []
            change_index = randrange(0, int(self.height/2))
            if yy == change_index:
                self.proc_gen()
            for xx in range(0, self.width):
                if xx < self.width-1 and xx > 0:
                    left = self.arr2[yy][xx-1]
                    current = self.arr2[yy][xx]
                    right = self.arr2[yy][xx+1]
                else:
                    left = self.arr2[yy][xx]
                    current = self.arr2[yy][xx]
                    right = self.arr2[yy][xx]
                tp = self.binaryToDec(left, current, right)         
                rry.append(tp)
            
            if yy > 0:
                self.arr2[yy-1] = rry
        self.proc_gen()
        for yy in range(int(self.height/2), 0, -1):
            rry = []
            change_index = randrange(0, int(self.height/2))
            if yy == change_index:
                self.proc_gen()
            for xx in range(0, self.width):
                if xx < self.width-1 and xx > 0:
                    left = self.arr4[yy][xx-1]
                    current = self.arr4[yy][xx]
                    right = self.arr4[yy][xx+1]
                else:
                    left = self.arr4[yy][xx]
                    current = self.arr4[yy][xx]
                    right = self.arr4[yy][xx]
                tp = self.binaryToDec(left, current, right)         
                rry.append(tp)
            
            if yy > 0:
                self.arr4[yy-1] = rry  

## Draw functions: These are the draw functions that correspond to each of the rule functions

    #Draws alt_rule
    def alt_draw(self):
        for y in range(0, self.height):
            i = randrange(2, 256)
            j = randrange(2, 256)
            k = randrange(2, 256)
            for x in range(0, self.width):
                if self.arr[y][x] == 1:
                    square_coords = (y * self.pix,                  x * self.pix,
                                    y * self.pix,                  x * self.pix + self.pix,
                                    y * self.pix + self.pix, x * self.pix,
                                    y * self.pix + self.pix, x * self.pix + self.pix)
                    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES, [0, 1, 2, 1, 2, 3], ("v2i", square_coords), ('c3B', (i, j, k, i, j, k, i, j, k,  i, j, k)))
                    square_coords2 = (x * self.pix,                  y * self.pix,
                                    x * self.pix,                  y * self.pix + self.pix,
                                    x * self.pix + self.pix, y * self.pix,
                                    x * self.pix + self.pix, y * self.pix + self.pix)
                    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES, [0, 1, 2, 1, 2, 3], ("v2i", square_coords2), ('c3B', (i, j, k, i, j, k, i, j, k,  i, j, k)))
                    square_coords3 = (y * self.pix,                  x * self.pix,
                                    y * self.pix,                  x * self.pix + self.pix,
                                    y * self.pix, x * self.pix  + self.pix,
                                    y * self.pix, x * self.pix + self.pix)
                    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES, [0, 1, 2, 1, 2, 3], ("v2i", square_coords3), ('c3B', (i, j, k, i, j, k, i, j, k,  i, j, k)))
                    square_coords4 = (x * self.pix,                  y * self.pix,
                                    x * self.pix  + self.pix,                  y * self.pix + self.pix,
                                    x * self.pix, y * self.pix  + self.pix,
                                    x * self.pix, y * self.pix + self.pix)
                    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES, [0, 1, 2, 1, 2, 3], ("v2i", square_coords4), ('c3B', (i, j, k, i, j, k, i, j, k,  i, j, k)))
               
    #Draws rule
    def draw(self):
        for y in range(0, self.height):
            i = randrange(2, 256)
            j = randrange(2, 256)
            k = randrange(2, 256)
            for x in range(0, self.width):
                if self.arr[y][x] == 1:
                    square_coords = (y * self.pix,                  x * self.pix,
                                    y * self.pix,                  x * self.pix + self.pix,
                                    y * self.pix + self.pix, x * self.pix,
                                    y * self.pix + self.pix, x * self.pix + self.pix)
                    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES, [0, 1, 2, 1, 2, 3], ("v2i", square_coords), ('c3B', (i, j, k, i, j, k, i, j, k,  i, j, k)))
                    square_coords2 = (x * self.pix,                  y * self.pix,
                                    x * self.pix,                  y * self.pix + self.pix,
                                    x * self.pix + self.pix, y * self.pix,
                                    x * self.pix + self.pix, y * self.pix + self.pix)
                    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES, [0, 1, 2, 1, 2, 3], ("v2i", square_coords2), ('c3B', (i, j, k, i, j, k, i, j, k,  i, j, k)))
                if self.arr2[y][x] == 1:
                    square_coordz = (y * self.pix,                  x * self.pix,
                                    y * self.pix,                  x * self.pix + self.pix,
                                    y * self.pix + self.pix, x * self.pix,
                                    y * self.pix + self.pix, x * self.pix + self.pix)
                    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES, [0, 1, 2, 1, 2, 3], ("v2i", square_coordz), ('c3B', (i, j, k, i, j, k, i, j, k,  i, j, k)))
                    underside = (x * self.pix,                  y * self.pix,
                                    x * self.pix,                  y * self.pix + self.pix,
                                    x * self.pix + self.pix, y * self.pix,
                                    x * self.pix + self.pix, y * self.pix + self.pix)
                    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES, [0, 1, 2, 1, 2, 3], ("v2i", underside), ('c3B', (i, j, k, i, j, k, i, j, k,  i, j, k)))

    #Draws un_rule
    def un_draw(self):
        for y in range(0, self.height):
            i = randrange(2, 256)
            j = randrange(2, 256)
            k = randrange(2, 256)
            for x in range(0, self.width):
                if self.arr[y][x] == 1:
                    square_coords = (y * self.pix,                  x * self.pix,
                                    y * self.pix,                  x * self.pix + self.pix,
                                    y * self.pix + self.pix, x * self.pix,
                                    y * self.pix + self.pix, x * self.pix + self.pix)
                    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES, [0, 1, 2, 1, 2, 3], ("v2i", square_coords), ('c3B', (i, j, k, i, j, k, i, j, k,  i, j, k)))
                if self.arr3[y][x] == 1:
                    square_coords2 = (x * self.pix,                  y * self.pix,
                                    x * self.pix,                  y * self.pix + self.pix,
                                    x * self.pix + self.pix, y * self.pix,
                                    x * self.pix + self.pix, y * self.pix + self.pix)
                    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES, [0, 1, 2, 1, 2, 3], ("v2i", square_coords2), ('c3B', (i, j, k, i, j, k, i, j, k,  i, j, k)))
                if self.arr2[y][x] == 1:
                    square_coordz = (y * self.pix,                  x * self.pix,
                                    y * self.pix,                  x * self.pix + self.pix,
                                    y * self.pix + self.pix, x * self.pix,
                                    y * self.pix + self.pix, x * self.pix + self.pix)
                    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES, [0, 1, 2, 1, 2, 3], ("v2i", square_coordz), ('c3B', (i, j, k, i, j, k, i, j, k,  i, j, k)))
                if self.arr4[y][x] == 1:
                    underside = (x * self.pix,                  y * self.pix,
                                    x * self.pix,                  y * self.pix + self.pix,
                                    x * self.pix + self.pix, y * self.pix,
                                    x * self.pix + self.pix, y * self.pix + self.pix)
                    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES, [0, 1, 2, 1, 2, 3], ("v2i", underside), ('c3B', (i, j, k, i, j, k, i, j, k,  i, j, k)))

    #Draws m_rule
    def m_draw(self):
        for y in range(0, self.height):
            i = randrange(2, 256)
            j = randrange(2, 256)
            k = randrange(2, 256)
            for x in range(0, self.width):
                if self.arr[y][x] == 1:
                    square_coords = (y * self.pix,                  x * self.pix,
                                    y * self.pix,                  x * self.pix + self.pix,
                                    y * self.pix + self.pix, x * self.pix,
                                    y * self.pix + self.pix, x * self.pix + self.pix)
                    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES, [0, 1, 2, 1, 2, 3], ("v2i", square_coords), ('c3B', (i, j, k, i, j, k, i, j, k,  i, j, k)))
                    square_coords2 = (x * self.pix,                  y * self.pix,
                                    x * self.pix,                  y * self.pix + self.pix,
                                    x * self.pix + self.pix, y * self.pix,
                                    x * self.pix + self.pix, y * self.pix + self.pix)
                    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES, [0, 1, 2, 1, 2, 3], ("v2i", square_coords2), ('c3B', (i, j, k, i, j, k, i, j, k,  i, j, k)))
                    square_coords3 = ((self.height * self.pix) - y * self.pix,                 (self.width * self.pix) - x * self.pix,
                                    (self.height * self.pix) - y * self.pix,                  (self.width * self.pix) - x * self.pix + self.pix,
                                    (self.height * self.pix) - y * self.pix + self.pix,     (self.width * self.pix) - x * self.pix,
                                    (self.height * self.pix) - y * self.pix + self.pix,     (self.width * self.pix) - x * self.pix + self.pix)
                    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES, [0, 1, 2, 1, 2, 3], ("v2i", square_coords3), ('c3B', (i, j, k, i, j, k, i, j, k,  i, j, k)))
                    square_coords4 = ((self.width * self.pix) - x * self.pix,                 (self.height * self.pix) - y * self.pix,
                                    (self.width * self.pix) - x * self.pix,                  (self.height * self.pix) - y * self.pix + self.pix,
                                    (self.width * self.pix) - x * self.pix + self.pix,     (self.height * self.pix) - y * self.pix,
                                    (self.width * self.pix) - x * self.pix + self.pix,     (self.height * self.pix) - y * self.pix + self.pix)
                    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES, [0, 1, 2, 1, 2, 3], ("v2i", square_coords4), ('c3B', (i, j, k, i, j, k, i, j, k,  i, j, k)))