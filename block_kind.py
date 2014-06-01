class BlockKind:
    available_colors = ['blue', 'yellow', 'red', 'green', 'purple', 'orange',
                        'pink', 'teal']

    def __init__(self, color):
        self.color = color

    def __eq__(self, other):
        return self.color == other.color