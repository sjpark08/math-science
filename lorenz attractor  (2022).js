

float x = 0.01;
float y = 0;
float z = 0;

float a = 10;
float p = 28;
float b = 8.0/3.0;

ArrayList<PVector> points = new ArrayList<PVector>();





void setup() {
  
  size(800, 600, P3D);
  
  
}

void draw() {
  
  background(0);
  
  float dt = 0.01;
  
  float dx = (a * (y - x)) * dt;
  float dy = (x * (p - z) - y) * dt;
  float dz = (x * y - b * z) * dt;
  
  x = x + dx;
  y = y + dy;
  z = z + dz;
  
  println(x, y, z);
  
  points.add(new PVector(x, y, z));
  
  translate(width/2, height/2); 
  scale(5); 
  stroke(255); 
  noFill();
  
  float hu = 0;
  beginShape();
  for (PVector v : points) {
    stroke(255, 255, 255) ;
    vertex(v.x, v.y, v.z) ;
    hu += 0.1;
    rotateY((hu/255)/360);
    
  }
  endShape();
  
}
