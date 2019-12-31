from lxml import etree

def root_tag(width, height):
    return etree.Element('svg', {'width': str(width), 'height': str(height), 'xmlns': 'http://www.w3.org/2000/svg'})

def add_tag(parent, tag, attributes=None, text=None):
    tag = etree.SubElement(parent, tag, attributes)
    tag.text = text
    return tag 

def to_string(tree):
    return etree.tostring(tree, pretty_print=True)
