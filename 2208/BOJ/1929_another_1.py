a, b = map(int,input().split())
def odd(a,b):
  list_x = [1] * (b+1)
  for i in range(2,int((b+1)**0.5)+1):
    if list_x[i] == 1:
      for x in range(i*2,b+1,i):
        list_x[x] = 0

  for y in range(a,b+1):
    if y>1 and list_x[y]==1:
      print(y)

odd(a,b)