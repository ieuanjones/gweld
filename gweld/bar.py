from gweld.svg_lib import root_tag, add_tag, to_string
from gweld import Chart
import math

class Bar(Chart):
    def plot(self):
        pass

    def __repr__(self):
        return 'Bar()'

    def plot(self, vis):
        tree = root_tag(vis.style.width, vis.style.height)
        add_tag(tree, 'style', text=vis.style.css)
        add_tag(tree, 'rect', attributes={'x': '0', 'y': '0', 'width': str(vis.style.width), 'height': str(vis.style.height), 'fill': '#efefef'})

        # Left, Right
        plot_x = (
            vis.style.width * vis.style.margin[0],
            vis.style.width * vis.style.margin[2]
        )
        # Up, Down
        plot_y = (
            vis.style.height * vis.style.margin[1],
            vis.style.height * vis.style.margin[3]
        )

        plot_width = vis.style.width - plot_x[0] - plot_x[1]
        plot_height = vis.style.height - plot_y[0] - plot_y[1]

        y_scale = self._calculate_y_scale(vis.data, 6)

        width_per_bar = plot_width / len(vis.data)
        bar_width = width_per_bar * vis.style.bar_width

        for i, item in enumerate(vis.data):
            height = (item / y_scale[-1]) * plot_height
            centre_x = plot_x[0] + i * width_per_bar + width_per_bar/2

            add_tag(tree, 'rect', attributes={
                'width': str(bar_width),
                'height': str(height),
                'x': str(centre_x - bar_width/2),
                'y': str(plot_y[0] + plot_height - height),
                'class': 'data_colour'
            })

            if vis.style.show_values == 'all' or (vis.style.show_values == 'limits' and
                    (item == vis.data.max or item == vis.data.min)):
                add_tag(tree, 'text', attributes={
                    'x': str(centre_x),
                    'y': str(plot_y[0] + plot_height - height - vis.style.text_styles["value"].size/2),
                    'class': 'value_label'
                }, text=str(item))

            if vis.data.labels:
                label_y = plot_y[0] + plot_height + vis.style.text_styles["x_axis"].size/2
                add_tag(tree, 'text', attributes={
                    'x': str(centre_x),
                    'y': str(label_y),
                    'transform': f'rotate({vis.style.text_styles["x_axis"].angle} {centre_x} {label_y})',
                    'class': 'x_axis_label'
                }, text=str(vis.data.labels[i]))


        # Axes
        
        add_tag(tree, 'line', attributes={
            'x1': str(plot_x[0]),
            'x2': str(plot_x[0]),
            'y1': str(plot_y[0] + plot_height),
            'y2': str(plot_y[0]),
            'class': 'axis'
        })
        
        add_tag(tree, 'line', attributes={
            'x1': str(plot_x[0]),
            'x2': str(plot_x[0] + plot_width),
            'y1': str(plot_y[0] + plot_height),
            'y2': str(plot_y[0] + plot_height),
            'class': 'axis'
        })
        
        for i, label in enumerate(y_scale):
            add_tag(tree, 'text', attributes={
                'x': str(plot_x[0] - 5),
                'y': str(plot_y[0] + plot_height - i * plot_height/(len(y_scale)-1)),
                'class': 'y_axis_label'
            }, text=str(label))

        return to_string(tree)

    def _calculate_y_scale(self, data, tick_count=5):
        # Algorithm from: https://stackoverflow.com/a/326746
        lower_bound = 0 # No support for negative numbers.... yet
        upper_bound = data.max
        data_range = upper_bound - lower_bound
        coarse_tick_size = data_range / (tick_count-1)
        magnitude = math.ceil(math.log(coarse_tick_size, 10)) # Yay floating point arithmetic!

        for tick_size in [0.1, 0.125, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.7, 0.75, 0.8, 0.9, 1]:
            if coarse_tick_size/10**magnitude <= tick_size:
                tick_size *= 10**magnitude
                break

        if not tick_size % 1:
            tick_size = int(tick_size)

        scale = [0]
        while tick_count-1 > 0:
            scale.append(round(scale[-1]+tick_size, 3))

            if scale[-1] > upper_bound:
                break
            tick_count -= 1

        return scale
