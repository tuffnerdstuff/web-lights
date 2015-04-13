'''
Created on 05.12.2014

@author: stefan
'''
import unittest, model


class TestModels(unittest.TestCase):


    def test_build_bar(self):
        bar = model.build_bar(3, 0, 3, 0, 1, 2)
        pixels = bar.get_pixels()
        self.assertTrue(len(pixels) == 3)
        self.assertTrue(pixels[0].get_color_channels() == (0,1,2), pixels[0].get_color_channels())
        self.assertTrue(pixels[-1].get_color_channels() == (6,7,8), pixels[-1].get_color_channels())
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()