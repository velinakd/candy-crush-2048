class Block:

    def __init__(self, kind):
        self.kind = kind

    def __eq__(self, other):
        return self.kind == other.kind
