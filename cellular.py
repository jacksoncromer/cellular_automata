import pyglet
from rule90 import RULE_90
from pyglet import clock
from time import time
from pyglet.window import key
from pyglet.gl import *
import sys

# Random Cellular Automata 
# By Jackson Cromer
# This program creates many different cellular automata
# There are many different functions for generating these
#
# Uncomment out the one you want to see, comment out all others:
#
# m_rule, m_draw - One cellular automata (the best looking and is uncommented already)
# un_rule, un_ draw - 4 cellular automata
# rule, draw - 2 cellular automata
# alt_rule, alt_draw - 2 cellular automata in a different way

name = ""
class Window(pyglet.window.Window):
    frame_num = 0

    def __init__(self):
        res = 600
        pixel_size = 2
        super().__init__(res, res)
        self.cellular_rule_90 = RULE_90(res, res, pixel_size)

        self.cellular_rule_90.m_rule()
        #self.cellular_rule_90.un_rule()
        #self.cellular_rule_90.alt_rule()
        #self.cellular_rule_90.rule()

        pyglet.clock.schedule_interval(self.update, 1.0/15.0)
        
    def on_draw(self):
        self.clear()

        ## Only have one of these lines uncommented
        self.cellular_rule_90.m_draw()
        #self.cellular_rule_90.un_draw()
        #self.cellular_rule_90.alt_draw()
        #self.cellular_rule_90.draw()
        ##

        Window.frame_num += 1
        new_fname = "%s%s%s.png" % (name, "_",Window.frame_num)
        pyglet.image.get_buffer_manager().get_color_buffer().save("C:\\Users\\jacks\\Desktop\\cell_pics\\%s" %(new_fname))
        
        
    def update(self, dt):

        ## 1 unique cellular automata 
        self.cellular_rule_90.m_draw()
        self.cellular_rule_90.m_rule()

        ## 2 unique cellular automata in a different way
        #self.cellular_rule_90.alt_draw()
        #self.cellular_rule_90.alt_rule()

        ## 4 unique cellular automata
        #self.cellular_rule_90.un_draw()
        #self.cellular_rule_90.un_rule()

        ## 2 unique cellular automata
        #self.cellular_rule_90.draw()
        #self.cellular_rule_90.rule()

    ## closes the window after an amount of time
    def exit_callback(self, dt):
        self.close()

    ## press [ESC] to close the window
    def on_key_press(self, symbol, modifiers):
        if symbol == key.ESCAPE: # [ESC]
            self.close()
    
if __name__ == "__main__":
    print("\n")
    print(" ____________________________________________________________________________________________ ")
    print("|                                                                                            |")
    print("| This program will generate unique cellular automata.                                       |")
    print("| The frame number and .png will be appended end of the file name automatically:             |")    
    print("| (EX: MyFile_1.png, MyFile_2.png)                                                           |")                         
    print("|                                                                                            |")
    print("|____________________________________________________________________________________________|")
    name = input("\nName the image. No extension: (EX: MyFile ): ")
    window = Window()
    pyglet.clock.schedule_once(window.exit_callback , 15) 
    pyglet.app.run()
