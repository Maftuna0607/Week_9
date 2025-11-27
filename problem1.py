def are_anagrams(string1, string2):
    string1=string1.lower().replace(" ","").replace(".","")
    string2=string2.lower().replace(" ","").replace(".","")
    l1=list(string1)
    l2=list(string2)
    l1.sort()
    l2.sort()
    s1= "".join(l1)
    s2="".join(l2)
    print(s1)
    print(s2)
    if s1==s2:
        return True
    return False
print(are_anagrams("Listen", "Silent"))
print(are_anagrams("The Morse Code", "Here come dots"))
print(are_anagrams("Astronomer", "Moon starer"))
print(are_anagrams("Hello", "World"))
print(are_anagrams("Dormitory", "Dirty room."))