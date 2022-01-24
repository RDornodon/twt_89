for I in[I:=input]*int(I()):
 r,_=0,range;w,h=map(int,I().split());M=[I()[::2]+'0'for z in'_'*h];Q=[[l[i:].find('0')for i in _(w)]for l in M];R=[*zip(*Q)]
 for a in _(h):
  for b in _(w):
   if Q[a][b]:
    for c in _(0,h-a):
     if Q[a+c][b]:r=max(-~c*min(R[b][a:a-~c]),r)
     else:break
 print(r)