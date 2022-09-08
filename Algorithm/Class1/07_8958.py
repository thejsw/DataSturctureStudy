case_num = int(input())

for i in range(case_num):
  OX_str = input()
  OX_score = 0
  Sum_score = 0
  for j in OX_str:
    if (j == 'O'):
      OX_score += 1
      Sum_score += OX_score
    else:
      OX_score = 0
  print(Sum_score)
  
