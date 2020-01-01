Gweld
=====

Gweld is designed to be a lightweight and flexible charting library for Python.

In Gweld, the fundamental unit is a Vis object - referencing a Visualisation. To
this data, styles, and chart types are added in order to change the final
output.

Probably the best way to understand the library is to follow the examples below:

A Small Tutorial
================

The Basics
----------

As mentioned above, we start off by instantiating a `Vis()` object, before
augmenting it with various attributes. The first thing we want to add to our
visualisation is the data we want to visualise. This is contained in a `Data()`
object.

Invoke the `plot()` method of the visualisation to get the SVG output.

```python
from gweld import Vis, Data

chart = Vis()
chart += Data(data=[12,24,7,19], labels=['Iestyn','Angharad','Gwenllian','Llewellyn'])
svg = chart.plot()
```

This produces a bar chart. This is the default type for a visualisation. We can
formalise this by adding a `Bar()` object to our visualisation. Similarly, we
can display alternative chart types by adding that chart to our visualisation.
For a pie chart:

```python
from gweld import Vis, Data, Pie

chart = Vis()
chart += Pie()
chart += Data(data=[12,24,7,19], labels=['Iestyn','Angharad','Gwenllian','Llewellyn'])
svg = chart.plot()
```

**Note**: the order in which we add things to the visualisation does not matter,
if multiple charts or datasets are added, we only use the last one added before
plotting.

Styling
-------

Styles are applied by adding a `Style()` class. Here first we'll want to create
a `Style()` object and set all the attributes we want to change before adding it
to our visualisation. In this way we can re-use styles across multiple
visualisations.

Take a look in `gweld/style.py` for the full list of attributes that can be set,
as these are being extended regularly.

```python
from gweld import Vis, Data, Bar, Style

my_style = Style(width=1200, height=700)
my_style.bar_width = 0.9
my_style.data_colour = '#a7a7a7'

chart = Vis()
chart += Bar()
chart += Data(data=[12,24,7,19], labels=['Iestyn','Angharad','Gwenllian','Llewellyn'])
chart += my_style
svg = chart.plot()
```

This overrides the default width for bars in the bar chart, and changes the
colour of the bars. Once we've created our style, we add it to our visualisation
as before.

Styling Text
------------

Text styles are applied on a per class basis. We create a `TextStyle()` class,
and add it to our style.

```python
from gweld import TextStyle

x_axis_text = TextStyle('x_axis')
x_axis_text.baseline = 'hanging'
x_axis_text.angle = 45 

my_style += x_axis_text
```

Here we set the baseline to hanging - that is, the text appears below its
baseline as opposed to above as is the default. We also set the angle to 45% to
allow enough space for each label to fit. Then, as always, we add our text style
to our style.

**Note:** When the angle is greater than 0, the text is aligned on the
`angle_anchor` field, and not the `anchor` field. This defaults to `start`.

As with styles, the easiest way to find all the attributes which can be adjusted
is in the `gweld/text_style.py` file. All the classes of text which can be
adjusted are found in `gweld/style.py`.
