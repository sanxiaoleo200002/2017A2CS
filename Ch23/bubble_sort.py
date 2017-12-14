#Leo Qiu Opt3

def bubbleSort(list1):
    for passnum in range(len(list1)-1,0,-1):
        for i in range(passnum):
            if list1[i]>list1[i+1]:
                temp = list1[i]
                list1[i] = list1[i+1]
                list1[i+1] = temp
list1 =[]
bubbleSort(list1)
print(list1)
