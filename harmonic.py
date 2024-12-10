import numpy as np
import matplotlib.pyplot as pp

def ode(c,v,y):
    k = 3
    m = 2
    return (-1*c*v)-((k/m)**y)

def euler(h,c,v,y):
    yp = ode(c,v,y)
    return yp*h

t = []
y1 = []
y2 = []
y3 = []
y4 = []
y0 = 2
v0 = 0
h = 0.05
yn = 2
vn = 0

f = 0

for i in range(20):
    t.append(i)

for i in range(20):
    f = yn + euler(h,0,vn,yn)
    y1.append(f)
    yn = f
    vn += vn*h

yn = 2

for i in range(20):
    f = yn + euler(h,6,vn,yn)
    y2.append(f)
    yn = f
    vn += vn*h

yn = 2

for i in range(20):
    f = yn + euler(h,3,vn,yn)
    y3.append(f)
    yn = f
    vn += vn*h

yn = 2

for i in range(20):
    f = yn + euler(h,9,vn,yn)
    y4.append(f)
    yn = f
    vn += vn*h

figure = pp.figure(figsize=(7,5),layout = 'constrained')
spec = figure.add_gridspec(ncols=2, nrows=2)

undamped = figure.add_subplot(spec[0,0])
undamped.plot(t,y1,'r-')

perfect_damped = figure.add_subplot(spec[0,1])
perfect_damped.plot(t,y2,'r-')

underdamped = figure.add_subplot(spec[1,0])
underdamped.plot(t,y3,'r-')

overdamped = figure.add_subplot(spec[1,1])
overdamped.plot(t,y4,'r-')

pp.show()
