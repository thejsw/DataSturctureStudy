while True:
  num_list = list(map(int, input().split()))
  if sum(num_list) == 0:
    break

  num_list.sort()
  max_num = num_list[2] ** 2
  two_num = num_list[0] ** 2 + num_list[1] ** 2
  
  if (max_num == two_num):
    print("right")
  else:
    print("wrong")
