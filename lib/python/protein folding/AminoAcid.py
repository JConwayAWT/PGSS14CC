class AminoAcid:
##    polarity #will be either A or B (A = hydrophobic, B = hydrophilic
##    num #tells the order of the amino acid change
##    locationx
##    locationy #the coordinates of the AminoAcid on the coordinate plane
##    isUsed #shows if the amino acid has been placed onto the coordinate plane

    def __init__(self):
        self.pole = None #Polarity of AA
        self.index = None #Index # of AA in chain
        self.coord = None #coordinate of Amino Acid
        self.pNeighbor = None #previousNeighbor
        self.nNeighbor = None #nextNeighbor

    def set_Polarity_and_Index(self,AAlist, indexnum):
        self.Pole = AAlist[indexnum]
        self.index = indexnum

    def setCoord(self,coord):
        self.coord = coord

    def setPreviousNeighbor(self,pAcid): #asks for a coordinate
        self.pNeighbor = pAcid
    def setNextNeighbor(self,nAcid): #asks for a coordinate
        self.nNeighbor = nAcid
