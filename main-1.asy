if(!settings.multipleView) settings.batchView=false;
settings.tex="pdflatex";
settings.inlinetex=true;
deletepreamble();
defaultfilename="main-1";
if(settings.render < 0) settings.render=4;
settings.outformat="";
settings.inlineimage=true;
settings.embed=true;
settings.toolbar=false;
viewportmargin=(2,2);

import graph;
defaultpen(fontsize(8pt));
size(7cm,0);
real xmin = -3;
real xmax = 3;
real ymin = 0;
real ymax = 3;

real b(real x) {return x < -0.7?0:(x>0.7?0:ymax);}
real f(real x) {
real t = 0.3;
real sum = 0;
int n = 100;
real dx = 2.0 / n;
for (int i = 0; i <= n; ++i) {
real xi = -1 + i * dx;
sum += exp(-((x - xi) * (x - xi)) / (4 * t)) * b(xi);
}
return sum / (sqrt(4 * 3.141592653589793 * t)) * dx;
}

draw((0, b(0)) .. (0, f(0)), black, arrow=Arrows(TeXHead));
label("local",(0,(b(0)-f(0))/2.+ f(0)), E);

draw(graph(new real(real x) { return b(x); },xmin,xmax, n=1000), heavyblue);
draw(graph(new real(real x) { return f(x); },xmin,xmax, n=1000), lightblue+dashed);
label("$A(\vek{x},t)$",(-0.69, b(-0.69)),NW, heavyblue);
label("$A(\vek{x},t+\Delta t)$",(2.0, f(2.0)),NE, lightblue);

// draw axis
arrowbar axisarrow = Arrow(TeXHead);
draw((xmin,0) -- (xmax,0), arrow=axisarrow);
label("$x$",(xmax,0),S);
draw((xmin+0.5,ymin) -- (xmin+0.5,ymax+0.5), arrow = axisarrow);
label("$A$",(xmin+0.5,ymax+0.5),E);

draw((0,ymin) -- (0,ymax+0.5), black+dotted);
dot("$\vek{x}_i$",(0,ymin),S);
