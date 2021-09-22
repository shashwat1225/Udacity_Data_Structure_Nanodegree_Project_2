import sys

def huffman_encoding(data):
    tree_a = {}
    temp = '1'
    tree = {}
    encode = ''
    if data is None:
        return None
    for c in data:
        tree_a[c] = tree_a.get(c, 0) + 1
    for num in sorted(tree_a.items(), key = lambda x: x[1]):
        tree[num[0]] = temp
        temp = '0' + temp
    for d in data:
        encode += tree[d]
    return encode, tree
    pass

def huffman_decoding(data,tree):
    tree_a = {}
    decode = ''
    temp = ''
    for c in tree:
        tree_a[tree[c]] = c
    for d in data:
        if d == '1':
            decode += tree_a[temp + d]
            temp = ''
        else:
            temp += d
    return decode
    pass

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is in the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))



if __name__ == "__main__":
    codes = {}

    a_great_sentence = "AAAAAAAAA"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))


if __name__ == "__main__":
    codes = {}

    a_great_sentence = ""

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(encoded_data)))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

