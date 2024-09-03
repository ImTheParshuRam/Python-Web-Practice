# # file handling : the key fun working is open
# '''acces method '''
# f= open("D:\\work\\Programming\\python practice\\Projectt\\traning\\practice.txt","r")
# # print(f.read())
# # print(f.readline())
# for x in f:
#     print(x, end =" ")
# f.close()# always close ur files
# f=open("practice.txt", "a")
# f.write("my age is 19")
# f.close()
# f= open("practice.txt", "r")
# for x in f:
# #     print(x, end =" ")
# # f.close()
# f= open("practice.txt", "w")#overwrite
# f.write("ho gya bs")
# f.close()

import os
if os.path.exists("practice.txt"):
    #folder delte through rmdir method 