class Alpha_Beta(ProteinChainClass.ProteinChain):
    def solver(self, coordinates):
        #place second amino acid
        next_point
        hPoints = 0;
        pPoints = 0;
        sumPoints = 0;
        valueH = 3;
        valueP = 1;
##        while #empty space around amino acid
##
##        if filled #next to something (x - 1 in coords and y - 1 in coords, etc)
##            if#next to h
##
##            else#next to p

self.possible_coords = [[0,0]];

end_coord = deepcopy(self.coords[-1])
test_coords = [[end_coord[0] + 1, end_coord[1]],[end_coord[0] - 1, end_coord[1]],[end_coord[0], end_coord[1] + 1],[end_coord[0], end_coord[1] - 1]]
#^list of possible coords to choose from
int(n = 0);
while n <= 3:
    if test_coords[n] not in self.coords:
        possible_coords.append[test_coords[n]];
    n = n+1;
#made a list of possible coordinates

n = 0;#resetting increment
#adjacent point system
first_possible_coord = possible_coords[-1];
test_possible_coords = [[first_possible_coord[0] + 1, first_possible_coord[1]],[first_possible_coord[0] - 1, first_possible_coord[1]],[first_possible_coord[0], first_possible_coord[1] + 1],[first_possible_coord[0], first_possible_coord[1] - 1]]
while n <= 3:
    if test_possible_coords[n] not in self.coords:
        #if this possible coord has location-neighbors
        if amino_acid_chain[self.coords.index(test_possible_coords[n])] == "H":
            hPoints = 3*valueH;
        else: #must be polar
            pPoints = 3*valueP;
    n = n+1;

n = 0; #reset increment again
#diagonal point system
test_possible_coords = [[first_possible_coord[0] + 1, first_possible_coord[1] +1],[first_possible_coord[0] - 1, first_possible_coord[1] - 1],[first_possible_coord[0] - 1, first_possible_coord[1] + 1],[first_possible_coord[0] + 1, first_possible_coord[1] - 1]]
while n <= 3:
    if test_possible_coords[n] not in self.coords:
        #if this possible coord has location-neighbors
        if amino_acid_chain[self.coords.index(test_possible_coords[n])] == "H":
            hPoints += 1*valueH;#multiplying by 1 is not necessary, but here it is for user-friendliness
        else: #must be polar
            pPoints += 1*valueP;
    n = n+1;

sumPoints = hPoints + pPoints;







while len(self.coords) < number_of_acids:
    print (self.coords)#may need fixing