#!/usr/bin/env python3, this gives an invalid syntax if # is taken off, dont know what this does ask the professor on Monday
import math
import numpy
#import os

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
		print ("{0}{1}, {2}{3}, {4}{5}".format('4-momentum for Muon#1 = ', self.P1, '4-momentum for Muon#2 = ', self.P2, 'With invariant M = ', self.M))#not sure what was meant by nice formatted printouts

	def __str__(self):
		rv = "Muon#1: 4-momentum is " + print(P1) + "\n"
		rv += "Muon#2: 4-momentum is " + print(P2) + "\n"
		rv += "Invarient Mass is=" + M
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

	def eandp (self):
		Px=self.Pt*math.cos(self.phi)
		Py=self.Pt*math.sin(self.phi)
		Pz=self.Pt*math.sinh(self.eta)
		#E1=math.sqrt(self.m**2+self.Pt**2*(1+pow(math.sinh(self.eta),2)))#I want to leave the energy equation like this rather than the Ptcosh(eta) as I don't know how much the mass would effect the end results
		E2=self.Pt*math.cosh(self.eta)#very slight change not enough to have a significant impact
		#print(E1)
		#print("{0}{1}{2}".format(E1,', compared to ' , E2))
		return [E2,Px,Py,Pz,self.m,self.Pt, self.phi,self.eta]

	def magofp (Px,Py,Pz):#assuming the ||p|| is the magnitude of the 3 vector of momentum
		magP=math.sqrt(pow(Px,2)+pow(Py,2)+pow(Pz,2))
		return magP


	#def testinvm (self, P14, P24, Pt1, Pt2, m1, m2, phi1, phi2, eta1, eta2):
		P1=P14[0]
		P13=P14[1:3]
		P2=P24[0]
		P23=P24[1:3]
		#Hopefully, the issue is fixed
		#print(math.sqrt(2*Pt1*Pt2*(math.cosh(eta1-eta2)-math.cos(phi1-phi2))))
		#print ("{0} {1} {2}".format(math.sqrt(m1**2+m2**2+2*(P1*P2-(numpy.dot(P13,P23)))), 'compared to', math.sqrt(2*Pt1*Pt2*(math.cosh(eta1-eta2)-math.cos(phi1-phi2)))))
		return math.sqrt(m1**2+m2**2+2*(P1*P2-(numpy.dot(P13,P23))))
	def invarmass (self, P14, P24, m1, m2):
	#def invarmass(self, Pt1, Pt2, eta1, eta2, phi1, phi2)
		P1=P14[0]
		P13=P14[1:3]
		P2=P24[0]
		P23=P24[1:3]
		#return math.sqrt(2*Pt1*Pt2*(math.cosh(eta1-eta2)-math.cos(phi1-phi2)))
		return math.sqrt(m1**2+m2**2+2*(P1*P2-(numpy.dot(P13,P23))))#by hand calc is off by +/- 10, most likely due to my rounding, so I think it is fairly accurate

a=0
n=1
fo=open("invmlist.txt","w")
#f1=open("muons3.txt","w")
#lines=[]
#with open('muons2.txt') as f:					realized it would be better to do this in another code so I don't have to keep deleting muons 3
#to keep testing the code
#	lines=f.readlines()
#for line in lines:
#	if ':' in line:
#		f1.write(line)
#at this point I could delete muons2.txt and only have muons3.txt
#os.replace('muons3.txt', 'muons2.txt')
lines=[]

with open('muons3.txt') as f:
	lines=f.readlines()
for line in lines[0::2]:
	
	Enp=Particle(f'{line}')
	Pt1=Enp.eandp()[5]
	m1=Enp.eandp()[4]
	P14=Enp.eandp()[:-4]
	#phi1=Enp.eandp()[6]
	#eta1=Enp.eandp()[7]

	Enp=Particle(f'{lines[n]}')
	n=n+2
	Pt2=Enp.eandp()[5]
	m2=Enp.eandp()[4]
	P24=Enp.eandp()[:-4]
	#phi2=Enp.eandp()[6]
	#eta2=Enp.eandp()[7]
#	invM=Enp.testinvm(P14,P24,Pt1,Pt2,m1,m2,phi1,phi2,eta1,eta2)
	invM=Enp.invarmass(P14,P24,m1,m2)
	#invM=Enp.invarmass(Pt1,Pt2,eta1,eta2,phi1,phi2)
	p2p=Muons(P14,P24,invM)
	p2p.displayMuons()
	a=a+1	
	fo.write("{0}{1}, {2}{3}{4}".format('For trial#', a , 'The invariant mass is ', invM, '\n'))