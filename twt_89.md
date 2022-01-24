#TWT Challenge 89

##first try - bruteforce
```py
for I in[I:=input]*int(I()):
 w,h=map(int,I().split())
 M=[I()[::2]for _ in'_'*h]
 N=[*zip(*M)]
 r=0
 for a,c in[(a,c)for a in range(h)for c in range(w)if'0'<M[a][c]]:
  for B in range(h-a):
   for D in range(w-c):
    if'0'not in N[c+D][a:a+B+1]:r=max(~B*~D,r)
    else:break
 print(r)
```
Code is just 
1) Iterating through the inputs
2) mapping the input to a 2D list
3) making a transposed list
4) iterating through the list and try to create rectangles with the upper left corner fixed
5) if the last row does not contain '0' it calculates\* the size and updates r if it's bigger than the previous result
6) prints at the end of the bruteforcing

_*`~B*~D` is really `(-1-B)*(-1-D)` which equals `(B+1)*(D+1)`_

##Second try - histogram (count of 1s to the end)
It just later occurred to me, that what I'm calculating is really just a histogram...
```py
for I in[I:=input]*int(I()):
 r,_=0,range
 w,h=map(int,I().split())
 M=[I()[::2]+'0'for z in'_'*h]
 Q=[[l[i:].find('0')for i in _(w)]for l in M]
 R=[*zip(*Q)]
 for a in _(h):
  for b in _(w):
   if Q[a][b]:
    for c in _(0,h-a):
     if Q[a+c][b]:
      r=max(-~c*min(R[b][a:a-~c]),r)
     else:
      break
 print(r)
```
Same basic stuff:
1) iterate through elements
2) `M` create a 2D list from the input (putting an extra 0 to the end of eachline to help building the next step)
3) `Q` Calculating histogram (how many consecutive '1' from the current position in the row)
4) `R` tranposing `Q`
5) Iterate through all elements in `Q` if the value is not zero
   1) try to add more rows from the cell.
   2) calculate\* the maximum available rectangle (by selecting the checking the available number of consecutive '1's), and selecting the lowest value, whic is the available maximum with without any '0's.
   3) updating the result(`r`) if bigger than before

_*`-~c*min(R[b][a:a-~c])` this works as described, `-~c` is just `(c+1)` and instead of column indexing it just uses row indexing using the transposed table of the histogram_