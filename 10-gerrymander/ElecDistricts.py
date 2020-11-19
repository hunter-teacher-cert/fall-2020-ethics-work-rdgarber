
rows, cols = (360, 18) 
panel = [[0 for i in range(cols)] for j in range(rows)] 
panelCount = 0


#we will define the possible group# of 3 cells in a 6x3 grid (18 square units)
# If every contingous group has exactly 3 cells and they must all be
# contiguous, we can have exactly 6. If we number them all, Group 1 will
# always start in the top left, and group 6 will always end in the bottom 
# right. We will list each possible group each space could contain:
possrows, posscols = (18,6)
possGroup = [[0 for i in range(posscols)] for j in range(possrows)] 

possGroup[0] = [1]
possGroup[1] = [1,2]
possGroup[2] = [1,2,3]

possGroup[3] = [1,2,3]
possGroup[4] = [1,2,3]
possGroup[5] = [2,3,4]

possGroup[6] = [1,2,3,4]
possGroup[7] = [2,3,4]
possGroup[8] = [2,3,4]

possGroup[9] = [2,3,4]
possGroup[10]= [3,4,5]
possGroup[11]= [3,4,5,6]

possGroup[12]= [3,4,5]
possGroup[13]= [4,5,6]
possGroup[14]= [4,5,6]

possGroup[15]= [4,5,6]
possGroup[16]= [5,6]
possGroup[17]= [6]

#print buffer declarations
MAXPRINT = 10
pcountArr = [0 for i in range(MAXPRINT)]
pcountArrSize = 0

MAXCELLS = 18
TOTALCELLS = 18     # track the total possible cells we are using
INUSECELLS = 6      # track the number of cells in use at a given time
#declarations for voter pupulations
voters = [0 for i in range(MAXCELLS)]



# we cycle through each possibility for each cell, and determine if this
# combination has (1) Exactly 3 cells of each of the 6 groups; and
# (2) All of the 6 groups of 3 cells are contiguous
# If so, we add it to the list of panels.
#  limit is maximum number of panels to build
#     limit = 0 is unlimited until all possibilities are generated
def buildPanels(limit):
    print("Building our districts.....")
    trackingArray =[0 for i in range(18)]
    #for i in range(18):   #initialize the tracking array
     #   trackingArray[i] = possGroup[i][0]  #start with initial possibilities
    while limit == 0 or panelCount < limit :
        if checkCellCount(trackingArray) and checkCellContig(trackingArray) and inSequence(trackingArray):
            addPanel(trackingArray)
        if nextTracking(trackingArray) == False:
            break
        
    
#function to check that the potential array contains 3 of each number 1-6
def checkCellCount(trackingArray):
    counter = [0,0,0,0,0,0] # keep track of number of each group -want all 3's
    #print(trackingArray)
    #print(".", end='')
    for x in range(18):
        gnum = possGroup[x][trackingArray[x]]
        counter[gnum-1] += 1   #add one to the count
    for y in counter:
        if y != 3:        
            return False
    return True        
    
    
def checkCellContig(trackingArray):
    for y in range(6):  # find each of the 6 numbers one at a time
        location = [0,0,0]
        count = 0
        for x in range(18):
            gnum = possGroup[x][trackingArray[x]]
            if (gnum == y + 1):  # match to our number
                location[count] = x   # save the location
                #print(count,y+1,x)
                count += 1
        # we have our 3 locations, lets see if they are contiguous
        # if the first two are contiguous, then we need to check that either must be contiguous with the third
        if (isContig(location[0],location[1])):
            if (isContig(location[0],location[2]) or isContig(location[1],location[2])):
                continue
        #the only other way it could be contiguous (if 0-1 is not) is for 0-2 and 1-2 to be contiguous
        elif (isContig(location[0],location[2])):
            if (isContig(location[1],location[2])):
                continue
        return False
    # -------------------------------------------------    
    #if we got to the bottom then all 6 groups are contiguous    
    return True        

#checks if two spots on the 6x3 grid are contiguous (numbered 0-17 left to right up to down)
# assume the spots are always ascending 
def isContig(loc1, loc2):
    #print("Comp: ", end='')
    #print(loc1,end=' ')
    #print(loc2,end=' ')
    if (loc2 == loc1 + 1 and loc2 %3 >0): # consecutive locations on the same row
        #print("True")
        return True
    if (loc2 == loc1 + 3):  # next row down
        #print("True")
        return True
    #print("False")
    return False    # if not directly to the right or down one row, they are not contiguous


