
class Registry:
    def __init__(self, name):
        self.name = name
        self._registry = {}


    def register(self,cls):
        self._registry[cls.__name__] = cls
        return cls

    def __getitem__(self,name):
        return self._registry[name]


SHAPES = Registry('shapes')

@SHAPES.register
class Circle:
    def __init__(self, radius): self.radius = radius
    def area(self): return 3.14*self.radius **2

@SHAPES.register
class Square:
    def __init__(self,side): self.side = side
    def area(self): return self.side**2

def build(cfg):
    cfg = cfg.copy()
    cls = SHAPES[cfg.pop('type')]
    return cls(**cfg)


if __name__ == "__main__":
    circle = build(dict(type='Circle', radius=5))
    square = build(dict(type='Square', side=4))

    print(circle.area())
    print(square.area())