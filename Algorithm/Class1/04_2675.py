case_num = int(input())

for i in range(case_num):
  cnt, string = input().split()
  for j in string:
    print(j * int(cnt), end='')
  print()