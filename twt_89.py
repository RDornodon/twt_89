for I in[I:=input]*int(I()):
 w,h=map(int,I().split());M=[I()[::2]for _ in'_'*h];N=[*zip(*M)];r=0
 for a,c in[(a,c)for a in range(h)for c in range(w)if'0'<M[a][c]]:
  for B in range(h-a):
   for D in range(w-c):
    if'0'not in N[c+D][a:a+B+1]:r=max(~B*~D,r)
    else:break
 print(r)
