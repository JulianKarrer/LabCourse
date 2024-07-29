if(!settings.multipleView) settings.batchView=false;
settings.tex="pdflatex";
settings.inlinetex=true;
deletepreamble();
defaultfilename="main-9";
if(settings.render < 0) settings.render=4;
settings.outformat="";
settings.inlineimage=true;
settings.embed=true;
settings.toolbar=false;
viewportmargin=(2,2);

import graph;
defaultpen(fontsize(8pt));
unitsize(0.7cm);
arrowbar axisarrow = Arrow(TeXHead);

real a = sqrt(2/(3*sqrt(3)));
pair a1 = (1.5*a,a);
pair a2 = (0,sqrt(3)*a);
int range = 3;
int n=6;
pair[] V= sequence(new pair(int i){return dir(360*i/n);}, n);
filldraw(
a*V[0]--a*V[1]--a*V[2]--a*V[3]--a*V[4]--a*V[5]--cycle,
blue+opacity(0.1), white+linewidth(0)
);
draw(-3*a1--3*a1,p=red+opacity(0.2));
draw(-3*a2--3*a2,p=red+opacity(0.2));
draw(-sqrt(3)*(a1+a2)--sqrt(3)*(a1+a2),p=red+opacity(0.2));
draw(-1.9*(-a1+2*a2)--1.9*(-a1+2*a2),p=red+opacity(0.2));
draw(-3*(a1-a2)--3*(a1-a2),p=red+opacity(0.2));
draw(-1.6*(2*a1-a2)--1.6*(2*a1-a2),p=red+opacity(0.2));
for (int i=2*range; i>=-2*range; i-=1){
for (int j=-2*range; j<=2*range; j+=1){
pair p = j*a1+i*a2;
if(-range<=p.x && p.x<=range && -range<= p.y && p.y <= range){
dot(j*a1+i*a2);
}
}
}
draw((0,0)--a1,arrow=axisarrow);
label("$\vek{a}_1$",0.5*a1,align=SE);
draw((0,0)--a2,arrow=axisarrow);
label("$\vek{a}_2$",0.5*a2,align=NW);
