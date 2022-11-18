'''
Задача №3
Вход: размер шахматной доски, от 0 до 20
Выход: вывести на экран эту доску с названиями полей.
Пример:
In: 4
Out:
a4 b4 c4 d4
a3 b3 c3 d3
a2 b2 c2 d2
a1 b1 c1 d1
'''
# а можно же сделать обычным списком?
alphabet ={1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t'}
foo = num = int(input('Enter num: '))
c = 1
count = 0
while count < num:
    print('')
    for var in range(num):
        print(alphabet[c],foo, sep='',end=' ')
        c += 1
    count += 1
    foo -= 1
    c = 1
   
# import string
# ALPHA = string.ascii_lowercase
# # ALPHA 
# # 'abcdefghijklmnopqrstuvwxyz'
# t ={i: ALPHA[i] for i in range(len(ALPHA))}
# print(t)
    
    
    
    