# 1
fruits = ['banana','orange','apple','peach','lemon']

# 2
for fruit in fruits:
	if fruit = 'apple':
		print('I found it!')

# 3
fruits.append('pear')
fruits.append('kiwi')

# 4
for fruit in fruits:
	print(fruit,'has',len(fruit),'letters')

# 5
def half_squared(list):
    newlist = []
    for num in list:
        num = num ** 2 / 2
        newlist.append(num)
    return newlist

# 6
score1 = int(input('input first student\'s score:'))
score2 = int(input('input second student\'s score:'))
score = [score1,score2]
for s in score:
    if s < 0 or s > 100:
        print('The score should be greater or equal than 0 and less or equal than 100!')
    elif s <= 60:
        print('C')
    elif s < 90:
        print('B')
    else:
        print('A')

# 7
def revSort(a: int, b: int, c: int):
    if a < b:
        t = a
        a = b
        b = t
    if a < c:
        t = a
        a = c
        c = t
    if b < c:
        t = b
        b = c
        c = t
    return a,b,c

# 8
list1 = [1,2,3]
list2 = [4,5,6]
array = [list1,list2]
for list in array:
    for num in list:
        print(num,end=" ")

# 9
a = range(1,101)
b = []
def f(x):
    return x ** 3
for i in map(f,a):
    b.append(sum(map(int,str(i))))
index = 0
while index < 100:
    if a[index] == b[index]:
        print(a[index])
    index += 1

# 10
import random
x = random.randint(1,10)
y = random.randint(1,10)
print(x,y)
t = x
x = y
y = t
print(x,y)

# 11
s = '*'
rows = 7
for i in range(1, rows + 1, 2):
    print((s * i).center(rows))
for i in reversed(range(1, rows - 1, 2)):
    print((s * i).center(rows))

# 12
for i in range(1,7):
    for j in range(i,i+6):
        if j > 6:
            j = j - 6;
        print(j,end = '')
    print()

# 13
players=['charles','martina','michael','florence','eli']
for player in players:
    print(player.title(),end=' ')