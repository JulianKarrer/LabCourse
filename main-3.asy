if(!settings.multipleView) settings.batchView=false;
settings.tex="pdflatex";
settings.inlinetex=true;
deletepreamble();
defaultfilename="main-3";
if(settings.render < 0) settings.render=4;
settings.outformat="";
settings.inlineimage=true;
settings.embed=true;
settings.toolbar=false;
viewportmargin=(2,2);

import graph;
size(400,150,IgnoreAspect);
real h=1.0;
real pi=3.1415926535;
real alpha = 1.0/(6.0*h);

real w(real d) {
real q = abs(d);
if(0.0<=q && q<1.0){
return alpha*((2.0-q)*(2.0-q)*(2.0-q) -4.0*(1.0-q)*(1.0-q)*(1.0-q));
}
if(1.0<=q && q<2.0){
return alpha*((2.0-q)*(2.0-q)*(2.0-q));
}
return 0.0;
}

real dw(real d) {
real q = abs(d);
if(0.0<=q && q<1.0){
return sgn(d)*alpha/h*(-3.0*(2.0-q)*(2.0-q) +12.0*(1.0-q)*(1.0-q));
}
if(1.0<=q && q<2.0){
return sgn(d)*alpha/h*(-3.0*(2.0-q)*(2.0-q));
}
return 0.0;
}

// real gauss(real d){
// real sig = 1.0;
// return 0.5*(1.0/sig*sqrt(2.0*pi)) * exp(-0.5*d*d/(sig*sig));
// }
// draw(graph(gauss,-2,2),green,"$\frac{1}{\sqrt{2\pi}}e^{-\frac{x^2}{2}}$");

draw(graph(w,-2,2),heavyred,"$W(\vek{x},\hbar)$");
draw(graph(dw,-2,2),heavyblue,"$||{\nabla W(\vek{x}, \hbar)}||$");

xaxis("$\frac{\dist{\vek{x}}}{h}$",Bottom,RightTicks);
yaxis("",Left,LeftTicks(trailingzero));


add(legend(),point(E),2E,UnFill);
