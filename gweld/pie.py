from gweld.svg_lib import root_tag, add_tag, add_text, to_string
from gweld import Chart
import math

class Pie(Chart):
    def plot(self, vis):
        tree = root_tag(vis.style.width, vis.style.height)
        add_tag(tree, 'style', text=vis.style.css)
        add_tag(tree, 'rect', attributes={'x': '0', 'y': '0', 'width': str(vis.style.width), 'height': str(vis.style.height), 'fill': vis.style.background_colour})

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


        # Plot pie

        angles = self._calculate_angles(vis.data)
        centre = (plot_x[0] + plot_width/2, plot_y[0] + plot_height/2)
        radius = min(plot_width, plot_height)/2 * 0.9

        # SVG paths can't draw full circle. Backtrack to a circle if we
        # get too close
        if len(vis.data) == 1 or max(angles) > 1.99 * math.pi:
            add_tag(tree, 'circle', attributes={
                'cx': str(centre[0]),
                'cy': str(centre[1]),
                'r': str(radius),
                'fill': vis.style.data_colours[0]
            })
        else:
            x = centre[0]
            y = centre[1] - radius
            angle = 0

            for i, item in enumerate(vis.data):
                (old_x, old_y) = (x,y)
                angle += angles[i]
                x = centre[0] + radius * math.sin(angle)
                y = centre[1] + -(radius * math.cos(angle))
                big = 1 if angles[i] > math.pi else 0

                add_tag(tree, 'path', attributes={
                    'd': f'M{centre[0]},{centre[1]} L{old_x},{old_y} A{radius},{radius} 0 {big},1 {x},{y} Z',
                    'fill': vis.style.data_colours[i%len(vis.data)]
                }, text=str((angles[i], angle)))

        add_tag(tree, 'circle', attributes={
            'cx': str(centre[0]),
            'cy': str(centre[1]),
            'r': str(radius * vis.style.pie_inner_radius),
            'fill': vis.style.background_colour
        })

        return to_string(tree)

    def _calculate_angles(self, data):
        angles = []

        for item in data:
            angles.append(2 * math.pi * (item / sum(data)))

        return angles
