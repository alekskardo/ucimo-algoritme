def stepenuj(x, n):
  if n == 0: return 1
  return x * stepenuj(x, n-1)

print(stepenuj(2, 8))
