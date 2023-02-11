# def win(ls):
#     for i in range(3):
#         if len(set(ls[i])) == 1 and ls[i][0] != 0:
#                 return True
#     new_mat = []
#     row = []
#     for i in range(3):
#         for j in range(3):
#             row.append(ls[j][i])
#         new_mat.append(row)
#         row = []
#     for i in range(3):
#         if len(set(new_mat[i])) == 1 and ls[i][0] != 0:
#             return True
#     if len(set([ls[i][i] for i in range(3)])) == 1 and ls[1][1] != 0:
#         return True
#     elif len(set([ls[i][2 - i] for i in range(3)])) == 1 and ls[1][1] != 0:
#         return True
#     else:
#         return False
    

# def tictac():
#     ls = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#     choices = ['{},{}'.format(i, j) for i in range(3) for j in range(3)]
    
    
#     while not win(ls) or choices == []:
#         x = str(input("Please enter the position of x in one of those options \n{}\n".format(choices)))
#         while x not in choices:
#             x = str(input("Please enter valid option "))
#         choices.remove(x)
#         ls[int(x[0])][int(x[2])] = 1
#         for i in range(3):
#             print(ls[i])
#         if win(ls):
#             for i in range(3):
#                 print(ls[i])
#             return 'X wins'

#         o = str(input("Please enter the position of o in one of those options \n{}\n".format(choices)))
#         while o not in choices:
#             o = str(input("Please enter valid option "))
#         choices.remove(o)
#         ls[int(o[0])][int(o[2])] = 2
#         for i in range(3):
#             print(ls[i])
#         if win(ls):
#             for i in range(3):
#                 print(ls[i])
#             return 'O wins'

#     if choices == []:
#         return 'Draw'
    

# print(tictac())

# import random
# import time

# questions = [    "What is the formula for water?",    "What is the basic unit of life?",    "What is the study of human behavior called?",    "What is the name of the first computer?",    "What is the most abundant gas in Earth's atmosphere?",    "What is the name of the currency used in the European Union?",    "What is the process of photosynthesis?",    "What is the smallest bone in the human body?",    "What is the name of the world's largest land mammal?",    "What is the name of the famous Shakespearean tragedy about two star-crossed lovers?"]

# answers = [    "H2O",    "Cell",    "Psychology",    "ENIAC",    "Nitrogen",    "Euro",    "Conversion",    "Stirrup",    "Elephant",    "RomeoJuliet"]

# def quiz():
#     score = 0
#     count = 0
#     dic = dict(zip(questions,answers))
#     print('Welcome to a small quiz! \n For each right answer you get 2 points, for a wrong -1.')
#     for i in range(len(dic)):
#         x = random.choice(list(dic.keys()))
#         time.sleep(1)
#         ans = str(input("The {} queston is` \n {} \n".format(i + 1, x)))
#         time.sleep(1)

#         if ans == dic[x]:
#             print('Right!')
#             count += 1
#             score += 2

#         else:
#             print('Wrong!')
#             score -= 1

#         dic.pop(x)

#     return "You answered {} right questions, and your score is {}".format(count, score)

# print(quiz())
        
ls = [('1', '2'), ('2', '3', '5'), ('3', '4'), ('2', '3', '4', '2')]

for i in range(len(ls)):
    ls[i] = list(ls[i])
    for j in range(len(ls[i])):
        ls[i][j] = int(ls[i][j])

print(ls)


