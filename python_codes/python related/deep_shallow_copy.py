import copy

class Box:
    def __init__(self, value):
        self.value = value

class Shelf:
    def __init__(self, box):
        self.box = box

original = Box(10)
original_shelf = Shelf(Box(10))


shallow = copy.copy(original)
shallow.value = 99

shallow_shelf = copy.copy(original_shelf)
shallow_shelf.box.value = 99
print(original_shelf.box.value)


deep_shelf = copy.deepcopy(original_shelf)
deep_shelf.box.value = 50
print(original_shelf.box.value)

if __name__ == "__main__":
    print(original.value)

