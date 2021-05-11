print('Alma', 'Armud', 'Banan', sep=' hahahah ')
'''
This code for something
nljhjl
kjlkhl
jlj
'''

x = 5
y = str(x)
z = x + y

x = "Mentiqi tefekkuru yoxlayan testler"
y = x.replace('testler', 'suallar')
print(y)

x = 'yagis yagir'
while x:
    print('hava soyuqdu')
while True:
    print('hava soyuqdu')

text = 'Python Programming'
i = 1
while i < len(text):
    print(f'{i}:{text}')
    i = i + 1

text = 'Python Programming'
i = 1
while i < len(text):
    print(f'{i}:{text}')
    if i == 10:
        break
    i = i + 1

text = 'Python Programming'
i = 1
while i < len(text):
    i = i + 1
    if i == 10:
        continue
    print(f'{i}:{text}')
    
#FOR DONGUSU

text = 'Python'
for i in text:
    print(i)

text = 'Python'
j = 0
for i in text:
    j += 1
    print(f'{j}:{i}')

for i in range(10):
    print(i)

for i in range(10,50):
    print(i) 

text = 'Python'
for i in range(len(text)):
    print(i)

for i in range(10,50, 5): ## start, stop, step
    print(i)

for i in range(1,51):
    if i % 2 == 0:
        print(f'Cut eded {i}')
    else:
        print(f'Tek eded {i}')

for i in range(4):
    for j in range(6):
        print(f'i:{i} => j:{j}')