def print_set(some_set): #some_set переданное множество в функцию, результат а-б, б-а, пересечение
    print(len(some_set)) #len метод возвращающий длину множества, которая представляет из себя общее количество элементов во множестве
    print(*[str(item) for item in sorted(some_set)]) #печать каждого элемента из множества, сортированного по возрастанию
 
N, M = [int(s) for s in input().split()] #количество кубиков у ани и бори
A_colors, B_colors = set(), set() #задание множеств
for i in range(N): #добавление номеров цветов в множество Ани
    A_colors.add(int(input()))
for i in range(M): #добавление номеров цветов в множество Бори
    B_colors.add(int(input()))
     
print_set(A_colors & B_colors) #печать номеров цветов кубиков которые есть в обеих наборах (анперсент - пересечение)
print_set(A_colors - B_colors) #вывод номеров цветов которые есть только у ани (вычитание)
print_set(B_colors - A_colors) #вывод номеров цветов которые есть только у бори (вычитание)
