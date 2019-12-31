from gweld.svg_lib import root_tag, add_tag, to_string

from gweld import Chart

class Bar(Chart):
    def plot(self):
        pass

    def __repr__(self):
        return 'Bar()'

    def plot(self, vis):
        tree = root_tag(vis.style.width, vis.style.height)
        add_tag(tree, 'style', text=vis.style.css)

        width_per_bar = vis.style.width / len(vis.data)
        bar_width = width_per_bar * vis.style.bar_width

        for i, item in enumerate(vis.data):
            height = (item / vis.data.max) * vis.style.height

            add_tag(tree, 'rect', attributes={
                'width': str(bar_width),
                'height': str(height),
                'x': str(i * width_per_bar + (1-vis.style.bar_width) * width_per_bar),
                'y': str(vis.style.height - height),
                'class': 'data_colour'}
            )

        return to_string(tree)
