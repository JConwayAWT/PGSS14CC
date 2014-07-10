/**
Lines never seem to overlap in solutions

*/

int cities=0;
int tests=0;
double coefficientStart=0;
double coefficient=coefficientStart;
double coefficientIncrease=.00001;
double coefficientMax=5;
int moving=0;
double best=Integer.MAX_VALUE;
boolean drawShortest=true;
boolean drawBackground=true;
ArrayList<Coordinate>  bestOrder = new ArrayList<Coordinate>();
ArrayList<Coordinate>  cords = new ArrayList<Coordinate>(); 

double phernomes [][];
int CALCULATIONS=100000;
double travelIncrease=.1;
boolean traversed[];
int numTraversed=0;
int start=0;
int totalDistance=0;
int bestDistance=99999;
double PHERNOME_SCALE=1000;
long startTime=0;


class Coordinate {
  float x, y;
  int i;
  Coordinate(float x, float y) {
    this.x=x;
    this.y=y;
    this.i=cities;
  }  
  float dist(Coordinate a) {
    return sqrt(pow(x-a.x, 2)+pow(y-a.y, 2));
  }
}
class Color{
   int r,g,b;
  Color(int r, int g, int b){
     this.r=r;
     this.g=g;
     this.b=b;
  } 
}


void findEdges(){
  Coordinate c = new Coordinate(0,0);
  cords.add(c);
  moving=cities; 
  cities++;
  drawShortest=false;
  HashMap<Integer, Color> colors = new HashMap<Integer, Color>();
  int sz=15;
  for(int x=0;x<width;x+=sz){
    for(int y=0;y<height;y+=sz){
      c.x=x;
      c.y=y;
      computeShortestPath();
      int bp=intBestPath();
      if(!colors.containsKey(bp)){
        println("new color");
        colors.put(bp,new Color((int)random(0,255),(int)random(0,255),(int)random(0,255))); 
      }
      Color col =colors.get(bp);
      fill(col.r,col.g,col.b);
      stroke(col.r,col.g,col.b);
      rect(x,y,sz,sz);
      //println(x+" "+y+" "+bp);
    }
    println(x);
  }
  cords.remove(c);
  cities--;
  drawShortest=true;
}

int intBestPath(){
  int bestP=0;
  if (bestOrder.size()>0) {
    for (Coordinate c : bestOrder) {
      bestP*=10;
      bestP+=c.i;
    }
  }  
  return bestP;
}

void computeShortestPath() {
  best=Integer.MAX_VALUE;
  if(drawShortest&&drawBackground){
    drawBack();
  }
  if (cities>0) {
    if(drawShortest){
      drawCoordinates();
    }
    tests=0;  
    compute(0, 0, -1, new ArrayList<Coordinate>());
    if(drawShortest){
      drawBestPath();
    }
  }
}

void drawBack(){
  fill(0, 0, 0);
  stroke(0, 0, 0);
  rect(0, 0, width, height);
}

void drawLine(int a, int b) {
  Coordinate p = cords.get(a);
  Coordinate c = cords.get(b);
  int offset=2;
  line(p.x+offset, p.y+offset, c.x+offset, c.y+offset);
}

void drawCoordinates() {
  int i=0;
  for (Coordinate c : cords) {
    if(moving==i){
      fill(255, 255, 0);
    }else{
      fill(255, 0, 0);
    }
    ellipse(c.x, c.y, 10, 10);
    i++;
  }
}
void drawBestPath() {
  if (bestOrder.size()>0) {
    Coordinate p=bestOrder.get(bestOrder.size()-1);
    for (Coordinate c : bestOrder) {
      if(!drawBackground){
        stroke(0, 0, 0);
      }else{
        stroke(0, 255, 0);
      }
      line(p.x, p.y, c.x, c.y);
      p=c;
    }
  }
}
void compute(long traversed, double len, int srcNum, ArrayList<Coordinate> order) {
  if (traversed==pow(2, cities)-1) {
    len+=order.get(order.size()-1).dist(order.get(0));
    if (len<best) {
      best=len;
      bestOrder=order;
    }
    tests++;
    return;
  }

  Coordinate src=null;
  if (srcNum>=0) {
    src=cords.get(srcNum);
  }
  
  double farthest=0;
  int f=-1;
  for (int i=0; i<cords.size (); i++) {
    if (!checkTraversed(traversed, i)) {
      double dist = (srcNum == -1)?0:src.dist(cords.get(i));
      farthest = Math.max(farthest,dist);
      f=i;
    }
  }
  
  for (int i=0; i<cords.size (); i++) {
    if (!checkTraversed(traversed, i)) {
      double dist = (srcNum == -1)?0:src.dist(cords.get(i));
      ArrayList<Coordinate> o = (ArrayList<Coordinate>)(order.clone());
      o.add(cords.get(i));
      compute(setTraversed(traversed, i), len+dist, i, o);
    }
  }
}

