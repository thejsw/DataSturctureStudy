### 1번 풀이
# case_num = int(input())
# num_list = list(map(int, input().split()))
# print(min(num_list), max(num_list))


### 2번 풀이
case_num = int(input())
num_list = list(map(int, input().split()))
max = num_list[0]
min = num_list[0]

for i in num_list[1:]:
	if i > max:
		max = i
	elif i < min:
		min = i

print(min,max)