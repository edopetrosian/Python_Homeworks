# sum = ""
# for i in range(5):
#     x = str(input("Please, enter the {}th number = ".format(i+1)))
#     sum += x + '+'

# print(sum[:-1])

# num = str(input("Enter a phone number: "))
# num_lst = list(range(10))

# def num_check(num):
#     if len(num) != 12:
#         if len(num) != 14:
#             return "Invalid"

#     for i in range(len(num)):
#         if i == 3 or i == 7:
#             if num[i] != '-':
#                 return "Invalid"
#         else:
#             if int(num[i]) != 1:
#                 return "Invalid"
#     return "Valid"

# if num[0] == '1' and num[1] == '-':
#     print(num_check(num[2:]))
# else:
#     print(num_check(num))

# def Caesar(char):
#     if ord(char) >= 65 and ord(char) <= 90:
#         return chr((((ord(char) - 65) - 3) % 26) + 65)
#     elif ord(char) >= 97 and ord(char) <= 122:
#         return chr((((ord(char) - 97) - 3) % 26) + 97)
#     else:
#         return char


# txt = str(input("Please, enter your text = "))

# for i in range(len(txt)):
#     txt = txt[:i] + Caesar(txt[i]) + txt[i+1 :]

# print(txt)



# n = int(input("Please, enter the n = "))

# def Fib(n):
#     if n == 0:
#         return 1
#     elif n == 1:
#         return 1
#     else:
#         return Fib(n-1) + Fib(n-2)

# lst = []

# for i in range(n):
#     lst.append(Fib(i))
# print(lst)


# n = str(input("Please, enter the string "))
# new_n = ""
# for i in set(list(n)):
#     new_n += i
# print(new_n)







