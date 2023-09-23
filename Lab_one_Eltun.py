#Первое задание

GREEN = '\u001b[42m'
RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
BLACK = '\u001b[40m'
END = '\u001b[0m'

print('France')
for i in range(9):
    print(f'{BLUE}{"  "*8}{WHITE}{"  "*8}{RED}{"  "*8}{END}')

#Второе задание

print('Узор')
i=0
while i<15:
    if i%2==0:
        print('  ',f'{BLACK}{"   " * 1}{END}',' '*1,f'{BLACK}{"   " * 1}{END}')
        i+=1
    else:
        print('  ', '  ' * 1, f'{BLACK}{"   " * 1}{END}')
        i+=1

#Третье задание

plot_list = [[0 for i in range(10)] for i in range(10)]
result = [0 for i in range(10)]

for i in range(10):
    result[i] = i ** 2

step = round(abs(result[0] - result[9]) / 9, 2)
print(step)

for i in range(10):
    for j in range(10):
        if j == 0:
            plot_list[i][j] = step * (8-i) + step

for i in range(9):
    for j in range(10):
        if abs(plot_list[i][0] - result[9 - j]) < step:
            for k in range(9):
                if 8 - k == j:
                    plot_list[i][k+1] = 1

for i in range(9):
    line = ''
    for j in range(10):
        if j == 0:
            line += '\t' + str(int(plot_list[i][j])) + '\t'
        if plot_list[i][j] == 0:
            line += '--'
        if plot_list[i][j] == 1:
            line += '!!'
    print(line)
print('\t0\t1 2 3 4 5 6 7 8 9')

for i in range(10):
    #print(plot_list[i])
    pass

#Четвёртое задание

f=open('C://sequence.txt')
a=[float(i) for i in f]
k1 = k2 =0
for i in a:
    if i>0:
        k1+=1
    elif i<0:
        k2+=1

for i in range(max(k1,k2)):
    if i<(max(k1,k2)-min(k1,k2)):
        print(f'{GREEN}{"   " * 1}{END}', '     ',f'{RED}{"   " * 0}{END}')
    else:
        print(f'{GREEN}{"   " * 1}{END}', '     ',f'{RED}{"   " * 1}{END}')
print(k1,'     ',k2,'\nЧисла','   ','Числа','\nбольше    меньше','\nнуля      нуля')