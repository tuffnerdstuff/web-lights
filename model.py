'''
Created on 05.12.2014

@author: stefan
'''

def build_bar(pixels, start_ch, step_offset, r_offset, g_offset, b_offset):
    bar = Bar()
    ch = start_ch
    
    for off in range(0,pixels):
        bar.add_pixel(Pixel(ch+r_offset,ch+g_offset,ch+b_offset))
        ch += step_offset
    
    return bar

class Pixel:
    def __init__(self,ch_r,ch_g,ch_b):
        self.ch_r = ch_r
        self.ch_g = ch_g
        self.ch_b = ch_b
        
    def set_color(self,r,g,b):
        self.r = r
        self.g = g
        self.b = b
        
    def get_color(self):
        return (self.r,self.g,self.b)
    
    def get_color_channels(self):
        return (self.ch_r,self.ch_g,self.ch_b)
    
class Bar:
    def __init__(self):
        self.pixels = []
        
    def add_pixel(self,pixel):
        self.pixels.append(pixel)
    
    def get_pixels(self):
        return self.pixels
    
    
        
    
