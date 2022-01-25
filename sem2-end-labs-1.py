# Charlie CCG 1/24/2022

def filter_list(l):
    lst1 =[] # Empty list for numbers only
    for x in l: # for loop for each item in the list
        if type(x) != str: # filter out the strings
            lst1.append(x) # add integers and floats to the new list
    return lst1 # return the new list with the strings filtered out

print(filter_list([1,2,'a','b']) == [1,2])
print(filter_list([1,'a','b',0,15]) == [1,0,15])
print(filter_list([1,2,'aasf','1','123',123]) == [1,2,123])
