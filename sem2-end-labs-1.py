# Charlie CCG 1/24/2022

def filter_list(l):
    new_list =[]
    for x in l:
        if type(x) != str:
            new_list.append(x)
    return new_list

print(filter_list([1,2,'a','b']) == [1,2])
print(filter_list([1,'a','b',0,15]) == [1,0,15])
print(filter_list([1,2,'aasf','1','123',123]) == [1,2,123])
