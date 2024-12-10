init=input()
numList=init.split()
N=int(numList[0])
M=int(numList[1])

connData={}

for i in range(N):
  connData.update({i:[]})

for i in range(M):
  print()
  frndd=input()
  frnds=frndd.split()
  connData[int(frnds[0])].append(int(frnds[1]))
  connData[int(frnds[1])].append(int(frnds[0]))

print()
K=int(input())
R=N
days=1

for i in range(N):connData[i].sort()

attendance={}

for i in range(N):attendance.update({i:1})

print()

while R<K:
  for i in range(N):
    prsntFr=0
    nxtAttnd={}
  for i in range(N):
    for ele in connData[i]:
      if attendance[ele]==1:
        prsntFr=prsntFr+1
  for i in range(N):
    if attendance[i]==1:
      if prsntFr==3:
        nxtAttnd.update({i:1})
      else:
        nxtAttnd.update({i:0})
    else:
      if prsntFr<3:
        nxtAttnd.update({i:1})
      else:
        nxtAttnd.update({i:0})
  for i in range(N):
    if nxtAttnd[i]==1:
      R=R+1
  days=days+1
  attendance=nxtAttnd

print(days)