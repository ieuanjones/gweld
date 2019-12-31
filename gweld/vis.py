from gweld import Data, Chart, Style

class Vis:
    def __init__(self, data=None, chart_type=None, style=None):
        self.data = data
        self.chart_type = chart_type
        self.style = style

    def __repr__(self):
        return f'Chart(data={self.data!r}, chart_type={self.chart_type!r}, style={self.style!r})'

    def __add__(self, other):
        if isinstance(other, Data):
            return Vis(data=other, chart_type=self.chart_type, style=self.style)
        if isinstance(other, Chart):
            return Vis(data=self.data, chart_type=other, style=self.style)
        if isinstance(other, Style):
            return Vis(data=self.data, chart_type=self.chart_type, style=other)
        raise TypeError
