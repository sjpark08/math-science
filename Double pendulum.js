float l1 = 200;
float l2 = 200;
float m1 = 40;
float m2 = 40;
float a1 = PI/2;
float a2 = PI/8;



float a1v = 0;
float a2v = 0;



float g = 1;

float px2 = -1;
float py2 = -1;
float cx, cy;

PGraphics canvas;

void setup() {
  size(900,900);
  cx = width/2;
  cy = 300;
  canvas = createGraphics(900,900);
  canvas.beginDraw();
  canvas.background(255);
  canvas.endDraw();
  
}

void draw() {
  
  float a1a = ( -g * (2 * m1 + m2) * sin(a1) -m2 * g * sin(a1-2*a2) -2 *sin(a1-a2)*m2 * (a2v*a2v*l2 + a1v*a1v*l1 * cos(a1-a2)))/(l1 * (2*m1+m2-m2*cos(2*a1-2*a2)));
  float a2a = (2*sin(a1-a2)*(a1v*a1v*l1*(m1+m2)+g*(m1+m2)*cos(a1)+a2v*a2v*l2*m2*cos(a1-a2)))/(l2*(2*m1+m2-m2*cos(2*a1-2*a2)));
  
  
  image(canvas,0,0);
  stroke(0);
  strokeWeight(4);
  translate(cx,cy);
  
  float x1 = l1*sin(a1);
  float y1 = l1*cos(a1);
  
  float x2 = x1 + l2*sin(a2);
  float y2 = y1 + l2*cos(a2);
  
  
  line(0,0,x1,y1);
  fill(0);
  ellipse(x1,y1,m1,m1);
  
  line(x1,y1,x2,y2);
  fill(0);
  ellipse(x2,y2,m2,m2);
  
  


  a1v += a1a;
  a2v += a2a;
  
  
  a1 += a1v;
  a2 += a2v;
  
  
  
 
  

  
  canvas.beginDraw();
  canvas.translate(cx,cy);
  canvas.strokeWeight(1);
  canvas.stroke(0);
  
  if (frameCount > 1) {
    canvas.line(px2, py2, x2, y2);
  }
  
  canvas.line(px2, py2, x2, y2);
  canvas.endDraw();
  
  px2 = x2;
  py2 = y2;
  
}
