attention_sentence = ('Attention can be of two types. One of them is self-attention and the other one is cross-attention.'
                      'They differ in their use cases and are essential for encoder and decoder architecture')

chars = sorted(list(set(attention_sentence)))

attention_list = ['self-attention', 'query', 'key', 'values', 'softmax', 'layer_norm', 'residual_connection']

# for index, ele in enumerate(attention_list):
#     print(ele, index)

# for index, ele in enumerate(chars):
#     print(ele, index)

element_wise_dict = {ele:ind for ind,ele in enumerate(chars) } #look up table created
print(element_wise_dict)
print()
mapping_on_look_up_table = {ind:ele for ind,ele in enumerate(chars)}
print(mapping_on_look_up_table)

if __name__ == "__main__":
     pass