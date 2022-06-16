import math
import ROOT as r
from ROOT import TCanvas, TFile, TH1F
from ROOT import gROOT, gSystem, Double
from ROOT import TLorentzVector
 
c1 = TCanvas( 'c1', 'Dynamic Filling', 200, 10, 700, 500 )
c1.SetFillColor( 42 )
c1.GetFrame().SetFillColor( 21 )
c1.GetFrame().SetBorderSize( 6 )
c1.GetFrame().SetBorderMode( -1 )

hfile=gROOT.FindObject( 'py-test.root' )
if hfile:
	hfile.Close()
hfile=TFile( 'py-test.root', 'RECREATE', 'InvM ROOT file with histograms' )

InvMH=TH1F( 'InvMH', 'Invariant Mass Histogram', 100, -4, 4 )
#pt, eta, phi, px, py, pz, E, delta-Eta, delta-Phi and dR[6]
Pth=TH1F( 'Momentum-t', 'Momentum-t histograms', 100, -4, 4)
Pxh=TH1F( 'Momentum-x', 'Momentum-x histograms', 100, -4, 4)
Pyh=TH1F( 'Momentum-y', 'Momentum-y histograms', 100, -4, 4)
Pzh=TH1F( 'Momentum-z', 'Momentum-z histograms', 100, -4, 4)
Phih=TH1F( 'Phi', 'Phi histograms', 100, -4, 4)
dPhih=TH1F( 'dPhi', 'dPhi histograms', 100, -4, 4)
Etah=TH1F( 'Eta', 'Eta histograms', 100, -4, 4)
dEtah=TH1F( 'dEta', 'dEta histograms', 100, -4, 4)
dRh=TH1F( 'dR', 'sqrt(delta Eta ^2 + delta Phi ^2)', 100, -4, 4)
Eh=TH1F( 'E', 'E histograms', 100, -4, 4)



h1=[]
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

	def loopfillhist(self, invM):
		h1=h1.append(invM)
		return h1
     

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

	a=0
	n=1
	fo=open("invmlist.txt","w")
	lines=[]

	with open('muons3.txt') as f:
		lines=f.readlines()
	for line in lines[0::2]:
	
		Enp=Particle(f'{line}')
		mphieta1=Enp.mphieta()
		P14=[Enp.E(),Enp.pxhat(),Enp.pyhat(),Enp.pzhat()]
		#pt, eta, phi, px, py, pz, E, delta-Eta, delta-Phi and dR[6] between the 2 muons
		#P14=TLorentzVector(Enp.E(),Enp.pxhat(),Enp.pyhat(),Enp.pzhat())

		Enp=Particle(f'{lines[n]}')
		n=n+2
		mphieta2=Enp.mphieta()
		P24=[Enp.E(),Enp.pxhat(),Enp.pyhat(),Enp.pzhat()]
		#P14=TLorentzVector(Enp.E(),Enp.pxhat(),Enp.pyhat(),Enp.pzhat())
		
		p2p=Muons(P14,P24)
		invM1=p2p.invarmass1()

		invM2=p2p.invarmass2(mphieta1[1],mphieta2[1],mphieta1[2],mphieta2[2])
		invM3=p2p.invarmass3()
		p2pstr=p2p.__str__(invM1,invM2,invM3)
		print(p2pstr)
		a=a+1	
		fo.write("{0}{1}, {2}{3}{4}{5}{6}{7}".format('For trial#', a , 'The invariant mass is ', invM1,' , ', invM2, ' , or ', invM3, '\n'))

		InvMH.Fill(invM1);InvMH.Fill(invM2);InvMH.Fill(invM3)
		Pxh.Fill(P14[1]);Pyh.Fill(P14[2]);Pzh.Fill(P14[3]);Pth.Fill(P14[1]/math.cos(mphieta1[1]))
		Pxh.Fill(P24[1]);Pyh.Fill(P24[2]);Pzh.Fill(P24[3]);Pth.Fill(P24[1]/math.cos(mphieta2[1]))
		Phih.Fill(mphieta1[1]);Etah.Fill(mphieta1[2]);Eh.Fill(P14[0])
		Phih.Fill(mphieta2[1]);Etah.Fill(mphieta2[2]);Eh.Fill(P24[0])
		dPhih.Fill(mphieta1[1]-mphieta2[1]);dEtah.Fill(mphieta1[2]-mphieta2[2]);dRh.Fill(math.sqrt((mphieta1[1]-mphieta2[1])**2+(mphieta1[2]-mphieta2[2])**2))


hfile.Write()