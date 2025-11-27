def decompress_rle(encoded_string):
    result = ""
    counter = ""
    for c in encoded_string:
        if '0'<= c <= '9':
            counter += c
        else:
            result += c*int(counter)
            counter= ""
    return result


print(decompress_rle("3A2B4C"))
print(decompress_rle("1W4B1W"))
print(decompress_rle("10X1Y"))
print(decompress_rle("1A1B1C1D1E"))
print(decompress_rle("12Z"))