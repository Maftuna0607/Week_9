def reverse_words(sentence):
    list_of_words = sentence.split()
    reversed_words = []
    for word in list_of_words:
        reversed_words.append(word[::-1])
    new=" ".join(reversed_words)
    result = ""
    counter=0
    for c in sentence:
        if c == " ":
            result += " "
        else:
            result += reversed_words[counter]
            counter +=1
    return result



print(reverse_words("Hello World"))
print(reverse_words("Python is fun!"))
print(reverse_words("This is a  test   with   multiple spaces"))
print(reverse_words("s'teL    ecitcarp"))