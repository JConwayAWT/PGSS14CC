def makeList(testChain):
    testList = []
    a = 0 #used to parse through testChain and return the individual characters

    while a < len(testChain):
        testList.append(testChain[a])
        a += 1

    return testList

amino_acid_chain = input()

print amino_acid_chain

amino_acid_list = makeList(amino_acid_chain)

print amino_acid_list