long setTraversed(long traversed, int n) {
  return traversed | 1<<n;
}

boolean checkTraversed(long traversed, int n) {
  return (traversed & 1<<n)>0;
}

void setup() {
  size(400, 300);
  computeShortestPath();
}
void draw() {
}

void removeCitiesNear(Coordinate c) {
  for (Coordinate n : cords) {
    if (c.dist(n)<20) {
      cords.remove(n);
      cities--;
      computeShortestPath();
      break;
    }
  }
}
void mouseDragged() {
  Coordinate c = new Coordinate(mouseX, mouseY);
  if ( mouseButton == RIGHT) {
    removeCitiesNear(c);
  } else {
    if (moving>=0) {
      cords.get(moving).x=mouseX;
      cords.get(moving).y=mouseY;
      computeShortestPath();
    }
  }
}
void mousePressed() {
  Coordinate c = new Coordinate(mouseX, mouseY);
  if ( mouseButton == RIGHT) {
    removeCitiesNear(c);
  } else {    
    moving=-1;
    int i=0;
    for (Coordinate n : cords) {
      if (c.dist(n)<20) {
        moving=i;
        break;
      }
      i++;
    }
    if(moving==-1){
      cords.add(c);
     moving=cities; 
      cities++;
      computeShortestPath();
    }
  }
}

void keyPressed() {
  if (key=='c') {
    cities=0;
    cords = new ArrayList<Coordinate>();
    computeShortestPath();
  }
  if (key=='a') {
    computeShortestPath();
    antTraverse();
    printBestPath();
  }
  if(key=='f'){
     findEdges();
     drawBackground=false;
     computeShortestPath();
    drawBackground=true; 
  }
  if(key=='r'){
   computeShortestPath(); 
  }
  if(key=='e'){
    drawBack();
   drawCoordinates(); 
  }
}

float distance(int a, int b) {
  return cords.get(a).dist(cords.get(b));
}

void antTraverse() {
  start=0;
  initArrays(); 
  int i=0;
  for (i=0; coefficient<=coefficientMax; i++) {
    resetArrays();
    oneStep(0);
    coefficient+=coefficientIncrease;
  }
  println("Ant: "+i);
}

void oneStep(int c) {
  numTraversed++;
  if (numTraversed>=cities) {
    totalDistance+=distance(c, start);
    return;
  }
  traversed[c]=true;
  float total=0;
  for (int j=0; j<cities; j++) {
    if (traversed[j])continue;
    total+=1+phernomes[c][j];
  }
  double r = Math.random()*total;
  float cur=0;

  int j=0;
  for (j=0; j<cities; j++) {
    if (traversed[j])continue;
    cur+=1+phernomes[c][j];
    if (cur>r) {
      totalDistance+=distance(c, j);
      oneStep(j);
      break;
    }
  }
  phernomes[c][j]+=coefficient/pow((float)totalDistance,(float)coefficient);
}
void printBestPath() {
  resetArrays();
  bestStep(0);
}

void bestStep(int c) {
  numTraversed++;
  if (numTraversed>=cities) {
    drawLine(c, 0);
    totalDistance+=distance(c, 0);
    return;
  }
  traversed[c]=true;
  double best=0;
  int bc=0;
  for (int i=1; i<cities; i++) {
    if (traversed[i])continue;
    if (phernomes[c][i]>best) {
      best=phernomes[c][i];
      bc=i;
    }
  }
  if (bc==0) {
    totalDistance=Integer.MAX_VALUE;
  } else {
    totalDistance+=distance(c, bc);
    drawLine(c, bc);
    bestStep(bc);
  }
}
void initArrays() {
  phernomes= new double [cities][cities];
  coefficient=coefficientStart;
  resetArrays();
}
void resetArrays() {
  traversed = new boolean[cities];
  totalDistance=0;
  numTraversed=0;
}

