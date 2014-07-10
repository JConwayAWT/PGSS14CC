def makeList(testChain):
    testList = []
    a = 0 #used to parse through testChain and return the individual characters

    while a < len(testChain):
        testList.append(testChain[a])
        a += 1

    return testList