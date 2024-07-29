if(!settings.multipleView) settings.batchView=false;
settings.tex="pdflatex";
settings.inlinetex=true;
deletepreamble();
defaultfilename="main-8";
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
pair a1 = (1,0);
pair a2 = (0.5,1);
int range = 3;
filldraw(
(-0.5*(a1+a2))--(-0.5*a2+0.5*a1)--(0.5*(a1+a2))--(0.5*a2-0.5*a1)--cycle,
blue+opacity(0.1), white+linewidth(0)
);
draw((0,-range)--(0,range),p=red+opacity(0.2));
draw((-range,0)--(range,0),p=red+opacity(0.2));
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
