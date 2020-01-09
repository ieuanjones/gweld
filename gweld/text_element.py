from gweld.svg_lib import add_text
from gweld import VisElement

class TextElement(VisElement):
    def __init__(self, text, pos, style):
        self.text = text
        self.pos = pos
        self.style = style

    def plot(self, tree, vis):
        # Left, Right
        margin_x = (
            vis.style.width * vis.style.margin[0],
            vis.style.width * vis.style.margin[2]
        )
        # Up, Down
        margin_y = (
            vis.style.height * vis.style.margin[1],
            vis.style.height * vis.style.margin[3]
        )

        plot_width = vis.style.width - margin_x[0] - margin_x[1]
        plot_height = vis.style.height - margin_y[0] - margin_y[1]

        x = plot_width * self.pos[0] + margin_x[0]
        y = plot_height * self.pos[1] + margin_y[0]

        add_text(tree, (x, y), self.text, self.style)
