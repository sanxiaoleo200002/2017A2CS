#Leo Qiu Jingfa Opt3

d = {}
d('OS') = ('Operating System')
d('RAM') = ('Randon Access Memory')
d('ROM') = ('Read Only Memory')
d('ADC') = ('Algrithm Digital Convert')
d('DAC') = ('DIgital Algrithm Convert')

def insert(key,record):
    index = hash(record)
    while index is not Null:
        index += index
        if index > Max:
            index = 1
        hash(index) = newrecord

def find(searchkey,record):
    index = hash(searchkey)
    while index.searchkey !=searchkey and index is not Null:
        index +=index
        if index > Max:
            index = 0
    if  index is not Null:
        return index
