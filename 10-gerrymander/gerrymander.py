from ElecDistricts import *



#panel = [[1,1,1,2,3,3,2,3,4,2,4,4,5,6,6,5,5,6],
#             [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6]]


#myArray = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
myArray1 = [ 0,0,0,1,2,1,1,1,2,0,1,2,1,1,1,2,1,0]
myArray2= [ 0,0,0,1,1,1,1,1,1,2,2,2,1,1,2,0,1,0]


#print(checkCellContig(myArray))
#addPanel(myArray1)
#addPanel(myArray2) 
#addPanel(myArray2) 
        
#printPanel(0)
#printPanel(1)
        


#Scenario 0
#situation where 1/3 of the voters are 1's but a randon districting plan is 
#more likely to give them no districts than two districts
#voters = [1,0,1,1,0,0,0,0,0,0,0,0,0,1,1,0,1,0]
"""
YOUR MISSION:
Experiment with different possible distributions of 0 and 1 voters in Lilliputia
 -- first by playing with this sheet, then programmatically with your python code --
       to find as many examples as possible of each...
0) a situation where 1/3 of the voters are 1's, but a random districting plan is more likely to 
   give them no districts than two districts.
      (Two out of six is what they would get if you had proportional representation.)
1) a situation where 1/3 of the voters are 1's, but where they win no districts (sus)
2) a situation where 1/3 of the voters are 1's, and they win 3 districts  (again, sus)
3) a situation where 1/3 of the voters are 1's, but there is simply no way for them to win more than one district (sus much?)
4) situations where half the voters are 1's. More open-ended exploration is in order...
    Which arrangements of their voters are most advantageous for Party 1?
5)    Which are least advantageous?
6)   Are there arrangements that are hard to gerrymander in either direction?

"""


def Assignment(Anum):
    if Anum == 0:
        print("Case 0 - Random plan - more likely to give them no districts than 2 districts")
        print("This is also an example of case 3 - no way to win more than 1 district")
    if Anum == 1:
        print("Case 1 - Win No Districts")
    if Anum == 2:
        print("Case 2 - Win 3 Districts")
    if Anum == 3:
        print("Case 3 - No More than 1 District win")
    if Anum == 4:
        print("Case 4a - Most advantageous for Party 1 winning")
    if Anum == 5:
        print("Case 4b - Least advantageousfor Party 1 winning")
    if Anum == 6:
        print("Case 4c - Most difficult to Gerrymander")
      
    if Anum <= 3:
        initVoters(18, 6)   # 1/3 split 6 out of 18
    else:
        initVoters(18,9)    # these questions deal with a 50/50 split
    count = 0
    while True:
        if calcWinDistribution(voters, Anum):
            count += 1      
        if nextVoters() == False:
            print(str(count)," different matches")
            printBestWinDistribution()
            
            break    
    print("")
    
buildPanels(0)        
printPanelBuffer()
Assignment(0)
Assignment(1)
Assignment(2)
Assignment(3)
Assignment(4)
Assignment(5)
Assignment(6)

    