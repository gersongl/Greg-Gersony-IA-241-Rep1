#lab7
#3.1
i = 0
while i <= 5:
    if i != 3:
        print(i)
    i = i + 1
#3.2
a = 1
result_1 = 1
while a <= 5:
    result_1 = result_1 * a
    a = a + 1
print(result_1)
#3.3
b = 1
result_2 = 0
while b <= 5:
    result_2 = result_2 + b
    b = b + 1
print(result_2)
#3.4
c = 3
result_3 = 1
while c <= 8:
    result_3 = result_3 * c
    c = c + 1
print(result_3)
#3.5
d = 4
result_4 = 1
while d <= 8:
    result_4 = result_4 * d
    d = d + 1
print(result_4)
#3.6
num_list = [12,32,43,35]
while num_list:
    num_list.remove(num_list[0])
print(num_list)
#done