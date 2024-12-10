import numpy as np
import matplotlib.pyplot as pp

def angle(grade):
	return np.atan(grade)

def drag(v,cd,den,a):
	return ((-1*0.00002*a*(v/2))+(-0.5*cd*den*a*v*v))

def ode(p,m,v,cd,den,a):
	return(p/(m*v))
	
def euler(vn,ts,p,m,cd,den,a):
	return vn + (ts*ode(p,m,vn,cd,den,a))

f = 0
ph = 0
cd = 0.9
den = 1.29
a = 0.33
vi = 4
vn = vi
v = [4]
m = 70
p = 400
ts = 0.1
ti = 0
tf = 200
t = [0]
iterator = ti + ts
len = int(tf/ts)

while iterator < tf:
	t.append(iterator)
	iterator += ts
	
iterator = ti + ts

for l in range (len): 
	v.append(euler(vn,ts,p,m,cd,den,a))
	vn = euler(vn,ts,p,m,cd,den,a)

pp.ylabel('Velocity (m/s)')
pp.xlabel('Time (s)')
pp.plot(t,v,'r-')
pp.show()
	







	