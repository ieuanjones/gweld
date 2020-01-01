from gweld import TextStyle

class Style:
    def __init__(self, width=640, height=480):
        self.width = width
        self.height = height
        self.bar_width = 0.8
        self.data_colour = '#f00'
        self.data_colours = ['#ed4334','#27ca42','#2546eb','#eadc45','#faab43']
        self.background_colour = '#efefef'
        self.axis_font_size = 24
        self.x_axis_interval = 2 # Show every n items on the x axis
        self.pie_inner_radius = 0.5 # Move out to separate function in future

        self.text_styles = {
            'x_axis': TextStyle('x_axis'),
            'y_axis': TextStyle('y_axis'),
            'value': TextStyle('value')
        }
        self.show_values = 'limits'

        # L U R D
        self.margin = (0.05, 0.05, 0.05, 0.1)

    def __iadd__(self, other):
        if isinstance(other, TextStyle):
            if other.text_type:
                self.text_styles[other.text_type] = other
            else:
                print(f'Invalid text_type: TextStyle({other.text_type})')
                raise TypeError
        else:
            raise TypeError

        return self

    @property
    def css(self):
        css = f'''
        .data_colour {{
            fill: {self.data_colour};
        }}
        
        .axis {{
            stroke: black;
            stroke-width: 2px;
        }}
        '''

        for text_type in self.text_styles:
            css += self.text_styles[text_type].css

        return css
