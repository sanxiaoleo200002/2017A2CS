#Leo Qiu Opt3

array = [53,21,60,18,42,19]
print(array)
for i in range(1, len(array)):
    if array[i - 1] > array[i]:
        temp = array[i]   
        index = i          
        while index > 0 and array[index - 1] > temp:
            array[index] = array[index - 1]    
            index -= 1
        array[index] = temp 
print(array)
