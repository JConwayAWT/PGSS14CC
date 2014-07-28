class Alpha_Beta(ProteinChainClass.ProteinChain):
    print "This code has started"
    def solve(self, amino_acid_chain):#(self, coordinates)
    # the input should look like: 'PHHPHHHPPHHHPHPHPPPHHHPHPHPHPHP'
        #place second amino acid
        hPoints = 0
        pPoints = 0
        sumPoints = 0
        valueH = 3
        valueP = 1
    ##        while #empty space around amino acid
    ##
    ##        if filled #next to something (x - 1 in coords and y - 1 in coords, etc)
    ##            if#next to h
    ##
    ##            else#next to p

        self.chosen_coords = [[0,0]]
        for m in range(len(self.amino_acid_chain)):
            end_coord = deepcopy(self.chosen_coords[-1])
            test_coords = [[end_coord[0] + 1, end_coord[1]],[end_coord[0] - 1, end_coord[1]],[end_coord[0], end_coord[1] + 1],[end_coord[0], end_coord[1] - 1]]
            #^list of possible coords to choose from
            n = 0
            while n < 4:
                if test_coords[n] in self.coords:#if the space is filled
                    test_coords.pop(n)
                n = n+1
            #made a list of possible empty coordinates

            n = 0 #resetting increment
            #adjacent point system
            i = 0 #making new increment to test each possible empty space
            evaluted_coord = test_coords[i]
            coord_points = [0]#new list of points whose indices match up with those of test_coords
            while i < len(test_coords):
                test_evaluated_coords = [[evaluated_coord[0] + 1, evaluated_coord[1]],[evaluated_coord[0] - 1, evaluated_coord[1]],[evaluated_coord[0], evaluated_coord[1] + 1],[evaluated_coord[0], evaluated_coord[1] - 1]]
                #^looking at each location-neighbor of each test_coord

                while n < 4:
                    if test_evaluated_coords[n] in self.coords:
                        #if this possible coord has location-neighbors
                        if amino_acid_chain[self.coords.index(test_evaluated_coords[n])] == "H":
                            hPoints = 3*valueH
                        else: #must be polar
                            pPoints = 3*valueP
                        sumPoints = hPoints + pPoints
                        coord_points.append(sumPoints)
                    n = n+1
                i = i +1

            ordered_coord_points = [coord_points.sort()]
            self.chosen_coords.append(test_coords[coord_points.index(ordered_coord_points[-1])])
            #appended the test_coord with most points to the list of possible coords
            ##
            ##n = 0; #reset increment again
            ###diagonal point system
            ##test_possible_coords = [[first_possible_coord[0] + 1, first_possible_coord[1] +1],[first_possible_coord[0] - 1, first_possible_coord[1] - 1],[first_possible_coord[0] - 1, first_possible_coord[1] + 1],[first_possible_coord[0] + 1, first_possible_coord[1] - 1]]
            ##while n <= 3:
            ##    if test_possible_coords[n] not in self.coords:
            ##        #if this possible coord has location-neighbors
            ##        if amino_acid_chain[self.coords.index(test_possible_coords[n])] == "H":
            ##            hPoints += 1*valueH;#multiplying by 1 is not necessary, but here it is for user-friendliness
            ##        else: #must be polar
            ##            pPoints += 1*valueP;
            ##    n = n+1;
            ##    sumPoints = hPoints + pPoints;
    while (len(amino_acid_chain) < 5):
        print (self.chosen_coords)#may need fixing
        amino_acid_chain = solve(amino_acid_chain)
    ##while len(chosen_coords) <
    ##print (self.chosen_coords)

#s = Alpha_Beta()
#s.solve("PPPHPHPPPHHPHPHPHPHHH")
