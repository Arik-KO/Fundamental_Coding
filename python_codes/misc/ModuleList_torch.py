import torch.nn as nn

class BadModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = [nn.Linear(4,4 ) for _ in range(3) ]

bad_example = BadModel()

class GoodModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.ModuleList( [nn.Linear(4,4) for _ in range(3)]                )

good_example = GoodModel()

if __name__ == "__main__":
    print(list(bad_example.parameters()))
    print(list(good_example.parameters()))