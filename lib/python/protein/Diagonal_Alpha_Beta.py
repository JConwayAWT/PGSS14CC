
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
