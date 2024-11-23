import math

N=int(input("No. of pnts Beetle visited: "));
gvnStr=input("Enter the Coordinates as per the format: ");

pntSpl=gvnStr.split(',');
pnts=[] #Expected Format: [[x1,y1,z1],[x2,y2,z2],[x3,y3,z3]]

for i in range(N):
  pnts.append((int(pntSpl[3*i]),int(pntSpl[3*i+1]),int(pntSpl[3*i+2])));

print("Points beetle visited:",pnts);

dist=0;

for i in range(N-1):
  if (pnts[i][2]!=0):
    if (pnts[i][0]==pnts[i+1][0] and pnts[i][1]==pnts[i+1][1]):dist+=round(abs(6.28*(pnts[i+1][2]-pnts[i][2])/6),2);
    elif (pnts[i][1]==pnts[i+1][1] and pnts[i][2]==pnts[i+1][2]):dist+=round(abs(6.28*(pnts[i+1][0]-pnts[i][0])/6),2);
    elif (pnts[i][2]==pnts[i+1][2] and pnts[i][0]==pnts[i+1][0]):dist+=round(abs(6.28*(pnts[i+1][1]-pnts[i][1])/6),2);
    else:
      if (pnts[i][0]==pnts[i+1][0]):dist+=round(abs((pnts[i+1][2]-pnts[i][2])+(pnts[i+1][1]-pnts[i][1])),2);
      elif (pnts[i][1]==pnts[i+1][1]):dist+=round(abs((pnts[i+1][2]-pnts[i][2])+(pnts[i+1][0]-pnts[i][0])),2);
      elif (pnts[i][2]==pnts[i+1][2]):dist+=round(abs((pnts[i+1][1]-pnts[i][1])+(pnts[i+1][0]-pnts[i][0])),2);
      else: # x=0,x=10,y=0,y=10,z=0,z=10
        if (pnts[i][0]==0 or pnts[i][0]==10):
          if (pnts[i+1][1]==0 or pnts[i+1][1]==10):
            dist+=round(((abs(pnts[i+1][1]-pnts[i][1])+abs(pnts[i+1][0]-pnts[i][0]))**2+abs(pnts[i+1][2]-pnts[i][2])**2)**(1/2),2)
          elif (pnts[i+1][2]==0 or pnts[i+1][2]==10):
            dist+=round(((abs(pnts[i+1][2]-pnts[i][2])+abs(pnts[i+1][0]-pnts[i][0]))**2+abs(pnts[i+1][1]-pnts[i][1])**2)**(1/2),2)
        elif (pnts[i][1]==0 or pnts[i][1]==10):
          if (pnts[i+1][0]==0 or pnts[i+1][0]==10):
            dist+=round(((abs(pnts[i+1][1]-pnts[i][1])+abs(pnts[i+1][0]-pnts[i][0]))**2+abs(pnts[i+1][2]-pnts[i][2])**2)**(1/2),2)
          elif (pnts[i+1][2]==0 or pnts[i+1][2]==10):
            dist+=round(((abs(pnts[i+1][1]-pnts[i][1])+abs(pnts[i+1][2]-pnts[i][2]))**2+abs(pnts[i+1][0]-pnts[i][0])**2)**(1/2),2)
        elif (pnts[i][2]==0 or pnts[i][2]==10):
          if (pnts[i+1][1]==0 or pnts[i+1][1]==10):
            dist+=round(((abs(pnts[i+1][1]-pnts[i][1])+abs(pnts[i+1][2]-pnts[i][2]))**2+abs(pnts[i+1][1]-pnts[i][1])**2)**(1/2),2)
          elif (pnts[i+1][0]==0 or pnts[i+1][0]==10):
            dist+=round(((abs(pnts[i+1][2]-pnts[i][2])+abs(pnts[i+1][0]-pnts[i][0]))**2+abs(pnts[i+1][1]-pnts[i][1])**2)**(1/2),2)

print("Distance travelled:",dist);