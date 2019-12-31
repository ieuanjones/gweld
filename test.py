from gweld import *
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
