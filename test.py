from gweld import *
import random

# Text styles
x_axis_text = TextStyle('x_axis')
x_axis_text.size = 16
x_axis_text.baseline = 'hanging'
x_axis_text.anchor = 'middle'
#x_axis_text.angle = 45 

y_axis_text = TextStyle('y_axis')
y_axis_text.size = 24
y_axis_text.baseline = 'middle'
y_axis_text.anchor = 'end'

value_text = TextStyle('value')
value_text.size = 16
value_text.anchor = 'middle'

# Make style
test_style = Style(width=1200, height=700)
test_style.data_colour = '#a7a7a7'

test_style += x_axis_text
test_style += y_axis_text
test_style += value_text

# Generate the data
label_list = ('red','yellow','green','blue','black','white','grey','orange','pink','cyan','brown','purple','magenta')
labels = [random.choice(label_list) for i in range(25)]

# Generate the visualisation
vis = Vis()
vis += Data([(random.randint(0,250)+random.randint(0,250))//2 for i in range(25)], labels=labels[:25])
vis += Bar()
vis += test_style

#print(list(Bar()._calculate_y_scale(Data([.61]), 6)))

print(vis.plot().decode('utf-8'))
