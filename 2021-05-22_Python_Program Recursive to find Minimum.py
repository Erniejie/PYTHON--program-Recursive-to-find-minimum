#python program Recursive to find minimum
"Computer Programming Tutor, May21,2021 "

def findMinNumber(Data,no):
    if (no == 1):
        return Data[0]
    return min(Data[no-1],findMinNumber(Data,no-1))

if __name__=="__main__":
    Data = [14,4,12,-6,56,12,2]
    no=len(Data)
    print("The Minimum Number is: "+str(findMinNumber(Data,no)))
