from gweld import *
import random
import math

# Text styles
x_axis_text = TextStyle('x_axis')
x_axis_text.size = 16
x_axis_text.baseline = 'hanging'
x_axis_text.anchor = 'middle'
x_axis_text.base_offset = 8
#x_axis_text.angle = 45 

y_axis_text = TextStyle('y_axis')
y_axis_text.size = 24
y_axis_text.baseline = 'middle'
y_axis_text.anchor = 'end'

value_text = TextStyle('value')
value_text.size = 16
#value_text.anchor = 'middle'
value_text.format = lambda x: f'{round(float(x), 2)}'

centre_text = TextStyle('centre')
centre_text.size = 64
centre_text.anchor = 'middle'
centre_text.baseline = 'middle'

# Make style
test_style = Style(width=1200, height=700)
test_style.bar_width = 0.5
#test_style.x_axis_interval = 50
#test_style.data_colour = '#a7a7a7'

test_style += x_axis_text
test_style += y_axis_text
test_style += value_text
test_style += centre_text
test_style.x_axis_interval = 50

# Generate the data
label_list = ('red','yellow','green','blue','black','white','grey','orange','pink','cyan','brown','purple','magenta')
labels = [random.choice(label_list) for i in range(25)]
max_size = random.randint(25,1000)

data_set = DataSet(labels=[str(i) for i in range(501)])
for i in range(5):
    d = [random.randint(500, 750)]
    direction = 0
    for j in range(500):
        if not random.randint(0, 5) or (direction < 0 and not random.randint(0,2)):
            direction += math.floor(random.randint(-10, 10) + random.randint(-10, 10)/2)
            direction = max(-15, min(direction, 25))
        d.append(max(0, d[-1]+direction))
    #d = [(random.randint(0,max_size)+random.randint(0,max_size))//2 for i in range(10)]
    #d = [100 * i/sum(d) for i in d]
    d = Data(d)
    data_set += d

d = [(random.randint(0, max_size)+random.randint(0,max_size))//2 for i in range(10)]
data = Data(d, labels=labels[:10])

# Generate the visualisation
vis = Vis()
vis += data_set
vis += Line()
#vis += TextElement('574', (0.5, 0.5), centre_text)
vis += test_style

#print(list(Bar()._calculate_y_scale(Data([.61]), 6)))

with open('out.svg', 'w') as f:
    f.write(vis.plot().decode('utf-8'))
