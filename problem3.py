def reformat_number(phone_number):
    cleaned = phone_number.replace(" ","").replace("-","")
    new_list = []
    for i in range(0,len(cleaned),3):
        new_list.append(cleaned[i:i+3])
    if len(new_list[-1]) == 1:
        new_list[-1]=new_list[-2][-1]+new_list[-1]
        new_list[-2]=new_list[-2][0:2]
    return "-".join(new_list)
       



print(reformat_number("123 456 789"))     # 9 digits -> 3-3-3
print(reformat_number("123-456-7890"))    # 10 digits -> 3-3-2-2 (4 remaining -> 2-2)
print(reformat_number("123 45 678"))      # 8 digits -> 3-3-2
print(reformat_number("12"))              # 2 digits -> 2
print(reformat_number("12345"))           # 5 digits -> 3-2
print(reformat_number("--1 23 4-5 6-7--"))