class Style:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.bar_width = 0.5
        self.data_colour = '#f00'
        self.axis_font_size = 16

        # L U R D
        self.margin = (0.05, 0.1, 0.05, 0.1)

    def __repr__(self):
        return f'Style({self.size!r})'

    @property
    def css(self):
        return f'''.data_colour {{
            fill: {self.data_colour};
        }}
        
        .scale {{
            text-anchor: end;
            font-size: {self.axis_font_size};
        }}'''
