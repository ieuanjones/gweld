"""
vis.py
======

Module containing the core visualisation object.
"""

from gweld import Data, Chart, Bar, VisElement, Style
from gweld.svg_lib import to_string

class Vis:
    """
    A visualisation object. The core object worked with to create visualisations.
    """
    def __init__(self, data=Data(), chart=Bar(), elements=[], style=Style()):
        self.data = data
        self.chart = chart
        self.elements = elements
        self.style = style

    def __repr__(self):
        return f'Chart(data={self.data!r}, chart={self.chart!r}, style={self.style!r})'

    def __add__(self, other):
        if isinstance(other, Data):
            return Vis(data=other, chart=self.chart, elements=self.elements, style=self.style)
        if isinstance(other, Chart):
            return Vis(data=self.data, chart=other, elements=self.elements, style=self.style)
        if isinstance(other, VisElement):
            return Vis(data=self.data, chart=self.chart, elements=self.elements+[other], style=other)
        if isinstance(other, Style):
            return Vis(data=self.data, chart=self.chart, elements=self.elements, style=other)
        raise TypeError

    def plot(self):
        tree = self.chart.plot(self)

        for element in self.elements:
            element.plot(tree, self)

        return to_string(tree)
