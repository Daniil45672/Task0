a = input("Введіть рядок:")
l = len(a)
mas1 = []
mas2 = []
i = 0

while i < l:
    a_int = ''
    q = a[i]
    while '0' <= q <= '9':
        a_int += q
        i += 1
        if i < l:
            q = a[i]
        else:
            break
    i += 1
    if a_int != '':
        mas1.append(int(a_int))
print("Вивід чисел:",mas1)
for w in '1234567890':
    a=a.replace(w, '')
a.strip(' ')
while a.find('  ') != -1:
    a = a.replace('  ', ' ')
print("Вивід слів:",a)
def cap(a):
     a, result = a.title(), ""
     for word in a.split():
        result += word[:-1] + word[-1].upper() + " "
     return result[:-1]     

print("\nЗамена первой и последней буквы в каждом слове на заглавные:\n", cap(a), sep='')

largest_number = max(mas1)
print("Максимальне число=",largest_number)

for i in range(len(mas1)):
    if mas1[i] != largest_number:
        mas2.append(mas1[i]**i)
print("Массив чисел піднесених до степені:",mas2)
