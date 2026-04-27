
model= dict(
    type = 'spade',
    num_queries = 900,
    embed_dim = 256,
    dropout = 0.2
)

new_model = model.copy()
class_name = new_model.pop('type')


if __name__ == "__main__":
    print(class_name)
