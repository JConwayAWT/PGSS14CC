#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Guirong
#
# Created:     10/07/2014
# Copyright:   (c) Guirong 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Name:        Protein Generator
# Purpose:
#
# Author:      Guirong
#
# Created:     09/07/2014
# Copyright:   (c) Guirong 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random

hydrophobicA = ['A', 'A', 'A', 'A', 'A', 'A', 'A']
hydrophilicB = ['B', 'B', 'B', 'B', 'B', 'B', 'B','B', 'B', 'B', 'B', 'B', 'B']
totalAminoAcids = hydrophobicA + hydrophilicB

def repeatedAAGen(n):    # generate AAs
    chain = ""
    counter = 0
    while counter < n:
        acid = random.choice(totalAminoAcids)
        chain += acid
        counter += 1
    return chain

n=21
chain = repeatedAAGen(n)
print chain