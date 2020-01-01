class Style:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.bar_width = 0.8
        self.data_colour = '#f00'
        self.axis_font_size = 24
        self.value_font_size = 16
        self.label_font_size = 16
        self.label_angle = 0

        self.show_values = 'all'

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
            dominant-baseline: middle;
            font-size: {self.axis_font_size}px;
        }}
        
        .value {{
            text-anchor: middle;
            font-size: {self.value_font_size}px;
        }}

        .legend_label {{
            text-anchor: {'middle' if self.label_angle == 0 else 'left'};
            dominant-baseline: hanging;
            font-size: {self.value_font_size}px;
        }}
        
        .axis {{
            stroke: black;
            stroke-width: 2px;
        }}'''
