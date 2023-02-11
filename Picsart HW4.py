# print([x for x in range(100,1001) if str(x)[::-1] == str(x)])

# matrix = [[1, 2, 3] ,[4, 5, 6] ,[7, 8, 9] ,[10, 11, 12], [13, 14, 15]]

# for i in range(round(len(matrix)/2)):
#     for j in range(len(matrix[i])):
#         matrix[i][j], matrix[len(matrix)-(i+1)][len(matrix[i])-(j+1)] = matrix[len(matrix)-(i+1)][len(matrix[i])-(j+1)], matrix[i][j]
# if len(matrix) % 2 != 0:
#     mid = int((len(matrix) - 1)/2)
#     for i in range(round(len(matrix[mid])/2)):
#         matrix[mid][i], matrix[mid][len(matrix[mid])-(i+1)] = matrix[mid][len(matrix[mid])-(i+1)], matrix[mid][i]

# print(matrix)

# matrix = [[1, 2, 3] ,[4, 5, 6] ,[7, 8, 9] ,[10, 11, 12], [13, 14, 15]]

# new_mat = []
# row = []
# for i in range(len(matrix[0])):
#     for j in range(len(matrix)):
#         row.append(matrix[j][i])
#     new_mat.append(row)
#     row = []
    
# print(new_mat)

# def two_pow(n):
#     while n != 1:
#         if n % 2 != 0:
#             return False
#         n = n / 2
#     return True

# print(two_pow(1024))

# def one_count(n):
#     if n == 0:
#         return 0
#     count = 1
#     while n != 1:
#         if n % 2 != 0:
#             count += 1
#             n //= 2
#         else:
#             n //= 2
#     return count

# print(one_count(255))





