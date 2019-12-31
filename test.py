from gweld import *
import random

test_style = Style(width=1200, height=700)
test_style.bar_width = 0.9
test_style.data_colour = '#a7a7a7'

vis = Vis()
vis += Data([random.randint(0,10) for i in range(25)])
vis += Bar()
vis += test_style

#print(list(Bar()._calculate_y_scale(Data([.61]), 6)))

print(vis.plot().decode('utf-8'))
