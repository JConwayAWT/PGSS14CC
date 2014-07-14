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

class GravitationalTravelingSalesmanSolver (TravelingSalesmanSolver.TravelingSalesmanSolver):
      bestOrder=[];
      CM = Coordinate.Coordinate(0, 0, 0);
      bestDistance=float("inf");
      current = Coordinate.Coordinate(0, 0, 0);
      pointsLeft = [];

      def __init__(self):
        pass

      def solve(self):
        if len(self.cords) < 3:
            BruteForceTravelingSalesmanSolver.solve();
        for index in range(0, len(self.cords)):
            self.pointsLeft.append(self.cords[index]);
        self.bestDistance=float("inf");
        index = self.findFarthest();
        if index > 0:
            temp = self.cords[index];
            self.cords[index] = self.cords[0];
            self.cords[0] = temp;
        else:
            temp = self.cords[index];
            self.cords[index] = self.cords[len(self.cords) - 1];
            self.cords[len(self.cords) - 1] = temp;
        current = self.cords[0];
        self.compute();
        self.getAnswer();
        return self.answer;

      def getAnswer(self):
        for c in self.bestOrder:
          self.answer+=str(c.i)+","

      def getCM(self):
        xsum = 0.0;
        ysum = 0.0;
        for i in range(0, len(self.cords)):
            xsum += self.cords[i].x;
            ysum += self.cords[i].y;
        CM = Coordinate(self, xsum/len(self.cords), ysum/len(self.cords), 0);
        return CM;

      def findFarthest(self):
        maxdist = 0.0;
        i = 0;
        for k in range(0, len(self.cords)):
            if self.cords[k].dist(self.CM) > maxdist:
                maxdist = self.cords[k].dist(self.CM);
                i = k;

        return i;

      def compute(self):
        while len(self.pointsLeft) > 0 :
            minEnergy = float("inf");
            index = 0;
            for i in range(1, len(self.pointsLeft)):
                energy = 1.0/self.current.dist(self.pointsLeft[i]) - 1.0/self.lineDistance(self.current, self.pointsLeft[i], self.CM);
                if energy < minEnergy:
                    minEnergy = energy;
                    index = i;
            bestOrder.add(pointsLeft[i]);
            current = pointsLeft[i];
            pointsLeft.remove(i);

      def lineDistance(self, point1, point2, CM):
        if point1.x == point2.x:
            if point1.y > self.CM.y and point2.y < self.CM.y or point1.y < self.CM.y and point2.y > self.CM.y:
                return self.CM.x - point1.x;
            else:
                return(min(point1.dist(self.CM), point2.dist(self.CM)));
        #maximum = max(point1.dist(self.CM), point2.dist(self.CM));
        #if(math.sqrt(maximum**2 - pow(self.CM.x - point1.x, 2))):
        #PERFORM TEST HERE TO FIND OUT WHETHER PERPENDICULAR FROM CM LIES ON SEGMENT OR NOT!!! INVOLVES RIGHT TRIANGLES AND INEQUALITY!
        numerator = -(point2.y + point1.y)/(point2.x - point1.x)*CM.x +(point1.x)*(point2.y - point1.y)/(point2.x - point1.x)*point1.x - point1.y;
        denominator = math.sqrt(pow((point2.y - point1.y)/(point2.x - point1.x), 2) + 1);
        return numerator/denominator;

gravity = GravitationalTravelingSalesmanSolver();
gravity.cords.append(Coordinate.Coordinate(0, 0, 0));
gravity.cords.append(Coordinate.Coordinate(0, 8, 0));
gravity.cords.append(Coordinate.Coordinate(8, 0, 0));
print(gravity.solve());