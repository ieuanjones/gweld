from gweld.svg_lib import root_tag, add_tag, add_text, to_string
from gweld import Chart
import math

class Bar(Chart):
    def plot(self, vis):
        tree = root_tag(vis.style.width, vis.style.height)
        add_tag(tree, 'style', text=vis.style.css)
        add_tag(tree, 'rect', attributes={'x': '0', 'y': '0', 'width': str(vis.style.width), 'height': str(vis.style.height), 'fill': vis.style.background_colour})

        if len(vis.data) == 0:
            return to_string(tree)

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

        y_scale = self._calculate_y_scale(vis.data, vis.style.y_axis_tick_number)

        for i in range(len(y_scale)):
            y_pos = plot_y[0] + plot_height - i * plot_height/(len(y_scale)-1)
            if vis.style.show_grid_lines:
                add_tag(tree, 'line', attributes={
                    'x1': str(plot_x[0]),
                    'x2': str(plot_x[0] + plot_width),
                    'y1': str(y_pos),
                    'y2': str(y_pos),
                    'class': 'grid_lines'
                })

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
                label_y = plot_y[0] + plot_height - height - vis.style.text_styles["value"].size/2
                add_text(tree, (centre_x, label_y), str(item), vis.style.text_styles['value'])

            if vis.data.labels:
                if not i % vis.style.x_axis_interval:
                    label_y = plot_y[0] + plot_height + vis.style.text_styles["x_axis"].size/2
                    add_text(tree, (centre_x, label_y), str(vis.data.labels[i]), vis.style.text_styles['x_axis'])

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
            y_pos = plot_y[0] + plot_height - i * plot_height/(len(y_scale)-1)
            add_text(tree, (plot_x[0]-5, y_pos), str(label), vis.style.text_styles['y_axis'])

        return to_string(tree)

    def _calculate_y_scale(self, data, tick_count=5):
        # Algorithm from: https://stackoverflow.com/a/326746
        lower_bound = 0 # No support for negative numbers.... yet
        upper_bound = data.max
        data_range = upper_bound - lower_bound
        coarse_tick_size = data_range / (tick_count-1)
        magnitude = math.ceil(math.log(coarse_tick_size, 10)) # Yay floating point arithmetic!

        for tick_size in [0.1, 0.125, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.7, 0.75, 0.8, 0.9, 1]:
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