#we want to cut out duplicates - so we make sure that no number 1-6 appears AFTER an earlier
# number has appeared
def inSequence(trackingArray):
    firstAppear = [0,0,0,0,0,0]
    for x in range(18):
        gnum = possGroup[x][trackingArray[x]]
        if firstAppear[gnum - 1] == 0:
            firstAppear[gnum - 1] = x + 1   # store first appearance
    for y in range(5):       
        if firstAppear[y+1] < firstAppear[y]:  # out of sequence
            # carve out exception where last column is 666 and thats what caused the exception
            if y == 4 and firstAppear[5] == 12:
                return True # this is not a problem
             
            #for z in range(6):
            #    for zz in range(3):
            #        gnum = possGroup[3*z + zz][trackingArray[3*z + zz]]
            #        print(gnum, end=' ')
            #    print("")    

            return False
    # if we got to here, we are in sequence
    return True
        
        
def printPanel(pnum):
    global panelCount
    print("Panel",end=' ')
    print(panelCount+1)
    for x in range(6):
        for y in range(3):
            print (panel[pnum][3*x + y], end=' ')
        print("") 
    print("")
    

    
def addPrintPanelBuff(pnum):
    global pcountArrSize
    pcountArr[pcountArrSize] = pnum   #track which array number we are storing
    pcountArrSize +=1
    
    if (pcountArrSize % MAXPRINT == 0):   # we hit the maximum print buffer, so empty it
        printPanelBuffer()
        
def printPanelBuffer():
    global pcountArrSize
    if (pcountArrSize == 0):  # nothing to do here, the buffer is empty
        return  
    #print out the headers
    for p1 in range(pcountArr[0], pcountArr[0] + pcountArrSize):
        print("Panel",end=' ')
        print(p1 + 1, end = '   ')
        if (p1 + 1 < 10):
            print("", end= '  ')
        elif (p1 + 1 < 100):    
            print("", end= ' ')
        
    print("")
    #print out each of the 6 rows one at a time
    for x in range(6):
        for p1 in range(pcountArr[0], pcountArr[0] + pcountArrSize):
            for y in range(3):
                print(panel[p1][3*x + y], end=' ')
            print("      ", end='')
        print("")
        
    pcountArrSize = 0   #reset the buffer
    print("")   # add a blank line at the end
     
    
def addPanel(trackingArray):
    global panelCount
    for y in range(18):
         panel[panelCount][y] = possGroup[y][trackingArray[y]]
    addPrintPanelBuff(panelCount)
    panelCount += 1 
 

def nextTracking(trackingArray):
    for x in reversed(range(17)):
        trackingArray[x]+=1
        if trackingArray[x] >= len(possGroup[x]):
            trackingArray[x] = 0    # reset to the first one again and go up
        else:
            return True   
    return False    #if we got here we got to the top cannot go up further



# returns number of districts wins
def winCount(voters, myPanel):
    votecount = [0, 0, 0, 0, 0, 0]
    for x in range(18):
        if voters[x] == 1:
            district = panel[myPanel][x]
            votecount[district - 1] += 1
    # Ok, we have the votes in each district. We win if we have 2 or more votes
    winners = 0
    for y in range(6):
        #print(y+1,votecount[y])
        if votecount[y] > 1:
            winners += 1
    #printPanel(myPanel)
    #print("Count = ", str(winners))
  
    return winners


def printWinDistribution(winDistribution):
    # now, display it:
    for x in range(7):
        pct = 100 * (winDistribution[x] / panelCount)
        print(str(x) + " districts: " + str(winDistribution[x]) + "        "+ str(round(pct,2)) +"%")
    print("TOTAL PLANS: "+ str(panelCount))
  
"""  
Filters:
0 a situation where 1/3 of the voters are 1's, but a random districting plan is more likely to 
   give them no districts than two districts.
1) a situation where 1/3 of the voters are 1's, but where they win no districts (sus)
2) a situation where 1/3 of the voters are 1's, and they win 3 districts  (again, sus)
3) a situation where 1/3 of the voters are 1's, but there is simply no way for them to win more than one district (sus much?)
4) situations where half the voters are 1's. More open-ended exploration is in order...
    Which arrangements of their voters are most advantageous for Party 1?
5)    Which are least advantageous?
6)   Are there arrangements that are hard to gerrymander in either direction?
 
"""

