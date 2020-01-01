from gweld import *
import random

test_style = Style(width=1200, height=700)
test_style.data_colour = '#a7a7a7'
test_style.label_angle = 45

label_list = ('red','yellow','green','blue','black','white','grey','orange','pink','cyan','brown','purple','magenta')
labels = [random.choice(label_list) for i in range(25)]

vis = Vis()
vis += Data([(random.randint(0,250)+random.randint(0,250))//2 for i in range(25)], labels=labels[:25])
vis += Bar()
vis += test_style

#print(list(Bar()._calculate_y_scale(Data([.61]), 6)))

print(vis.plot().decode('utf-8'))
