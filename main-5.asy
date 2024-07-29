if(!settings.multipleView) settings.batchView=false;
settings.tex="pdflatex";
settings.inlinetex=true;
deletepreamble();
defaultfilename="main-5";
if(settings.render < 0) settings.render=4;
settings.outformat="";
settings.inlineimage=true;
settings.embed=true;
settings.toolbar=false;
viewportmargin=(2,2);

import graph;
defaultpen(fontsize(10pt));
size(4.5cm,0);
srand(42);
pen bdy = gray+opacity(0.4);
pen flu = deepcyan+opacity(0.4);
pen prt = heavyred+opacity(0.4);
real rand_spread = 0.1;

void boundary(pair coords) {filldraw(circle(coords,0.5),bdy,bdy+linewidth(1));}
void fluid(pair coords) {filldraw(circle(coords,0.5),flu,flu+linewidth(1));}
void particle(pair coords) {filldraw(circle(coords,0.5),prt,prt+linewidth(1));}

pair prt_rdm = (0.0,0.0);
for (int y=2; y>=-2; y-=1){
for (int x=-2; x<=2; x+=1){
if (y<=-2){
filldraw(circle((x,y),0.5),black+opacity(0),black+opacity(0)+linewidth(1));
continue;
}
pair rdm = (unitrand()-0.5, unitrand()-0.5)*rand_spread;
if(y<0){boundary((x,y));}
else{
if(x==0&&y==0){
prt_rdm = rdm;
particle((x,y)+rdm);
} else{
fluid((x,y)+rdm);
}
}
}
}
draw(circle(prt_rdm,2),prt+linewidth(1));
dot(prt_rdm,black+linewidth(3));
// draw line with particle radius
draw(prt_rdm..prt_rdm+(2,0),black+linewidth(1));
label("$\hbar$",prt_rdm+(1,0), align=N, p=black);
