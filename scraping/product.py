class Product:
    def __init__(self, id=None, url=None, image=None):
        self.id = id
        self.url = url
        self.image = image

    def fromDict(self, d):
        for key in d:
            setattr(self, key, d[key])

    def isIn(self, l):
        for p in l:
            if p.url == self.url:
                return True
        return False
