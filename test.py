from lxml import etree

root = etree.Element('svg')
root.set('width', '300')
root.set('height', '200')
root.set('xmlns', 'http://www.w3.org/2000/svg')

rect = etree.SubElement(root, 'rect')
rect.set('width', '50')
rect.set('height', '100')
rect.set('x', '50')
rect.set('y', '100')
rect.set('fill', 'red')

print(etree.tostring(root, pretty_print=True))

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

class Chart:
    def plot(self):
        pass

class Bar(Chart):
    def plot(self):
        pass

    def __repr__(self):
        return 'Bar()'

class Data:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f'Data({self.data!r})'

class Style:
    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return f'Style({self.val!r})'

a = Vis()
b = Data([1,2,3,4,5])
c = Bar()
d = Style('red')

print(a)
print(b)
print(c)
print(d)

print('===')
a += b

print(a)
print(b)
print(c)
print(d)

print('===')
a += c
a += d

print(a)
print(b)
print(c)
print(d)
