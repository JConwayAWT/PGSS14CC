import random

def repeatAAGen(n):    # generate AAs
## given a length n, return a string of length n
## consisting of A or B at each slot
    hydrophobicA = ['A', 'A', 'A', 'A', 'A', 'A', 'A']
    hydrophilicB = ['B', 'B', 'B', 'B', 'B', 'B', 'B','B', 'B', 'B', 'B', 'B', 'B']
    totalAminoAcids = hydrophobicA + hydrophilicB
    chain = ""
    counter = 0
    n = int(n)
    while counter < n:
        acid = random.choice(totalAminoAcids)
        chain += acid
        counter += 1
    return chain

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
