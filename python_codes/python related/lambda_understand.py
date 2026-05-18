attention_sentence = ('Attention can be of two types. One of them is self-attention and the other one is cross-attention.'
                      'They differ in their use cases and are essential for encoder and decoder architecture')

chars = sorted(list(set(attention_sentence)))

lookup_table = { ch:i for i, ch in enumerate(chars)}
corresponding_map = {i:ch for i , ch in enumerate(chars)}
encode = lambda s : [lookup_table[ind] for ind in s]
decode = lambda l : "".join([corresponding_map[ind] for ind in l])

if __name__ == "__main__":
     print(encode('attention'))
     print(decode([0,1,2,5,7,19,22]))