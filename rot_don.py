import math
import numpy as np
import curses
alpha_values=np.linspace(0,2*math.pi,45)
beta_values=np.linspace(0,2*math.pi,200)
aux1=np.linspace(0,math.pi/4,50)
aux1rev=aux1[::-1]
xtheta_value=[*aux1,*aux1rev]
ytheta_value=np.linspace(0,math.pi,100)
ztheta_value=0
Rinx=8
Riny=4
Rinz=4
Rtx=20
Rty=9


zbuffer=np.full((40,60),-100)
shadsign=['.',',','-','~',':',';','=','!','*','#','$','@']


e=math.cos(ztheta_value)
e1=math.sin(ztheta_value)
curses.initscr()
win=curses.newwin(60,60,0,0)
curses.curs_set(False)
for k in range(100):
    win.clear()
    c=math.cos(xtheta_value[k])
    c1=math.sin(xtheta_value[k])
    d=math.cos(ytheta_value[k])
    d1=math.sin(ytheta_value[k])
    for i in range(200):
        b=math.cos(beta_values[i])
        b1=math.sin(beta_values[i])
        for j in range(45):
            a=math.cos(alpha_values[j])
            a1=math.sin(alpha_values[j])
            dx=round((Rtx+Rinx*a)*b*d*e+(Rty+Riny*a)*b1*(-c*e1+e*d1*c1)+Rinz*a1*(e*c*d1+e1*c1))+29
            dy=round((Rtx+Rinx*a)*b*d*e1+Rinz*a1*(d*e1*d1-e*c1)+(Rty+Riny*a)*b1*(e*c+e1*d1*c1))+13
            dz=round(-(Rtx+Rinx*a)*b*d1+e*(Rinz*c*a1+(Rty+Riny*a)*b1*c1))
            shadcomp=abs(round(11*(-a*b*d1+d*(c*a1+a*b1*c1))))
            if dz > zbuffer[dy,dx]:
                zbuffer[dy,dx]=dz
                win.addstr(dy,dx,shadsign[shadcomp])
            else:
                pass
    win.refresh()
    zbuffer=np.full((40,60),-100)
    win.move(0,0)
curses.endwin()
