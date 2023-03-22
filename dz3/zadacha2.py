n = (int(input("Введите количество элементов: ")))
a = [int(i) for i in input("Введите через пробел элементы списка: ").split()]
X = int(input("Введите число X, с которым необходимо сравнивать элементы списка: "))
find_num = 0
for i in range(len(a)):
    if a[i] < n:
        find_num = -find_num
    else:
        find_num = find_num + 0
    if a[i] >= n and a[i] - n <= find_num - n:
        find_num = a[i]
    elif a[i] <= n and find_num - n <= a[i] - n:
        find_num = a[i]
print(find_num)