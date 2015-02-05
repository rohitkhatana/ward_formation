blocks = [1,2,3,4,5,6,7]
nearByBlock = {1: [3,5], 2: [3, 4], 3: [2, 1, 4], 4: [2,3,5], 5: [3, 4], 6: [3,7], 7: [6, 3] }
populationPerBlock = {1: 700, 2: 900, 3: 1000, 4: 600, 5: 800, 6: 700, 7: 900}
shapeOfBlock = {1: 50, 2: 30, 3: 80, 4: 20, 5: 40, 6: 70, 7: 20}

def populationIsFine(ward, currentBlock):
    if ward[1] + populationPerBlock[currentBlock] <= 2600:
        ward[1] = ward[1] + populationPerBlock[currentBlock]
        return ward
    return False

def shapeIsFine(ward, currentBlock):
    return True

def canAddBlock(ward, traversedBlock, currentBlock):
    if currentBlock in traversedBlock:
        return False
    if shapeIsFine(ward, currentBlock) and  populationIsFine(ward, currentBlock):
        return True
    else:
        return False
def addRemainingBlock(ward, remainingBlock, currentBlock):
    return [block for block in nearByBlock[currentBlock] if block not in remainingBlock and block not in ward]

def generateBlock(ward, remainingBlock, traversedBlock, index):
    #print traversedBlock
    #print remainingBlock
    if len(remainingBlock) == index: #and len(blocks) == len(traversedBlock):
        return ward
    if canAddBlock(ward, traversedBlock, remainingBlock[index]):
        ward[0].append(remainingBlock[index])
        traversedBlock.append(remainingBlock[index])
        remainingBlock += addRemainingBlock(ward[0], remainingBlock, remainingBlock[index])
    generateBlock(ward, remainingBlock, traversedBlock, index+1)
    return ward 


def initializeBlock():
    traversedBlock = []
    wards = []
    for block in blocks:
        if block not in traversedBlock:
            ward = [[block],populationPerBlock[block], shapeOfBlock[block]]
            remainingBlock = [nearBlock for nearBlock in nearByBlock[block]]
            traversedBlock.append(block)
            wards.append(generateBlock(ward, remainingBlock, traversedBlock, 0))
    print wards

if __name__ == "__main__":
    initializeBlock()
