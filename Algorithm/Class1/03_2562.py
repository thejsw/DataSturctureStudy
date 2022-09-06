num_list = []

for i in range(9):
  i = int(input())
  num_list.append(i)

max_num = max(num_list)

print(max_num)
print(num_list.index(max_num) + 1)