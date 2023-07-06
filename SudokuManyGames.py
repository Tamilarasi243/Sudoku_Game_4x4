import random
import time
from colorama import Fore,init

init()

blueColor=Fore.BLUE
cyanColor=Fore.CYAN
greenColor=Fore.GREEN
whiteColor=Fore.LIGHTWHITE_EX
redColor=Fore.RED
yellowColor=Fore.LIGHTYELLOW_EX
magnataColor=Fore.MAGENTA

print(whiteColor+"-"*75)
print(yellowColor+"\n\t\t\t'...4x4 Sudoku...'\n")
print(whiteColor+"-"*75)

def firstBox(miss,zeroPos):
    if miss not in {List1[0][0],List1[0][1],List1[1][0],List1[1][1]}:
        a,b=zeroPos
        List1[a][b]=miss
    else:
        print(redColor+"Entered number already exists. Please enter a different number.")
        elseCheck(zeroPos)
        
def secondBox(miss,zeroPos):
    if miss not in {List1[0][2],List1[0][3],List1[1][2],List1[1][3]}:
        a,b=zeroPos
        List1[a][b]=miss
    else:
        print(redColor+"Entered number already exists. Please enter a different number.")
        elseCheck(zeroPos)


def thirdBox(miss,zeroPos):
    if miss not in {List1[2][0],List1[2][1],List1[3][0],List1[3][1]}:
        a,b=zeroPos
        List1[a][b]=miss
    else:
        print(redColor+"Entered number already exists. Please enter a different number.")
        elseCheck(zeroPos)


def fourthBox(miss,zeroPos):
    if miss not in {List1[2][2],List1[2][3],List1[3][2],List1[3][3]}:
        a,b=zeroPos
        List1[a][b]=miss
    else:
        print(redColor+"Entered number already exists. Please enter a different number.")
        elseCheck(zeroPos)


def elseCheck(zeroPos):
    while True:
            miss = int(input(magnataColor+"Enter missed number..."))

            if miss < 1 or miss > 4:
                print(redColor+"Invalid input, choose a number between 1 to 4...")
            else:
                if miss not in {List1[0][0], List1[0][1], List1[1][0], List1[1][1]}:
                    a, b = zeroPos
                    count = 0
                    for j in range(0, 4):
                        if List1[a][j] != miss and List1[j][b] != miss:
                            count += 1
                    if count == 4:
                        if zeroPos in {(0, 0), (0, 1), (1, 0), (1, 1)}:
                            firstBox(miss, zeroPos)
                            break
                        if zeroPos in {(0, 2), (0, 3), (1, 2), (1, 3)}:
                            secondBox(miss, zeroPos)
                            break
                        if zeroPos in {(2, 0), (2, 1), (3, 0), (3, 1)}:
                            thirdBox(miss, zeroPos)
                            break
                        if zeroPos in {(2, 2), (2, 3), (3, 2), (3, 3)}:
                            fourthBox(miss, zeroPos)
                            break
                else:
                    print(redColor+"Entered number already exists. Please enter a different number.")



while True:
    rowCount=1
    L1=[[0, 2, 4, 0], [1, 0, 3, 0], [0, 1, 2, 0], [2, 0, 1, 0]]
    #[3,2,4,1],[1,4,3,2],[4,1,2,3],[2,3,1,4]
    L2=[[4, 0, 1, 0], [3, 0, 2, 0], [1, 0, 4, 2], [2, 0, 3, 0]]
    #[4,2,1,3],[3,1,2,4],[1,3,4,2],[2,4,3,1]
    L3=[[3, 0, 0, 4], [2, 0, 3, 0], [0, 3, 4, 0], [0, 0, 1, 0]]
    #[3,1,2,4],[2,4,3,1],[1,3,4,2],[4,2,1,3]
    L4=[[2, 0, 1, 0], [3, 1, 0, 0], [1, 0, 2, 4], [4, 0, 3, 0]]
    #[2,4,1,3],[3,1,4,2],[1,3,2,4],[4,2,3,1]
    L5=[[4, 1, 0, 2], [2, 0, 1, 4], [1, 4, 2, 0], [0, 2, 0, 0]]
    #[4,1,3,2],[2,3,1,4],[1,4,2,3],[3,2,4,1]

    List1=random.choice([L1,L2,L3,L4,L5])

    startTime=time.time()

    for i in List1:
        if i==List1[0]:
            print(Fore.RED+str(i))
        else:
            print(greenColor+str(i))
    print(blueColor+"-"*75)

    for i in range(len(List1)):
        print(magnataColor + "Enter missing numbers from row...",yellowColor+str(rowCount))
        for j in range(len(List1)):
            if List1[i][j]==0:
                zeroPos=(i,j)
                
                while True:
                    miss=int(input(cyanColor+"Enter missed number..."))
                    if miss<1 or miss>4:
                        print(redColor+"Invalid input, choose number between 1 to 4...")
                    else:
                        a,b=zeroPos
                        count=0
                        for j in range(0,4):
                            if List1[a][j]!=miss and List1[j][b]!=miss:
                                count+=1
                        if count==4:
                            if zeroPos in {(0,0),(0,1),(1,0),(1,1)}:
                                firstBox(miss,zeroPos)
                                break
                            if zeroPos in {(0,2),(0,3),(1,2),(1,3)}:
                                secondBox(miss,zeroPos)
                                break
                            if zeroPos in {(2,0),(2,1),(3,0),(3,1)}:
                                thirdBox(miss,zeroPos)
                                break
                            if zeroPos in {(2,2),(2,3),(3,2),(3,3)}:
                                fourthBox(miss,zeroPos)
                                break
                        else:
                            print(redColor+"Entered number already exists. Please enter a different number.")
        if rowCount==4:
            break
        print(blueColor+"-"*75)
        for k in List1:
            if k==List1[rowCount]:
                print(Fore.RED+str(k))
            else:
                print(greenColor+str(k)) 
        print(blueColor+"-"*75)
        rowCount+=1               

    endTime=time.time()
    totalTime=endTime-startTime
    print(blueColor+"-"*75)
    print(yellowColor+"\t\t\t...Final Result...")
    print(blueColor+"-"*75)
    for i in List1:
        print(whiteColor+str(i))

    print(blueColor+"-"*75)
    print(yellowColor+"Total time: "+whiteColor+str(totalTime)+yellowColor+"\nYour IQ level: "+whiteColor+str((100-int(totalTime))))
    print(blueColor+"-"*75)

    choice=input(Fore.LIGHTRED_EX+"Do you want to continue(yes/no)...").lower()
    if choice!='yes':
        print(Fore.LIGHTMAGENTA_EX+"...Thank you for your time...")
        break