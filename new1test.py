import math

class Muons:
	count=0
	
	def __init__(self, P1, P2):
		self.P1=P1
		self.P2=P2
		Muons.count +=1
	
	def displayCount(self):
		print("Number of trials %d" % Muons.count)

	def invarmass1 (self):
		return math.sqrt(2*(self.P1[0]*self.P2[0]-self.P1[1]*self.P2[1]-self.P1[2]*self.P2[2]-self.P1[3]*self.P2[3]))
	def invarmass2 (self, phi1, phi2, eta1, eta2):
		Pt1=self.P1[1]/(math.cos(phi1))
		Pt2=self.P2[1]/(math.cos(phi2))
		return math.sqrt(2*Pt1*Pt2*(math.cosh(eta1-eta2)-math.cos(phi1-phi2)))
	def invarmass3 (self):
		return math.sqrt((self.P1[0]+self.P2[0])**2-((self.P1[1]+self.P2[1])**2+(self.P1[2]+self.P2[2])**2+(self.P1[3]+self.P2[3])**2))
		

	def __str__(self,M1,M2,M3):
		rv="{0}{1}, {2}{3}, {4}{5}{6}{7}{8}{9}".format('4-momentum for Muon#1 = ', self.P1, '4-momentum for Muon#2 = ', self.P2, 'With invariant M1 = ', M1, ', compared to M2 = ', M2, ', compared to M3 = ', M3)
		return rv

    
      

class Particle:

	def __init__(self, line):
		l1=line.split()
		self.Pt=float(l1[2])
		self.eta=float(l1[3])
		self.phi=float(l1[4])
		self.m=float(l1[5])
		#pxhat=self.Pt*math.cos(self.phi)
		#pyhat=self.Pt*math.sin(self.phi)
		#pzhat=self.Pt*math.sinh(self.eta)
		#En=self.Pt*math.cosh(self.eta)

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
	def magofp (Px,Py,Pz):
		magP=math.sqrt(pow(Px,2)+pow(Py,2)+pow(Pz,2))
		return magP

fo=open("muons3.txt","w")
lines=[]
with open('muons2.txt') as f:
	lines=f.readlines()
for line in lines:
	if ':' in line:
		fo.write(line)

if __name__=="__main__":

	a=0 #main part of the code use def __main__():
	n=1
	fo=open("invmlist.txt","w")
	lines=[]

	with open('muons3.txt') as f:
		lines=f.readlines()
	for line in lines[0::2]:
	
		Enp=Particle(f'{line}')
		mphieta1=Enp.mphieta()
		P14=[Enp.E(),Enp.pxhat(),Enp.pyhat(),Enp.pzhat()]

		Enp=Particle(f'{lines[n]}')
		n=n+2
		mphieta2=Enp.mphieta()
		P24=[Enp.E(),Enp.pxhat(),Enp.pyhat(),Enp.pzhat()]

		p2p=Muons(P14,P24)#,invM)
		invM1=p2p.invarmass1()
		invM2=p2p.invarmass2(mphieta1[1],mphieta2[1],mphieta1[2],mphieta2[2])
		invM3=p2p.invarmass3()
		p2pstr=p2p.__str__(invM1,invM2,invM3)
		print(p2pstr)
		a=a+1	
		fo.write("{0}{1}, {2}{3}{4}{5}{6}{7}".format('For trial#', a , 'The invariant mass is ', invM1,' , ', invM2, ' , or ', invM3, '\n'))