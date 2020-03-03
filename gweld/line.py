from gweld.svg_lib import root_tag, add_tag, add_text
from gweld import Chart, DataSet, Data
import math

class Line(Chart):
    def plot(self, vis):
        tree = root_tag(vis.style.width, vis.style.height)
        add_tag(tree, 'style', text=vis.style.css)
        add_tag(tree, 'rect', attributes={'x': '0', 'y': '0', 'width': str(vis.style.width), 'height': str(vis.style.height), 'fill': vis.style.background_colour})

        if len(vis.data) == 0:
            return tree

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

        if isinstance(vis.data, DataSet):
            for i, data in enumerate(vis.data):
                self._plot_line(vis, data, y_scale, plot_x, plot_y, plot_width, plot_height, vis.style.data_colours[i%len(data)], tree)
        elif isinstance(vis.data, Data):
            self._plot_line(vis, vis.data, y_scale, plot_x, plot_y, plot_width, plot_height, vis.style.data_colour, tree)
        else:
            raise Exception

        
        if vis.data.labels:
            for i, label in enumerate(vis.data.labels):
                if not i % vis.style.x_axis_interval:
                    width_per_node = plot_width / (len(data)-1)
                    x = plot_x[0] + i * width_per_node

                    label_y = plot_y[0] + plot_height + vis.style.text_styles["x_axis"].size/2
                    add_text(tree, (x, label_y), str(label), vis.style.text_styles['x_axis'])
        

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

        return tree

    def _plot_line(self, vis, data, y_scale, plot_x, plot_y, plot_width, plot_height, colour, tree):
        width_per_node = plot_width / (len(data)-1)
        points = []

        for i, item in enumerate(data):
            x = plot_x[0] + i * width_per_node
            y = plot_y[0] + plot_height - (item / y_scale[-1]) * plot_height
            points.append((x, y))

            if vis.style.show_values == 'all' or (vis.style.show_values == 'limits' and
                    (item == data.max or item == data.min)):
                label_y = y - vis.style.text_styles["value"].size/2

                add_text(tree, (x, label_y), str(item), vis.style.text_styles['value'])

        add_tag(tree, 'polyline', attributes={
            'points': ' '.join([f'{str(point[0])}, {str(point[1])}' for point in points]),
            'fill': 'none',
            'stroke': colour,
            'class': 'line_chart_data_line'
        })

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
