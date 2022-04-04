from decimal import*
import math
import numpy

class Muons:
	count=0
	
	def __init__(self, P1, P2, M):
		self.P1=P1
		self.P2=P2
		self.M=M
		Muons.count +=1
	
	def displayCount(self):
		print("Number of trials %d" % Muons.count)
	
	def displayMuons(self):
		print ("4-momentum for Muon#1: ", str(self.P1), ", 4-momentum for Muon#2: ", str(self.P2), ", With invariant M = ", str(self.M))

a=1

lines=[]
with open('muons.txt') as f:
	lines=f.readlines()
n=2
dlines=lines[n::5]
fo=open("info.txt","w")
for line in dlines:
	#print(f'{line}')
	l1=f'{line}'.split()
	#print(l1)

	Pt1=int(Decimal(l1[2]))
	#print(Pt1)
	e1=int(Decimal(l1[3]))
	phi1=int(Decimal(l1[4]))
	m1=int(Decimal(l1[5]))
	#print(m1)
	#print(f'{lines[n+1]}')

	l2=f'{lines[n+1]}'.split()
	#print(l2)
	n=n+5
	
	
	Pt2=int(Decimal(l2[2]))
	#print(Pt1)
	e2=int(Decimal(l2[3]))
	phi2=int(Decimal(l2[4]))
	m2=int(Decimal(l2[5]))
	#print(m2)
	
	Px1=Pt1*math.cos(phi1)
	Py1=Pt1*math.sin(phi1)
	Pz1=Pt1*math.sinh(e1)
	#print(Pz1)
	E1=math.sqrt(m1**2+Pt1**2*(1+pow(math.sinh(e1),2)))
	#print(E1)
	
	
	Px2=Pt2*math.cos(phi2)
	Py2=Pt2*math.sin(phi2)
	Pz2=Pt2*math.sinh(e2)
	
	E2=math.sqrt(m2**2+Pt2**2*(1+pow(math.sinh(e2),2)))
	
	
	P1p=[Px1,Py1,Pz1]
	P2p=[Px2,Py2,Pz2]
	
	P14=[E1,Px1,Py1,Pz1]
	P24=[E2,Px2,Py2,Pz2]
	
	
	invM=math.sqrt(abs(m1**2+m2**2+2*(E1*E2-numpy.dot(P14,P24))))#(not sure if I can hit it with and abs())
	#print(invM)
	p2p=Muons(P14,P24,invM)
	
	p2p.displayMuons()
	#p2plines=[]
	#p2plines.extend[p2p.displayMuons()]
	#print(P1)
	#print(P2)
	fo.write("For trial#"+str(a)+"The invariant mass is "+str(invM)+"\n%")
	a=a+1	
	
