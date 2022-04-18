import math
import numpy

class Muons: #see cleantest for the debugs I did on the code
	count=0
	
	def __init__(self, P1, P2, M):
		self.P1=P1
		self.P2=P2
		self.M=M
		Muons.count +=1
	
	def displayCount(self):
		print("Number of trials %d" % Muons.count)

	def __str__(self):
		rv="{0}{1}, {2}{3}, {4}{5}".format('4-momentum for Muon#1 = ', self.P1, '4-momentum for Muon#2 = ', self.P2, 'With invariant M = ', self.M)
		return rv

class Particle:

	def __init__(self, line):
		l1=line.split()
		self.Pt=float(l1[2])
		self.eta=float(l1[3])
		self.phi=float(l1[4])
		self.m=float(l1[5])
		
	def pxhat(self):
		return self.Pt*math.cos(self.phi)
	def pyhat(self):
		return self.Pt*math.sin(self.phi)
	def pzhat(self):
		return self.Pt*math.sinh(self.eta)
	def E(self):
		return self.Pt*math.cosh(self.eta)
	def mphieta(self):
		return [self.m,self.phi,self.eta]
	def magofp (Px,Py,Pz):#assuming the ||p|| is the magnitude of the 3 vector of momentum and not 4
		magP=math.sqrt(pow(Px,2)+pow(Py,2)+pow(Pz,2))
		return magP

	def invarmass (self, P14, P24, m1, m2):
		P1=P14[0]
		P13=P14[1:3]
		P2=P24[0]
		P23=P24[1:3]
		return math.sqrt(m1**2+m2**2+2*(P1*P2-(numpy.dot(P13,P23))))#by hand calc is off by +/- 10, most likely due to my rounding, so I think it is fairly accurate

a=0
n=1
fo=open("invmlist.txt","w")
#I typed up a quick code see untitled-test2.py, where I took the muon list as got rid of everything but m1 and m2 lines
lines=[]

with open('muons3.txt') as f:
	lines=f.readlines()
for line in lines[0::2]:
	
	Enp=Particle(f'{line}')
	Px1=Enp.pxhat()
	Py1=Enp.pyhat()
	Pz1=Enp.pzhat()
	E1=Enp.E()
	mphieta1=Enp.mphieta()
	m1=mphieta1[0]
	P14=[E1,Px1,Py1,Pz1]

	Enp=Particle(f'{lines[n]}')
	n=n+2
	Px2=Enp.pxhat()
	Py2=Enp.pyhat()
	Pz2=Enp.pzhat()
	E2=Enp.E()
	mphieta2=Enp.mphieta()
	m2=mphieta2[0]
	P24=[E2,Px2,Py2,Pz2]

	invM=Enp.invarmass(P14,P24,m1,m2)
	p2p=Muons(P14,P24,invM)
	p2pstr=p2p.__str__()
	print(p2pstr)
	a=a+1	
	fo.write("{0}{1}, {2}{3}{4}".format('For trial#', a , 'The invariant mass is ', invM, '\n'))