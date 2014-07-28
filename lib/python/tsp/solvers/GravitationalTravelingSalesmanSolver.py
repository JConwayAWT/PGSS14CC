#-------------------------------------------------------------------------------
# Name:        Gravitational Traveling Salesman Solver
# Purpose:     Traveling salesman gravitational solver
# Narahari Bharadwaj


import os, sys;
lib_path = os.path.abspath('..');
sys.path.append(lib_path);
lib_path = os.path.abspath('../../helpers')
sys.path.append(lib_path)
import Coordinate;
import math;
import TravelingSalesmanSolver;
import LineOverlapEliminatorTravelingSalesmanSolver

class GravitationalTravelingSalesmanSolver (LineOverlapEliminatorTravelingSalesmanSolver.LineOverlapEliminatorTravelingSalesmanSolver):

      def __init__(self):
        self.initSolver()
        self.initOverlapSolver()

        self.bestOrder=[];
        self.CM = Coordinate.Coordinate(0, 0, 0);
        self.bestDistance=float("inf");
        self.current = Coordinate.Coordinate(0, 0, 0);
        self.pointsLeft = [];

      def solve(self):
        for index in range(len(self.cords)):
            #print self.cords[index].x
            #print self.cords[index].y
            self.pointsLeft.append(self.cords[index]);
        self.bestDistance= float("inf");
        self.CM = self.getCM();
        index = self.findFarthest();
        if index > 0:
            temp = self.cords[index];
            self.cords[index] = self.cords[0];
            self.cords[0] = temp;
            self.pointsLeft[index] = self.cords[index];
            self.pointsLeft[0] = temp;
        else:
            temp = self.cords[index];
            self.cords[index] = self.cords[len(self.cords) - 1];
            self.cords[len(self.cords) - 1] = temp;
            self.pointsLeft[index] = self.cords[index];
            self.pointsLeft[len(self.cords) - 1] = temp;
        self.current = self.cords[0];
        self.compute();

        bo = []
        for c in self.bestOrder:
          bo.append(c.i)
        self.bestOrder=bo

        if self.REMOVE_LINE_CROSSES:
            self.removeLineCrosses()

        self.getAnswer();
        #for i in range(0, len(self.bestOrder)):
            #print("X: " + str(self.bestOrder[i].x) + " Y: " + str(self.bestOrder[i].y));
        return self.answer;

      def getAnswer(self):
        for c in self.bestOrder:
          self.answer+=str(c)+","

      def getCM(self):
        xsum = 0.0;
        ysum = 0.0;
        for i in range(0, len(self.cords)):
            xsum += self.cords[i].x;
            ysum += self.cords[i].y;
        self.CM = Coordinate.Coordinate(xsum/len(self.cords), ysum/len(self.cords), 0);
        return self.CM;

      def findFarthest(self):
        maxdist = 0.0;
        i = 0;
        for k in range(0, len(self.cords)):
            if self.cords[k].dist(self.CM) > maxdist:
                maxdist = self.cords[k].dist(self.CM);
                i = k;
        return i;

      def compute(self):
        self.bestOrder.append(self.pointsLeft[0]);
        while len(self.pointsLeft) > 0 :
            minEnergy = float("inf");
            index = 0;
            self.pointsLeft.remove(self.current);
            for i in range(0, len(self.pointsLeft)):
                #print(str(i) + " " + str(self.current.dist(self.pointsLeft[i])));
                #print(" " + str(self.lineDistance(self.current, self.pointsLeft[i], self.CM)));
                if(self.lineDistance(self.current, self.pointsLeft[i], self.CM) == 0):
                    energy = float("inf");
                else:
                    if (self.lineDistance(self.current, self.pointsLeft[i], self.CM) == 0):
                        print "hi"
                    if (self.current.dist(self.pointsLeft[i]) == 0):
                        print "yay"
                    energy = -1.0/self.current.dist(self.pointsLeft[i]) + 1.0/self.lineDistance(self.current, self.pointsLeft[i], self.CM);
                if energy < minEnergy:
                    minEnergy = energy;
                    index = i;
            if len(self.pointsLeft) > 0:
                self.bestOrder.append(self.pointsLeft[index]);
                self.current = self.pointsLeft[index];

      def lineDistance(self, point1, point2, CM):
        if point1.x == point2.x:
            if point1.y > self.CM.y and point2.y < self.CM.y or point1.y < self.CM.y and point2.y > self.CM.y:
                return self.CM.x - point1.x;
            else:
                return(min(point1.dist(self.CM), point2.dist(self.CM)));
        #maximum = max(point1.dist(self.CM), point2.dist(self.CM));
        #if(math.sqrt(maximum**2 - pow(self.CM.x - point1.x, 2))):
        #PERFORM TEST HERE TO FIND OUT WHETHER PERPENDICULAR FROM CM LIES ON SEGMENT OR NOT!!! INVOLVES RIGHT TRIANGLES AND INEQUALITY!
        numerator = -(point2.y - point1.y)/(point2.x - point1.x)*CM.x + CM.y + (point1.x)*(point2.y - point1.y)/(point2.x - point1.x) - point1.y;
        denominator = math.sqrt(pow((point2.y - point1.y)/(point2.x - point1.x), 2) + 1);
        maxdist = max(point1.dist(self.CM), point2.dist(self.CM));
        pointdist = point1.dist(point2);
        if(maxdist**2 - abs(numerator/denominator)**2 > pointdist**2):
            return min(point1.dist(self.CM), point2.dist(self.CM));
        else:
            return abs(numerator/denominator);

#gravity = GravitationalTravelingSalesmanSolver();
#gravity.cords.append(Coordinate.Coordinate(0, 0, 0));
#gravity.cords.append(Coordinate.Coordinate(8, 0, 1));
#gravity.cords.append(Coordinate.Coordinate(1, 6, 2));
#gravity.cords.append(Coordinate.Coordinate(7, 6, 3));
#gravity.cords.append(Coordinate.Coordinate(0, 12, 4));
#gravity.cords.append(Coordinate.Coordinate(8, 12, 5));
#print(gravity.solve());