bestDistribution= [0,0,0,0,0,0,0]   # best distribution
bestVoters = [0 for i in range(MAXCELLS)]

# function copies the latest distribution to the bestDistribution
# and stores the voting distribution in bestVoters
def copyToBest(winDistribution):
    for x in range(7):   # Copy our best range
        bestDistribution[x] = winDistribution[x]
    for x in range(MAXCELLS):   # Copy our best voters
        bestVoters[x] = voters[x]

def calcWinDistribution(voters, filter):
    winDistribution = [0,0,0,0,0,0,0]   # initialize counts
#first calculate the winner distribution
    for panelNum in range(panelCount):
        winDistribution[winCount(voters, panelNum)] += 1
    if filter == 0:
        if winDistribution[0] > winDistribution[2]:
            #print (voters)
            if winDistribution[0] > bestDistribution[0]: 
                copyToBest(winDistribution)
            return True
    if filter == 1:
        if winDistribution[0] > 0:
            #print (voters)
            if winDistribution[0] > bestDistribution[0]: 
                copyToBest(winDistribution)
            return True
    if filter == 2:  # 3 wins!
        if winDistribution[3] > 0:
            #print (voters)
            if winDistribution[3] > bestDistribution[3]: 
                copyToBest(winDistribution)
            return True
    if filter == 3:
        if winDistribution[2] == 0 and winDistribution[3] == 0:
            #print (voters)
            if winDistribution[0] > bestDistribution[0]: 
                copyToBest(winDistribution)
            return True
    if filter == 4:  # looking for the highest winning distributions - best we can do is 4 wins
        if winDistribution[4] > 0:
            #print (voters)
            if winDistribution[4] > bestDistribution[4]: 
                copyToBest(winDistribution)
            return True
    if filter == 5:  # looking for the lowest winning distributions - worst we can do is 2 wins
        if winDistribution[2] > 0:
            #print (voters)
            if winDistribution[2] > bestDistribution[2]: 
                copyToBest(winDistribution)
            return True
    if filter == 6:  # looking for the most even distributions - looing for most of the median 3 wins
        if winDistribution[3] > 0:
            #print (voters)
            if winDistribution[3] > bestDistribution[3]: 
                copyToBest(winDistribution)
            return True

    return False        # not an exceptional case
                    
        
def printBestWinDistribution():
    print("Best Example:")
    print(bestVoters)
    printWinDistribution(bestDistribution)
    

  
# total - total number of cells (for a 6x3 grid this would be 18)
# inUse - number of cells our group is populated in. 


def initVoters(total, inUse):
    global TOTALCELLS
    global INUSECELLS
    TOTALCELLS = total
    INUSECELLS = inUse
    for x in range(total):
        voters[x] = 0  # first clear everything out
    for x in range(inUse): # now set the first part (inUse) to all ones
        voters[x] = 1

# algorithm - we take the highest voter, and add one to it.
    #   if it is already at the max, we go up and find the next voter:
    #    if it itself is at its max (one below the max for the highest voter, we go up one more
    #     we we find one not at the max, we start all of the subsequent voters sequentially after it
    #    however, if there are no more voters up, then we are done, and return False.
    #    when we set the new voter, we return true
def nextVoters():
    global TOTALCELLS
    global INUSECELLS
    # get lowest voter
    for x in range (TOTALCELLS-1, -1, -1):
        #print(x, voters[x])
        if voters[x] == 1 : break
    

    if x < TOTALCELLS - 1:
        voters[x] = 0   # move one up
        voters[x + 1] = 1
        return True
    # we are already at the bottom, so keep track of levels going up    
    level = x
    while voters[level] == 1:
        level -= 1
        if TOTALCELLS - level > INUSECELLS : return False  # we are at the top
    # we are at a 0, not at our max, so we keep backing up until we find a 1
    levelsUp = TOTALCELLS - level
    while voters[level] == 0:
        level -= 1
    # now move the 1 down, and add the lower ones on, so 1,0,0,1,1 becomes 1,1,1,0,0
    voters[level] = 0
    for x in range(level + 1, TOTALCELLS):
        if x < level + levelsUp + 1:
            voters[x] = 1
        else:
            voters[x] = 0
    return True


    
    
    

        



