# import random
# import sys

# print(random.randint(20,23))

# print("hell",end="")
# sys.exit()
# print('a')
# import pyperclip
#
# pyperclip.copy('ouhello')

# print('cat','dog','camel',sep='abc')
# print('cat','dog','camel')

#Assignment Tricks
# cat = ['fat','orange','loud']
#
# size, color, disposition = cat
#
# print(size,color,disposition)
cat = ['fat','hi']
#
# cat[1] = [1,'hello']
#
# print(cat)

cat = ['a','z','e','f']

print(cat.index('a'))
cat.append('c')
print(cat)
cat.insert(1,'k')
print(cat)
cat.remove('a')
print(cat)
cat.append('A')
cat.sort()
print(cat)
cat.sort(reverse=True)
print(cat)
cat.append('a')
cat.append('C')
cat.sort(key=str.lower)
print(cat)
