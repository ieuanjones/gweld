from gweld import *
import random


test_style = Style(width=500, height=200)
test_style.bar_width = 0.7
test_style.data_colour = '#a7a7a7'

vis = Vis()
vis += Data([random.randint(0,10) for i in range(25)])
vis += Bar()
vis += test_style

print(vis.plot().decode('utf-8'))
