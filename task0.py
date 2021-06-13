import random
mas=[]
mas2=[]
num=0
a=0
for i in range(30):
    mas.append(random.randint(-100,100))
print(mas)
for i in range(30):
    if mas[i]==max(mas):
        num=i
print("Максимальний елемент:", max(mas))
print("Індекс максимального элемента:", num)
for i in range(30):
    if (mas[i]%2)!=0:
        mas2.append(mas[i])
        a=1
if a==0:
    print("Немає непарних чисел")
print("Список непарних чисел із начального списку:\n",sorted(mas2,reverse=True))
