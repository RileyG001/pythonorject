#!/usr/bin/env python3, this gives an invalid syntax if # is taken off, dont know what this does ask the professor on Monday
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
		print ("{0}{1}, {2}{3}, {4}{5}".format('4-momentum for Muon#1 = ', self.P1, '4-momentum for Muon#2 = ', self.P2, 'With invariant M = ', self.M))#not sure what was meant by nice formatted printouts

class Particle:

	def __init__(self, line):
		l1=line.split()
		self.Pt=float(l1[2])
		self.eta=float(l1[3])
		self.phi=float(l1[4])
		self.m=float(l1[5])
		
	def eandp (self):
		Px=self.Pt*math.cos(self.phi)
		Py=self.Pt*math.sin(self.phi)
		Pz=self.Pt*math.sinh(self.eta)
		E=math.sqrt(self.m**2+self.Pt**2*(1+pow(math.sinh(self.eta),2)))#I want to leave the energy equation like this rather than the Ptcosh(eta) as I don't know how much the mass would effect the end results
		return [E,Px,Py,Pz,self.m]

	def invarmass (self, P14, P24, m1, m2):
		#return math.sqrt(abs(m1**2+m2**2+2*(P14[0]*P24[0]-numpy.dot(P14,P24))))#(not sure if I can hit it with and abs())
        #I think (1 of) the problem(s) with my invariant mass calculation is that the dot product of the 4-momentum is E1(E2) - (P1*P2), 
        # but my previous calculation I just used numpy.dot which would just give me E1*E2+P1*P2, which is why in the incorrect version I would need an abs()
		return math.sqrt(m1**2+m2**2+2*(P14[0]*P24[0]-P14[0]*P24[0]+(numpy.dot(P14.pop(0),P24.pop(0)))))

a=0
n=2
fo=open("invmlist.txt","w")

lines=[]
with open('muons.txt') as f:
	lines=f.readlines()
for line in lines[n::5]:

	Enp=Particle(f'{line}')
	pm=Enp.eandp()
	m1=Enp.eandp()[4]
	P14=Enp.eandp()[:-1]

	Enp=Particle(f'{lines[n+1]}')
	m2=Enp.eandp()[4]
	P24=Enp.eandp()[:-1]

	invM=Enp.invarmass(P14,P24,m1,m2)
	p2p=Muons(P14,P24,invM)
	
	p2p.displayMuons()
	a=a+1	
	fo.write("{0}{1}, {2}{3}{4}".format('For trial#', a , 'The invariant mass is ', invM, '\n%'))