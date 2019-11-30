# hello world
print("hello world") #这是注释

'''
注释2
'''

"""
注释3
"""

if True:
    print("true")
    print("真")
else:
    print("false")
    print("") # 缩进需要一致

print("this " "is " "String " * 2)

print('this ' 'is ' 'String')

print("this " + 'is')

str = '012345'

print(str[0])
print(str[0:-1])
print(str[1:2])

print('222\n33')
print(r'444\n55')


#input("\n\n 请输入: ")

x=1
y=2
print(x);print(y)
print(x,end="");print(y, end="\n")

import  os
i=os.system("cls")