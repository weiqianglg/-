from math import log, sqrt
S1=5
S2=3
N=500
def Guass(x):
	return 0.5*log(1+x,2)
for x1 in range(N+1):
	x1=x1/float(N)
	c1=Guass(x1*S1)
	r=[]

	for x2 in range(N+1):
		x2=x2/float(N)
		c2=Guass(x2*S2)
		c12=Guass(S1+S2+2*sqrt(S1*S2*(1-x1)*(1-x2)))
		if c1+c2<c12:
			continue
		else:
			#print c12-c2,c2#A
			#print c1,c12-c1#B
			r.append(c12-c1)
	if len(r)>0:
		print c1, max(r)