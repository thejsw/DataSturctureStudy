def move(n, src, tmp, dest):
  if n == 1:
    print("move %d from %c to %c" %(n, src, dest))

  else:
      move(n-1, src, dest, tmp)
      print("move %d from %c to %c" %(n, src, dest))
      move(n-1, tmp, src, dest)

print(move(3, 'A', 'B', 'C'))