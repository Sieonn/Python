# count, line = 0, 1
# for i in range(65,91): #97 123
#     if line % 2 == 1:
#         print(chr(i), end = '\t')
#     else: print(chr(i+32), end = '\t')
#     # print(chr(1), end ='\t')
#     count += 1
#     if count % 5 ==0:
#         print()
#         line += 1
        
        
# for v 
# in range(97, 123):

cun = 0
for i  in range(65, 91):
    if i % 10 in (5,6,7,8,9):
        print(chr(i).lower(), end=' ')
    else:
        print(chr(i),end=' ') 
    cun += 1 
    if cun % 5 == 0:
        print()
    # cun += 1
    # if i % 10 in (5,6,7,8,9):
    #     print(chr(i).lower(), end=' ')  
    
    
    
# 65 66 67 68 69
# 70 71 72 73 74
# 75 76 78 79 80
