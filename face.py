class Face:
    mat = None
    pos = None
    id = None

    def __init__(self, image, pos, id):
        self.mat = image
        self.pos = pos
        self.id = id

    def rows(self):
        return len(self.mat)

    def cows(self):
        return len(self.mat[0])