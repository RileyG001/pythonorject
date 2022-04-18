fo=open("muons3.txt","w")
lines=[]
with open('muons2.txt') as f:
	lines=f.readlines()
for line in lines:
	if ':' in line:
		fo.write(line)
#at this point I could delete muons2.txt and only have muons3.txt